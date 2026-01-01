from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()
# Note: Fast api check top to bottom
# behind the scenes, this is running
# uvicorn books:app --reload
# new version
# fastapi run books.py
# fastapi dev books.py

BOOKS = [
    {
        "id": "1",
        "title": "Book 1",
        "author": "Author 1",
        "publisher": "Publisher 1",
        "category": "Physics",
    },
    {
        "id": "2",
        "title": "Book 2",
        "author": "Author 2",
        "publisher": "Publisher 2",
        "category": "Chemistry",
    },
    {
        "id": "3",
        "title": "Algebra",
        "author": "Author 1",
        "publisher": "Publisher 1",
        "category": "Maths",
    },
    {
        "id": "4",
        "title": "Trignometry",
        "author": "Author 1",
        "publisher": "Publisher 1",
        "category": "Maths",
    }
]
@app.get("/books")
async def read_all_books():
    return BOOKS

# Path parameters
# # x /books/books_one
# @app.get("/books/dynamic_books/{dynamic_param}")
# async def read_all_books(dynamic_param):
#     return {'dynamic_param': BOOKS[0]}

@app.get("/books/{category}")
async def read_books(category: str):
    for book in BOOKS:
        if book["category"].casefold() == category.casefold():
            return book
    return None

# Query parameters
@app.get("/books/{book_id}/")
async def read_book_category_by_query(book_id: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("id") == int(book_id) and book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# GET CANNOT HAVE BODY
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def create_book(existing_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("id") == existing_book.get("id"):
            BOOKS[i] = existing_book


@app.delete("/books/delete_book/{book_id}")
async def delete_book(book_id: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("id") == book_id:
            BOOKS.pop(i)