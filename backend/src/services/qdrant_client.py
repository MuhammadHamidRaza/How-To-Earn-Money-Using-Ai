import os
from qdrant_client import QdrantClient, models

def get_qdrant_client():
    """Initializes and returns a Qdrant client."""
    qdrant_url = os.getenv("QDRANT_URL")
    qdrant_api_key = os.getenv("QDRANT_API_KEY")

    if not qdrant_url or not qdrant_api_key:
        raise ValueError("QDRANT_URL and QDRANT_API_KEY environment variables must be set.")

    client = QdrantClient(
        url=qdrant_url,
        api_key=qdrant_api_key,
    )
    return client

def ensure_collection_exists(client: QdrantClient, collection_name: str, vector_size: int = 768):
    """Ensures that a Qdrant collection exists, creating it if necessary."""
    try:
        client.get_collection(collection_name=collection_name)
        print(f"Collection '{collection_name}' already exists.")
    except Exception:
        client.recreate_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
        )
        print(f"Collection '{collection_name}' created.")

if __name__ == "__main__":
    # This block is for local testing or initial setup
    # In a real application, these would be managed by your main application logic
    try:
        # Example usage:
        # Set dummy environment variables for local testing if they are not set
        if "QDRANT_URL" not in os.environ:
            os.environ["QDRANT_URL"] = "http://localhost:6333" # Or your Qdrant Cloud URL
        if "QDRANT_API_KEY" not in os.environ:
            os.environ["QDRANT_API_KEY"] = "dummy_api_key" # Or your actual API key

        client = get_qdrant_client()
        ensure_collection_exists(client, "book_content_collection")
        print("Qdrant client and collection setup complete (if environment variables were set or defaulted).")
    except ValueError as e:
        print(f"Error during Qdrant setup: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
