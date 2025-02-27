#!/bin/bash

# Check if a GPU is available by testing if nvidia-smi exists and runs.
if command -v nvidia-smi &>/dev/null && nvidia-smi &>/dev/null; then
    echo "GPU detected. Enabling GPU support."
    GPU_FLAG="--gpus all"
else
    echo "No GPU detected. Running without GPU support."
    GPU_FLAG=""
fi

# We run as non-root inside the container, so using a named volume rather
# than a mountpoint to download llama. To remove just run
# `docker volume rm llama-volume`
docker run --rm $GPU_FLAG -it --pull always \
  -v "llama-volume:/home/gensyn/repop_demo/Llama-3.2-1B-Instruct" \
  -v "$(pwd)/execute.sh":/home/gensyn/repop_demo/execute.sh \
  -v "$(pwd)/repops-demo.py":/home/gensyn/repop_demo/repops-demo.py \
  -v "$(pwd)/download-llama.sh":/home/gensyn/repop_demo/download-llama.sh \
  europe-docker.pkg.dev/gensyn-public-b7d9/public/repop-demo:v0.0.1 ./execute.sh
