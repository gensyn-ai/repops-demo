# repops-demo

## RepOps
Reproducible Operators (RepOps) is a library that ensures bitwise reproducibility of ML operations across different hardware. It solves the “nondeterminism” issue, where ML programs will often produce different outputs if they are executed on different devices. It works by controlling the order of floating point operations performed on all hardware, such that outputs will be bitwise identical, regardless of the device. This unlocks various use cases, including ML verification among untrusted nodes, reproducibility within academic research, and more.

## Prerequisites
* Disk space upto 20GB
* Docker (verify with `docker run hello-world`)
* An Nvidia GPU (optional, but preferred, with CC 7.0-9.0). Drivers should support Cuda 12.6 at minimum (560.28.03)

## Formally supported targets
We formally support a variety of hardware targets including CPUs and Nvidia GPUs (CC 7.5+) for the demo. This list includes:
* x86_64
* arm64
* T4
* V100
* A100
* RTX 3090

## Instructions

Run:

 `sh run_docker_image.sh`

## Cleanup
Once you are done with the demo, feel free to delete the llama-volume with `docker volume rm llama-volume`
