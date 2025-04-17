#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Load environment variables from .env if it exists
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
  echo "✅ Environment variables loaded from .env"
else
  echo "⚠️  .env file not found. Skipping variable load."
fi

# Optional: Confirm critical env variable
if [ -z "$OPENAI_API_KEY" ]; then
  echo "❌ OPENAI_API_KEY not set. Did .env fail to load?"
else
  echo "🔑 OPENAI_API_KEY is set"
fi

# Optional: Kick off your app here (uncomment one)
# chainlit run app.py --watch
# uvicorn app:app --reload
