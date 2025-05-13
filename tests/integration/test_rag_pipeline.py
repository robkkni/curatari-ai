#!/usr/bin/env python3
"""
Integration test for the RAG (Retrieval Augmented Generation) pipeline
"""

import unittest
import sys
import os

# Add the project directory to the path so we can import the modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.retrieval.weaviate_client import DocumentRetriever

class TestRAGPipeline(unittest.TestCase):
    """Test cases for the RAG pipeline"""
    
    def setUp(self):
        """Set up test environment"""
        # This will run before each test
        self.retriever = DocumentRetriever({
            "url": "http://localhost:8087"
        })
        
        # Test document data
        self.test_content = "This is test content about neural networks and machine learning."
        self.test_metadata = {
            "filename": "test_doc.md",
            "filetype": "markdown"
        }
        self.test_source = "tests/data/documents/test_doc.md"
        
        # Insert test document
        self.doc_id = self.retriever.ingest_document(
            self.test_content,
            self.test_metadata,
            self.test_source
        )
    
    def tearDown(self):
        """Clean up after tests"""
        # This will run after each test
        # Close the retriever connection
        self.retriever.close()
    
    def test_retrieval(self):
        """Test document retrieval"""
        # Skip test if document insertion failed
        if not self.doc_id:
            self.skipTest("Document insertion failed")
        
        # Test retrieval
        docs = self.retriever.retrieve_documents("neural networks", limit=1)
        
        # Assert we got a document back
        self.assertTrue(len(docs) > 0)
        
        # Assert the document contains our test content
        self.assertEqual(docs[0].content, self.test_content)

if __name__ == "__main__":
    unittest.main()
