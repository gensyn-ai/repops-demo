#!/bin/bash

if [ -f /home/gensyn/.profile ]; then
   # shellcheck source=/dev/null
   source /home/gensyn/.profile
fi

if [ ! -f ./Llama-3.2-1B-Instruct/model.safetensors ]; then
   ./download-llama.sh
fi

exec python repops-demo.py
