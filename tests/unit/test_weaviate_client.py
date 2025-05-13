#!/usr/bin/env python3
"""
Unit tests for the Weaviate client
"""

import unittest
import sys
import os

# Add the project directory to the path so we can import the modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.retrieval.weaviate_client import DocumentRetriever, Document

class TestWeaviateClient(unittest.TestCase):
    """Test cases for Weaviate client"""
    
    def test_document_creation(self):
        """Test document object creation"""
        doc = Document(
            content="Test content",
            metadata={"test": "metadata"},
            source="test/source"
        )
        
        self.assertEqual(doc.content, "Test content")
        self.assertEqual(doc.metadata, {"test": "metadata"})
        self.assertEqual(doc.source, "test/source")
    
    # Add more test cases as needed

if __name__ == "__main__":
    unittest.main()
