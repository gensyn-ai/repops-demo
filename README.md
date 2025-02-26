# repop-demo

Steps to run Demo:

1. docker run --rm --gpus all -it --pull always -v "$(pwd)/repop-demo.py":/home/gensyn/repop_demo/repop-demo.py -v "$(pwd)/download-llama.sh":/home/gensyn/repop_demo/download-llama.sh  briangen/repop-demo:latest bash
2. ./download-llama.sh && python ./repop-demo.py