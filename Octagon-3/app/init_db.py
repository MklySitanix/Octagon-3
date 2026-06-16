from db.db import engine
from db.models import Base
from db.crud import create_category, create_book

print(">>> INIT_DB STARTED")
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

print(">>> DB RESET DONE")

cat1 = create_category("Programming")
cat2 = create_category("Design")

create_book("Python Basics", "...", 1000, "", cat1.id)
create_book("Advanced Python", "...", 1500, "", cat1.id)

create_book("UI Design", "...", 900, "", cat2.id)
create_book("Figma Guide", "...", 1200, "", cat2.id)

print("Database initialized")