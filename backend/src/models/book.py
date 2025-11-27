from pydantic import BaseModel, Field
from typing import List, Optional

class ChapterOutline(BaseModel):
    title: str = Field(..., description="Title of the chapter")
    sections: List[str] = Field(default_factory=list, description="List of section titles within the chapter")

class BookOutline(BaseModel):
    title: str = Field(..., description="Title of the book")
    chapters: List[ChapterOutline] = Field(default_factory=list, description="List of chapter outlines for the book")

class BookContent(BaseModel):
    chapter_title: str = Field(..., description="Title of the chapter")
    section_title: Optional[str] = Field(None, description="Title of the section, if applicable")
    content: str = Field(..., description="Markdown content of the chapter or section")
    word_count: int = Field(0, description="Word count of the generated content")
    token_count: int = Field(0, description="Token count of the generated content")
    model_info: str = Field(..., description="Information about the AI model used for generation")
    timestamp: str = Field(..., description="ISO format timestamp of content generation")
