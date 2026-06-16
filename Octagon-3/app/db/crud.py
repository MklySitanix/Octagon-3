from sqlalchemy.orm import Session
from .models import Category, Book

def get_categories(db: Session):
    return db.query(Category).all()

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def create_category(db: Session, title: str):
    obj = Category(title=title)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_category(db: Session, category_id: int, title: str):
    obj = db.query(Category).filter(Category.id == category_id).first()
    if obj is None:
        return None
    obj.title = title
    db.commit()
    db.refresh(obj)
    return obj

def delete_category(db: Session, category_id: int):
    obj = db.query(Category).filter(Category.id == category_id).first()
    if obj is None:
        return None
    db.delete(obj)
    db.commit()
    return obj

def get_books(db: Session, category_id: int = None):
    query = db.query(Book)
    if category_id is not None:
        query = query.filter(Book.category_id == category_id)
    return query.all()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, title: str, description: str, price: int, url: str, category_id: int):
    obj = Book(title=title, description=description, price=price, url=url, category_id=category_id)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_book(db: Session, book_id: int, title: str, description: str, price: int, url: str, category_id: int):
    obj = db.query(Book).filter(Book.id == book_id).first()
    if obj is None:
        return None
    obj.title = title
    obj.description = description
    obj.price = price
    obj.url = url
    obj.category_id = category_id
    db.commit()
    db.refresh(obj)
    return obj

def delete_book(db: Session, book_id: int):
    obj = db.query(Book).filter(Book.id == book_id).first()
    if obj is None:
        return None
    db.delete(obj)
    db.commit()
    return obj