
from fastapi import APIRouter, HTTPException, status
from typing import List, Optional

from backend.src.models.book import BookOutline, BookContent
from backend.src.services.book_outline_service import BookOutlineService
from backend.src.services.content_generation_service import ContentGenerationService

router = APIRouter()

# Initialize services (in a real app, these would be dependency injected)
book_outline_service = BookOutlineService()
content_generation_service = ContentGenerationService()

@router.post("/outlines", response_model=BookOutline, status_code=status.HTTP_201_CREATED)
async def create_book_outline(title: str, description: str, parent_id: Optional[int] = None):
    """Create a new book outline entry."""
    outline = book_outline_service.create_outline(title, description, parent_id)
    return outline

@router.get("/outlines", response_model=List[BookOutline])
async def get_all_book_outlines():
    """Retrieve all book outlines."""
    return book_outline_service.get_all_outlines()

@router.get("/outlines/{outline_id}", response_model=BookOutline)
async def get_book_outline(outline_id: int):
    """Retrieve a specific book outline by ID."""
    outline = book_outline_service.get_outline_by_id(outline_id)
    if not outline:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Outline not found")
    return outline

@router.put("/outlines/{outline_id}", response_model=BookOutline)
async def update_book_outline(outline_id: int, title: Optional[str] = None, description: Optional[str] = None):
    """Update an existing book outline by ID."""
    updated_outline = book_outline_service.update_outline(outline_id, title, description)
    if not updated_outline:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Outline not found")
    return updated_outline

@router.delete("/outlines/{outline_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_outline(outline_id: int):
    """Delete a book outline by ID."""
    if not book_outline_service.delete_outline(outline_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Outline not found")

@router.post("/generate-content/{outline_id}", response_model=BookContent, status_code=status.HTTP_202_ACCEPTED)
async def generate_book_content_for_outline(outline_id: int):
    """Trigger AI content generation for a specific book outline."""
    outline = book_outline_service.get_outline_by_id(outline_id)
    if not outline:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Outline not found")

    # In a real application, this might trigger an asynchronous task
    generated_content = await content_generation_service.generate_content(outline)
    # Logic to store this generated_content (T014) would go here or be handled by content_generation_service
    return generated_content

@router.post("/generate-introduction", response_model=BookContent, status_code=status.HTTP_202_ACCEPTED)
async def generate_book_introduction_endpoint():
    """Trigger AI content generation for the book introduction."""
    generated_intro = await content_generation_service.generate_book_introduction()
    return generated_intro
