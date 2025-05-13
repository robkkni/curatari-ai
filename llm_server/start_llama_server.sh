#!/bin/bash
# Configuration
MODEL_PATH="/mnt/d/mlstore01/models/Qwen3-30B-A3B-128K-Q8_0.gguf"
PORT=8080
CONTEXT_SIZE=131072  # 128K tokens
THREADS=12

# Start server
~/src/llama.cpp/build/bin/server \
  -m $MODEL_PATH \
  --port $PORT \
  --ctx-size $CONTEXT_SIZE \
  --threads $THREADS \
  --embedding \
  --host 0.0.0.0 \
  --log-format json
