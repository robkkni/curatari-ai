from langroid.agent.chat_agent import ChatAgentConfig
from langroid.language_models.openai_gpt import OpenAIGPTConfig
from langroid.vector_store.weaviate import WeaviateConfig
import os

# Load environment variables
LLM_API_KEY = os.getenv("LLM_API_KEY", "not-needed")  # llama.cpp doesn't need this
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:8080/v1")

# LLM Configuration
llm_config = OpenAIGPTConfig(
    model="Qwen3-30b-128k",  # Model identifier
    api_key=LLM_API_KEY,  # Not required for local llama.cpp
    openai_base_url=LLM_BASE_URL,  # Point to llama.cpp server
    temperature=0.7,
    top_p=0.9,
    max_tokens=2000,
    request_timeout=300,
)

# Weaviate Configuration
weaviate_config = WeaviateConfig(
    url="http://localhost:8087",
    index_name="Document",
    text_key="content",
    embedding_model_name="local",  # Use local embeddings from llama.cpp
    embedding_model_api_key=LLM_API_KEY,
    embedding_model_base_url=LLM_BASE_URL,
)

# Agent Configuration
agent_config = ChatAgentConfig(
    name="CuratariAgent",
    llm=llm_config,
    vector_store=weaviate_config,
    system_prompt="""
    You are Curatari AI, a helpful assistant with access to a knowledge base.
    When responding to queries, use your knowledge and the retrieved context.
    If you don't know something, say so - don't make up information.
    For each response, cite the sources you used from the retrieved documents.
    """
)
