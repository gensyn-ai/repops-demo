# repops-demo

## RepOps Summary
Imagine a world where your deep learning experiments deliver bit-for-bit identical results—no matter the hardware, no matter the run. RepOps is the specialized library that makes this a reality. Designed to facilitate deterministic, reproducible outcomes, RepOps eliminates the chaos of hardware-induced variability in training and inference. For technical minds obsessed with trustless verification, control, consistency, and verifiable systems, RepOps isn’t just a tool — it’s the foundation for next-level ML reliability across CPUs, GPUs, and beyond for training and inference tasks.

## Prerequisites
* Disk space upto 100GB
* Docker (verify with `docker run hello-world`)
* An Nvidia GPU (optional, but preferred, with CC 7.5+)

## Unleashing the Demo: From Hugging Face to Hardware Harmony
This isn’t just a demo—it’s a front-row seat to the future of ML pipelines. We’ll take a Hugging Face model, lower it to RepOps, courtesy of the Gensyn workflow. After model conversion, the demo will execute inference on your hardware — starting with your CPU and flexing to an Nvidia GPU if you’ve got one handy. The payoff? A hashed output tensor that’s guaranteed to match, bit-for-bit, across any compatible hardware you throw at it. Different hardware, same model, same inputs, same hash—every time. It’s the bedrock of Gensyn’s verification system, ensuring trust and repeatability in distributed ML workloads.

Ready to see it in action? Here’s how to fire up inference with the CausalLM variant of Llama 3.2-1B-Instruct:

Kick things off with: `sh run_docker_image.sh`
Then roll: `./download-llama.sh && python ./repops-demo.py`
Experiment with different CPUs or GPUs. The hash won’t flinch. That’s the RepOps promise—determinism you can bank on, building for trustless verifiable distributed ML.

## Known Targets Supported by the Demo
We support a variety of hardware targets including CPUs and Nvidia GPUs (CC 7.5+) for the demo. This list includes:
* x86_64
* arm64
* T4
* A100
* RTX 4090
* H100
* H200