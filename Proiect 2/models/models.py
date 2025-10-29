from datetime import date, datetime
from typing import List

from sqlalchemy import Date, Integer, String, ForeignKey, Boolean, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, relationship


def safe_get(dct, *keys):
    for key in keys:
        try:
            dct = dct[key]
        except (KeyError, IndexError):
            return None
    return dct


Base = declarative_base()


class UserModel(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(64), unique=True, nullable=True, default=None)
    hashed_password: Mapped[str] = mapped_column(String(64), nullable=False)
    loans: Mapped[List["LoanModel"]] = relationship("LoanModel", back_populates="user")

    def __repr__(self) -> str:
        return f"User(username - {self.username})"


class AuthorModel(Base):
    __tablename__ = "author"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    birth_date: Mapped[date] = mapped_column(Date, nullable=False)
    death_date: Mapped[date] = mapped_column(Date, nullable=True, default=None)
    books: Mapped[List["BookModel"]] = relationship("BookModel", back_populates="author")

    def __repr__(self) -> str:
        return f"Author(name - {self.name}, birth_date - {self.birth_date}, books_count - {len(self.books)})"


class BookModel(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    genre: Mapped[str] = mapped_column(String(32), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"), nullable=False)
    author: Mapped["AuthorModel"] = relationship("AuthorModel", back_populates="books")
    loans: Mapped[List["LoanModel"]] = relationship("LoanModel", back_populates="book")

    def available(self) -> bool:
        return not any(loan.is_active for loan in self.loans)

    def __repr__(self) -> str:
        return f"Book(title - {self.title}, author_name - {self.author.name}, available - {self.available()})"


class LoanModel(Base):
    __tablename__ = "loan"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("book.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    start_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, default=datetime.now())
    stop_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    book: Mapped["BookModel"] = relationship("BookModel", back_populates="loans")
    user: Mapped["UserModel"] = relationship("UserModel", back_populates="loans")

    def __repr__(self) -> str:
        return f"Loan(book_title - {self.book.id}, username - {self.user.username}, is_active - {self.is_active})"
