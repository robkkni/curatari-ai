import weaviate
import os
from typing import List, Dict, Any, Optional

class Document:
    """Document class to maintain compatibility with Langroid"""
    def __init__(self, content: str, metadata: dict, source: str):
        self.content = content
        self.metadata = metadata
        self.source = source

class DocumentRetriever:
    def __init__(self, weaviate_config):
        """Initialize Document Retriever with Weaviate v4 client
        
        Args:
            weaviate_config: Configuration with Weaviate connection details
        """
        self.config = weaviate_config
        self.url = weaviate_config.get("url", "http://localhost:8087")
        
        # Connect to Weaviate using v4 client
        self.client = weaviate.connect_to_local(
            port=8087,  # Default is 8080, but docker-compose uses 8087:8080 mapping
        )
        self.collection = self.client.collections.get("Document")
    
    def retrieve_documents(self, query: str, limit: int = 5) -> List[Document]:
        """Retrieve relevant documents for a query
        
        Args:
            query: The search query
            limit: Maximum number of documents to return
            
        Returns:
            List of document objects
        """
        try:
            # Use BM25 search for text retrieval
            results = self.collection.query.bm25(
                query=query,
                limit=limit
            )
            
            # Convert to document objects
            documents = []
            for obj in results.objects:
                doc = Document(
                    content=obj.properties.get("content", ""),
                    metadata=obj.properties.get("metadata", {}),
                    source=obj.properties.get("source", "")
                )
                documents.append(doc)
                
            return documents
        except Exception as e:
            print(f"Error retrieving documents: {e}")
            return []
    
    def ingest_document(self, content: str, metadata: dict, source: str) -> Optional[str]:
        """Ingest a document into Weaviate
        
        Args:
            content: Document text content
            metadata: Dictionary of metadata
            source: Source of the document
            
        Returns:
            Document ID or None if ingestion failed
        """
        try:
            # Create document object
            doc_id = self.collection.data.insert({
                "content": content,
                "metadata": metadata,
                "source": source
            })
            
            return doc_id
        except Exception as e:
            print(f"Error ingesting document: {e}")
            return None
    
    def close(self):
        """Close the Weaviate client connection"""
        if hasattr(self, 'client'):
            self.client.close()
    
    def __del__(self):
        """Destructor to ensure connection is closed"""
        self.close()