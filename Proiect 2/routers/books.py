import csv
from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from db import create_session
from models import BookModel, AuthorModel
from schemas import BookCreate, BookInfo

router = APIRouter(prefix="/books", tags=["books"])


@router.get('')
def get_books(db: Session = Depends(create_session)):
    books: List[BookModel] = db.query(BookModel).all()
    return [BookInfo(title=book.title, genre=book.genre, author_name=book.author.name, is_available=book.available())
            for book in books]


@router.get('/{title}')
def get_books_by_title(title: str, db: Session = Depends(create_session)):
    books: List[BookModel] = db.query(BookModel).filter(BookModel.title.ilike(f"%{title}%")).all()
    return [BookInfo(title=book.title, genre=book.genre, author_name=book.author.name, is_available=book.available())
            for book in books]


@router.post('/create')
def create_book(new_book: BookCreate, db: Session = Depends(create_session)):
    author: AuthorModel | None = db.query(AuthorModel).filter(AuthorModel.name == new_book.author_name).first()
    if author is not None:
        book = BookModel(title=new_book.title, genre=new_book.genre, author=author)
        db.add(book)
        db.commit()
        return {"status": "Success"}
    else:
        raise HTTPException(status_code=422, detail="No author with this name found")
