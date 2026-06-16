# Octagon Books API

REST API для управления книгами и категориями. Построен на FastAPI + SQLAlchemy + PostgreSQL.

## Запуск

1. Установить зависимости:
pip install -r requirements.txt
2. Создать `.env` файл (или использовать существующий):
3. 
DB_HOST=localhost

DB_PORT=5432

DB_NAME=octagon_db

DB_USER=octagon

DB_PASSWORD=12345

5. Запустить сервер:
uvicorn app.main:app --reload
6. Открыть документацию: http://127.0.0.1:8000/docs

## Эндпоинты

- `GET /health` — проверка работы сервера
- `GET/POST /categories` — список категорий / создать категорию
- `GET/PUT/DELETE /categories/{id}` — получить / обновить / удалить категорию
- `GET/POST /books` — список книг (фильтр: `?category_id=`) / создать книгу
- `GET/PUT/DELETE /books/{id}` — получить / обновить / удалить книгу
