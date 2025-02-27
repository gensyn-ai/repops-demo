#!/bin/bash

# download proper Llama version
mkdir -p Llama-3.2-1B-Instruct

echo "Downloading Llama-3.2-1B-Instruct..."

curl -o Llama-3.2-1B-Instruct/generation_config.json https://storage.googleapis.com/gensyn-public-models/Llama-3.2-1B-Instruct/generation_config.json
curl -o Llama-3.2-1B-Instruct/config.json https://storage.googleapis.com/gensyn-public-models/Llama-3.2-1B-Instruct/config.json
curl -o Llama-3.2-1B-Instruct/model.safetensors https://storage.googleapis.com/gensyn-public-models/Llama-3.2-1B-Instruct/model.safetensors
curl -o Llama-3.2-1B-Instruct/special_tokens_map.json https://storage.googleapis.com/gensyn-public-models/Llama-3.2-1B-Instruct/special_tokens_map.json
curl -o Llama-3.2-1B-Instruct/tokenizer.json https://storage.googleapis.com/gensyn-public-models/Llama-3.2-1B-Instruct/tokenizer.json
curl -o Llama-3.2-1B-Instruct/tokenizer_config.json https://storage.googleapis.com/gensyn-public-models/Llama-3.2-1B-Instruct/tokenizer_config.json
