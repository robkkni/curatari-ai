import os
import argparse
from langroid.parsing.parser import Parser
from app.retrieval.weaviate_client import DocumentRetriever
from app.agent.config import weaviate_config

def parse_documents(directory_path):
    """Parse documents from a directory"""
    parser = Parser()
    documents = []
    
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                parsed_doc = parser.parse(file_path)
                documents.append({
                    "content": parsed_doc.text,
                    "metadata": {
                        "filename": file,
                        "path": file_path,
                        "filetype": os.path.splitext(file)[1],
                    },
                    "source": file_path,
                })
                print(f"Parsed: {file_path}")
            except Exception as e:
                print(f"Error parsing {file_path}: {e}")
    
    return documents

def ingest_documents(documents, retriever):
    """Ingest documents into Weaviate"""
    for doc in documents:
        retriever.ingest_document(
            content=doc["content"],
            metadata=doc["metadata"],
            source=doc["source"],
        )
        print(f"Ingested: {doc['source']}")

def main():
    parser = argparse.ArgumentParser(description="Ingest documents into Weaviate")
    parser.add_argument("--dir", required=True, help="Directory containing documents")
    args = parser.parse_args()
    
    # Parse documents
    documents = parse_documents(args.dir)
    print(f"Parsed {len(documents)} documents")
    
    # Ingest documents
    retriever = DocumentRetriever(weaviate_config)
    ingest_documents(documents, retriever)
    print("Ingestion complete")

if __name__ == "__main__":
    main()
