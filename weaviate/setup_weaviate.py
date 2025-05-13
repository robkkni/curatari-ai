import weaviate
from weaviate.classes.config import Property, DataType

def setup_weaviate_schema():
    """Initialize Weaviate schema using the v4 client"""
    # Initialize client with v4 syntax
    client = weaviate.connect_to_local(
        port=8087,  # Default is 8080, but your docker-compose uses 8087:8080 mapping
    )
    
    print("Connected to Weaviate")
    
    # Check if collection exists and delete if it does
    try:
        client.collections.delete("Document")
        print("Deleted existing Document collection")
    except Exception:
        print("No existing Document collection found")
    
    # Create the Document collection with v4 syntax
    document_collection = client.collections.create(
        name="Document",
        properties=[
            Property(
                name="content",
                data_type=DataType.TEXT,
                description="The content of the document"
            ),
            Property(
                name="metadata",
                data_type=DataType.OBJECT,
                description="Metadata about the document",
                nested_properties=[
                    Property(
                        name="filename",
                        data_type=DataType.TEXT,
                        description="The name of the file"
                    ),
                    Property(
                        name="filetype",
                        data_type=DataType.TEXT,
                        description="The type of the file"
                    ),
                    Property(
                        name="created_at",
                        data_type=DataType.DATE,
                        description="The creation date of the document"
                    )
                ]
            ),
            Property(
                name="source",
                data_type=DataType.TEXT,
                description="Source of the document"
            )
        ],
        # Skip vectorizer since we'll provide our own vectors
        vectorizer_config=None
    )
    
    print("Weaviate schema created successfully")
    print(f"Created collection: {document_collection.name}")
    client.close()

if __name__ == "__main__":
    setup_weaviate_schema()