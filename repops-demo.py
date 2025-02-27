import gensyn_onnx2torch
import torch
from transformers import AutoModelForCausalLM
from repop.utils import set_determinism, get_hash, hash_tensors
from repop.rand import stable_randn
import warnings

EXPECTED_OUTPUT_HASH = (
    "04c6980d863a3ccf2ef12e182a9dfe388533157c697687f8e8f0e8640080018c"
)


def get_learnable_parameters(model: torch.nn.Module) -> set[str]:
    """
    Given a torch module, we return a set that contains the names of all trainable model parameters,
    i.e., those parameters where requires_grad==True
    """
    learnable_parameters: set[str] = set()
    for name, param in model.named_parameters():
        if param.requires_grad:
            learnable_parameters.add(name)
    return learnable_parameters


def run_reproducible_demonstration(model: torch.nn.Module, devices: list[str]):
    #
    # Step 1: export the model to onnx
    #
    shape = (2, 8)
    vocab_size = model.config.vocab_size

    dummy_data = [
        torch.randint(0, vocab_size, shape),
        torch.randint(0, 2, shape),
    ]
    input_names = ["input_ids", "attention_mask"]
    output_names = ["logits"]
    dynamic_axes = {
        "input_ids": {0: "batch_size", 1: "sequence_length"},
        "attention_mask": {0: "batch_size", 1: "sequence_length"},
        "logits": {0: "batch_size"},
    }

    print("Exporting original model to ONNX format...")
    exported = "model.onnx"
    with warnings.catch_warnings():
        # squelch noisy tracer warnings
        warnings.simplefilter("ignore")
        torch.onnx.export(
            model,
            tuple(dummy_data),
            exported,
            input_names=input_names,
            output_names=output_names,
            dynamic_axes=dynamic_axes,
            export_params=True,  # save the weights with it
            do_constant_folding=False,
            training=torch.onnx.TrainingMode.TRAINING,
        )

    print("Converting ONNX model to reproducible version...")
    #
    # Step 2: deserialize the onnx model into a reproducible version
    #
    repop_model = gensyn_onnx2torch.convert(
        exported,
        attach_onnx_mapping=True,
        learnable_parameters=get_learnable_parameters(model),
        requires_reproducibility=True,
    )

    #
    # Step 3: run an inference forward pass of the reproducible model and
    # present the hash of the output for demonstration purposes.
    #
    model_hash = get_hash(repop_model)
    print("\033[35mRepOps Model Hash:\033[0m")
    print(f"\033[1;37m{model_hash}\033[0m")

    print("\033[35mInput Data Hash:\033[0m")
    data_hash = hash_tensors(dummy_data)
    print(f"\033[1;37m{data_hash}\033[0m")

    for device in devices:
        repop_model = repop_model.to(device)
        dummy_data = [d.to(device) for d in dummy_data]
        print(f"Running RepOps Model for device = {device} ... ")
        repop_output = repop_model(*dummy_data)
        print("\033[35mRepOps Inference Output Hash:\033[0m")
        repop_output_hash = get_hash(repop_output)
        print(f"\033[1;37m{repop_output_hash}\033[0m")

        print("\033[35mExpected Inference Output Hash:\033[0m")
        print(f"\033[1;37m{EXPECTED_OUTPUT_HASH}\033[0m")

        if repop_output_hash == EXPECTED_OUTPUT_HASH:
            print("\033[32mBitwise output match - success!\033[0m")


if __name__ == "__main__":
    print("\033[35mRunning the RepOps Demo!\033[0m")
    # initialized weights are random (for pretrained: just the classifier layers)
    set_determinism(22)

    # llama on disk was previously downloaded
    model_path = "./Llama-3.2-1B-Instruct"
    # Note: presently gensyn_onnx2torch does not handle tied embeddings
    model_init_kwargs = {}
    model_init_kwargs["tie_word_embeddings"] = False
    model = AutoModelForCausalLM.from_pretrained(model_path, **model_init_kwargs)
    # For Non Tied Weights, initialization is not determinstic across different architectures.
    # Therefore, we initialize the weights of the lm_head to be reproducible.
    model.lm_head.weight = torch.nn.Parameter(
        stable_randn((model.lm_head.out_features, model.lm_head.in_features), False)
    )
    set_determinism(42)
    devices = ["cpu", "cuda:0"] if torch.cuda.is_available() else ["cpu"]
    run_reproducible_demonstration(model=model, devices=devices)
