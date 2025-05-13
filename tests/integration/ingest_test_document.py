#!/usr/bin/env python3
"""
This script demonstrates how to ingest a document into Weaviate for testing.
It creates a sample document and ingests it into the Weaviate collection.
"""

import sys
import os
import datetime

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, project_root)

# Now import the DocumentRetriever
from app.retrieval.weaviate_client import DocumentRetriever

def ingest_sample_document():
    """Ingest a sample document into Weaviate for testing"""
    print("Creating sample document...")
    
    # Sample document content
    content = """
    # Curatari AI: A Next-Generation Document Assistant
    
    Curatari AI is a powerful document assistant that uses state-of-the-art language models 
    to help users find and understand information in their documents.
    
    ## Key Features
    
    - Advanced search capabilities with natural language queries
    - Document summarization and extraction
    - Question answering based on document content
    - Support for multiple document formats
    
    ## Technical Architecture
    
    Curatari AI uses a stack of cutting-edge technologies:
    
    1. Langroid for agent orchestration
    2. Qwen3-30B for language processing
    3. Weaviate for vector storage
    4. llama.cpp for local inference
    5. Chainlit for the user interface
    
    ## Future Directions
    
    Future plans include adding support for:
    
    - Document comparison
    - Automated document classification
    - Multi-language support
    - Integration with popular knowledge management tools
    """
    
    # Create metadata with RFC3339 compliant date format
    # Format: YYYY-MM-DDThh:mm:ssZ
    current_time = datetime.datetime.now(datetime.timezone.utc)
    formatted_date = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    
    metadata = {
        "filename": "curatari_overview.md",
        "filetype": "markdown",
        "created_at": formatted_date
    }
    
    # Source information
    source = "internal/documentation/overview.md"
    
    # Create document retriever
    retriever = DocumentRetriever({
        "url": "http://localhost:8087"
    })
    
    try:
        # Ingest document
        print("Ingesting document into Weaviate...")
        doc_id = retriever.ingest_document(content, metadata, source)
        
        if doc_id:
            print(f"Successfully ingested document with ID: {doc_id}")
        else:
            print("Failed to ingest document.")
            return False
        
        # Test retrieval
        print("\nTesting document retrieval...")
        query = "What technologies does Curatari AI use?"
        print(f"Query: '{query}'")
        
        docs = retriever.retrieve_documents(query, limit=1)
        if docs:
            print(f"Found {len(docs)} document(s)")
            print("\nDocument content (first 100 chars):")
            print(docs[0].content[:100] + "...")
            print("\nDocument metadata:")
            print(docs[0].metadata)
        else:
            print("No documents found.")
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        # Close the connection
        retriever.close()
    
    return True

if __name__ == "__main__":
    print("Starting document ingestion test...")
    success = ingest_sample_document()
    
    if success:
        print("\nDocument ingestion test completed successfully!")
    else:
        print("\nDocument ingestion test failed.")
        sys.exit(1)