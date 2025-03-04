# repops-demo

## RepOps
Reproducible Operators (RepOps) is a library that ensures bitwise reproducibility of ML operations across different hardware. It solves the “nondeterminism” issue, where ML programs will often produce different outputs if they are executed on different devices. It works by controlling the order of floating point operations performed on all hardware, such that outputs will be bitwise identical, regardless of the device. This unlocks various use cases, including ML verification among untrusted nodes, reproducibility within academic research, and more.

## Prerequisites
* Disk space up to 20GB
* Docker (verify with `docker run hello-world`)

## Formally supported targets
We formally support the following hardware targets, including CPUs and Nvidia GPUs. For the GPUs, we require CC 7.5-9, and drivers should support CUDA 12.6 or later (560.28.03). Targets:
* x86_64
* arm64
* T4
* L4
* L40
* A40
* V100
* A100
* H100
* H200
* RTX 3090
* RTX 4070
* RTX 4090

## Instructions

Run:

 `sh run_docker_image.sh`

## Cleanup
Once you're done with the demo, you can delete the `llama-volume` with `docker volume rm llama-volume`
