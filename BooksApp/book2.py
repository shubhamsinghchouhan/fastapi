from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status
app = FastAPI()

# BOOKS = []

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

# Pydantic
class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not needed on create', default=None)
    title: str = Field(min_length=3, max_length=100)
    author: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=3, max_length=1000)
    rating: int = Field(gt=0, lt=6)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A very nice book",
                "author": "A very nice book",
                "description": "A very nice book",
                "rating": 5,
            }
        }
    }
BOOKS = [
    Book(1, "Computer Science", "Coding with Shubham", "A very nice book", 5),
    Book(2, "Python", "Coding with Shubham", "A very nice book", 5),
    Book(3, "FastAPI", "Coding with Shubham", "A very nice book", 5),
    Book(4, "Ruby", "Coding with Shubham", "A very nice book", 2),
    Book(5, "Rails", "Coding with Shubham", "A very nice book", 3),
    Book(6, "Rails", "Coding with Shubham", "A very nice book", 1),
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books/new", status_code=status.HTTP_201_CREATED)
async def create_books(book_request: BookRequest):
    print(type(book_request))
    # new_book = Book(**book_request.dict())
    new_book = Book(**book_request.model_dump())
    print(type(new_book))
    BOOKS.append(find_book_id(new_book))

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    # BOOKS.remove(find_book_id(book_id))
    if book_changed == False:
        raise HTTPException(status_code=404, detail="Book not found")
    return None

@app.put("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not(book_changed):
        raise HTTPException(status_code=404, detail="Book not found")

    # new_book = Book(**book_request.model_dump())
    # BOOKS.append(find_book_id(new_book))
    # return None

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    #
    # return book
#
# @app.post("/create-book")
# async def create_books(book_request: BookRequest):
#     print(type(book_request))
#     BOOKS.append(book_request)

#
# @app.post("/create-book")
# async def create_books(book_request=Body()):
#     BOOKS.append(book_request)
