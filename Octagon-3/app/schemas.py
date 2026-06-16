from pydantic import BaseModel
from typing import Optional



class CategoryBase(BaseModel):
    title: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

    model_config = {"from_attributes": True}



class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: Optional[int] = None
    url: Optional[str] = None
    category_id: Optional[int] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookResponse(BookBase):
    id: int

    model_config = {"from_attributes": True}