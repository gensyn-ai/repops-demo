#!/bin/bash

# Check if a GPU is available by testing if nvidia-smi exists and runs.
if command -v nvidia-smi &>/dev/null && nvidia-smi &>/dev/null; then
    echo "GPU detected. Enabling GPU support."
    GPU_FLAG="--gpus all"
else
    echo "No GPU detected. Running without GPU support."
    GPU_FLAG=""
fi

docker run --rm $GPU_FLAG -it --pull always \
  -v "$(pwd)/repop-demo.py":/home/gensyn/repop_demo/repop-demo.py \
  -v "$(pwd)/download-llama.sh":/home/gensyn/repop_demo/download-llama.sh \
  briangen/repop-demo:latest bash
