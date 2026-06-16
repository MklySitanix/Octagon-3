from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db import crud
from app.schemas import CategoryCreate, CategoryUpdate, CategoryResponse

router = APIRouter()


@router.get("/", response_model=list[CategoryResponse])
def list_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    obj = crud.get_category(db, category_id)
    if obj is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return obj


@router.post("/", response_model=CategoryResponse, status_code=201)
def create_category(data: CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, data.title)


@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int, data: CategoryUpdate, db: Session = Depends(get_db)):
    obj = crud.update_category(db, category_id, data.title)
    if obj is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return obj


@router.delete("/{category_id}", response_model=CategoryResponse)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    obj = crud.delete_category(db, category_id)
    if obj is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return obj