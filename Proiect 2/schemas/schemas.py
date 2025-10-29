from datetime import date
from typing import Optional

from pydantic import BaseModel


class UserLogin(BaseModel):
    username: str
    password: str


class UserRegister(UserLogin):
    email: Optional[str] = None


class AuthorCreate(BaseModel):
    name: str
    birth_date: date
    death_date: Optional[date] = None


class AuthorInfo(AuthorCreate):
    books_count: int


class BookCreate(BaseModel):
    title: str
    genre: str
    author_name: str


class BookInfo(BookCreate):
    is_available: bool


class BookStat(BaseModel):
    title: str
    loan_count: int
