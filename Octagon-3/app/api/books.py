from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from app.db.db import get_db
from app.db import crud
from app.schemas import BookCreate, BookUpdate, BookResponse

router = APIRouter()


@router.get("/", response_model=list[BookResponse])
def list_books(category_id: Optional[int] = None, db: Session = Depends(get_db)):
    return crud.get_books(db, category_id)


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    obj = crud.get_book(db, book_id)
    if obj is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return obj


@router.post("/", response_model=BookResponse, status_code=201)
def create_book(data: BookCreate, db: Session = Depends(get_db)):
    category = crud.get_category(db, data.category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return crud.create_book(db, data.title, data.description, data.price, data.url, data.category_id)


@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, data: BookUpdate, db: Session = Depends(get_db)):
    category = crud.get_category(db, data.category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    obj = crud.update_book(db, book_id, data.title, data.description, data.price, data.url, data.category_id)
    if obj is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return obj


@router.delete("/{book_id}", response_model=BookResponse)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_book(db, book_id)
    if obj is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return obj