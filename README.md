# repop-demo

## RepOp Summary
RepOp is a specialized library designed to facilitate reproducible deep learning by guaranteeing bitwise identical outcomes across various hardware platforms for identical training or inference tasks.


## Running the Demo
Below are some steps to run inference on a CausalLM flavor of Llama 3.2-1B-Instruct. 
Notably, this demo will show the pipeline that Gensyn uses for taking a Huggingface Model and lowering to RepOp
1. `sh run_docker_image.sh`
2. ./download-llama.sh && python ./repop-demo.py

## Known Targets Supported by the Demo
We support a variety of targets including CPUs and Nvidia GPUs for the demo. This list includesx
* x86_64
* arm64
* T4
* A100
* RTX 4090
* H100
* H200