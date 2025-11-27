import os
from typing import List
from qdrant_client import QdrantClient, models
from backend.src.models.book import BookContent

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

def upsert_book_content_to_qdrant(client: QdrantClient, collection_name: str, content: BookContent):
    """Upserts a BookContent object into the specified Qdrant collection."""
    # Qdrant expects payload and vector. The ID can be content.id if it's unique.
    # Ensure embedding is a list of floats, and handle cases where it might be empty or None.
    vector = content.embedding if content.embedding else [0.0] * 768 # Default to 768 zeros if empty
    if not vector:
        raise ValueError("Embedding vector cannot be empty.")

    # Convert metadata to a dictionary for Qdrant payload
    payload = content.metadata.copy()
    payload["text_content"] = content.text # Store the full text in payload as well
    payload["book_content_id"] = content.id # Store the BookContent ID in payload

    client.upsert(
        collection_name=collection_name,
        points=models.Batch(
            ids=[content.id],
            vectors=[vector],
            payloads=[payload]
        )
    )
    print(f"Upserted BookContent with ID {content.id} to collection '{collection_name}'.")

def retrieve_similar_content_from_qdrant(client: QdrantClient, collection_name: str, query_embedding: List[float], limit: int = 3) -> List[dict]:
    """Retrieves content similar to the query embedding from Qdrant."""
    if not query_embedding:
        raise ValueError("Query embedding cannot be empty.")

    search_result = client.search(
        collection_name=collection_name,
        query_vector=query_embedding,
        limit=limit,
        with_payload=True # Retrieve the stored payload (including text_content)
    )

    results = []
    for hit in search_result:
        results.append({"id": hit.id, "score": hit.score, "payload": hit.payload})
    print(f"Retrieved {len(results)} similar content items from collection '{collection_name}'.")
    return results

