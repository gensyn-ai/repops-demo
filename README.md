# repop-demo

## RepOp Summary
RepOp is a specialized library designed to facilitate reproducible deep learning by guaranteeing bitwise identical outcomes across various hardware platforms for identical training or inference tasks.


## Running the Demo
Notably, this demo will show the pipeline that Gensyn uses for taking a Huggingface Model and lowering it to RepOp.
After the model is converted, the demo will then run inference on your target hardware CPU (and GPU if you have one installed).
The result will show a hash of the output tensor showing a bit reproducible result. If you try the demo with a different target CPU/GPU,
you will end up getting the exact same result. The guarantee of RepOp to produce these results serves as the backbone of our 
verification system.

Below are some steps to run inference on a CausalLM flavor of Llama 3.2-1B-Instruct:
1. `sh run_docker_image.sh`
2. `./download-llama.sh && python ./repop-demo.py`

## Known Targets Supported by the Demo
We support a variety of targets including CPUs and Nvidia GPUs for the demo. This list includes:
* x86_64
* arm64
* T4
* A100
* RTX 4090
* H100
* H200