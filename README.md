# Curatari AI

An intelligent agent using Langroid, Chainlit, Weaviate, and llama.cpp to provide an intuitive interface to your documents.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Start Weaviate:
   ```
   cd weaviate
   docker-compose up -d
   python setup_weaviate.py
   ```

3. Start llama.cpp server:
   ```
   cd llm_server
   ./start_llama_server.sh
   ```

4. Start the app:
   ```
   chainlit run app/main.py
   ```

## Project Structure

- `app/`: Main application code
  - `agent/`: Langroid agent configuration
  - `retrieval/`: Document retrieval using Weaviate
  - `utils/`: Utility functions
- `llm_server/`: llama.cpp server configuration
- `weaviate/`: Weaviate setup
- `scripts/`: Utility scripts
- `data/`: Document storage
