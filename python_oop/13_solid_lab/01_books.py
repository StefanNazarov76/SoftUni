from typing import List


class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self.page: int = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def find_book(self, title: str) -> Book:
        for book in self.books:
            if book.title == title:
                return book
