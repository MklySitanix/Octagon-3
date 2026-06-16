print("Hello, World!")
from db.crud import get_categories, get_books

cats = get_categories()
books = get_books()

print("CATEGORIES:")
for c in cats:
    print(c.id, c.title)

print("\nBOOKS:")
for b in books:
    print(b.title, b.price)