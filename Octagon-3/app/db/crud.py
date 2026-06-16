from .models import Category, Book
from .db import SessionLocal


def create_category(title):
    session = SessionLocal()
    obj = Category(title=title)
    session.add(obj)
    session.commit()
    session.refresh(obj)   
    session.close()
    return obj


def create_book(title, description, price, url, category_id):
    session = SessionLocal()
    obj = Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id
    )
    session.add(obj)
    session.commit()
    session.refresh(obj)
    session.close()
    return obj


def get_categories():
    session = SessionLocal()
    data = session.query(Category).all()
    session.close()
    return data


def get_books():
    session = SessionLocal()
    data = session.query(Book).all()
    session.close()
    return data