#!/bin/bash

set -eou pipefail

if [ -f /home/gensyn/.profile ]; then
   # shellcheck source=/dev/null
   source /home/gensyn/.profile
fi

if [ ! -f ./Llama-3.2-1B-Instruct/model.safetensors ]; then
   ./download-llama.sh
fi

python repops-demo.py
