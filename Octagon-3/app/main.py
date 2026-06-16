from fastapi import FastAPI
from app.api import books, categories

app = FastAPI(title="Octagon Books API")

app.include_router(categories.router, prefix="/categories", tags=["Categories"])
app.include_router(books.router, prefix="/books", tags=["Books"])

@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}