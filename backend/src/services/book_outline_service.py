
from typing import List, Optional
from backend.src.models.book import BookOutline

class BookOutlineService:
    def __init__(self):
        self.outlines: List[BookOutline] = []
        self._next_id = 1

    def create_outline(self, title: str, description: str, parent_id: Optional[int] = None) -> BookOutline:
        new_outline = BookOutline(id=self._next_id, title=title, description=description, order=len(self.outlines), parent_id=parent_id)
        self.outlines.append(new_outline)
        self._next_id += 1
        return new_outline

    def get_outline_by_id(self, outline_id: int) -> Optional[BookOutline]:
        return next((o for o in self.outlines if o.id == outline_id), None)

    def get_all_outlines(self) -> List[BookOutline]:
        return sorted(self.outlines, key=lambda o: o.order)

    def update_outline(self, outline_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[BookOutline]:
        outline = self.get_outline_by_id(outline_id)
        if outline:
            if title is not None:
                outline.title = title
            if description is not None:
                outline.description = description
            return outline
        return None

    def delete_outline(self, outline_id: int) -> bool:
        initial_len = len(self.outlines)
        self.outlines = [o for o in self.outlines if o.id != outline_id]
        return len(self.outlines) < initial_len
