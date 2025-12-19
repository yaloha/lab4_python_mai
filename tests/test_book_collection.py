import pytest
from src.internal import Book, BookCollection


class TestBookCollection:
    def test_collection_init(self):
        books = [Book("Книга1", "Автор1", 2000, "Жанр1", 111111),
                 Book("Книга2", "Автор2", 2001, "Жанр2", 222222)]
        collection = BookCollection(books)
        assert len(collection) == 2

    def test_collection_add_remove(self):
        collection = BookCollection()
        book = Book("Книга", "Автор", 2000, "Жанр", 111111)

        collection.add(book)
        assert len(collection) == 1
        assert book in collection

        collection.remove(book)
        assert len(collection) == 0
        assert book not in collection

    def test_collection_getitem(self):
        books = [Book(f"Книга{i}", f"Автор{i}", 2000 + i, "Жанр", 100000 + i)
                 for i in range(5)]
        collection = BookCollection(books)

        assert collection[0] == books[0]
        assert collection[1:3] is not None
        assert isinstance(collection[1:3], BookCollection)
        assert len(collection[1:3]) == 2

    def test_collection_iter(self):
        books = [Book(f"Книга{i}", f"Автор{i}", 2000 + i, "Жанр", 100000 + i)
                 for i in range(3)]
        collection = BookCollection(books)

        iterated = [book for book in collection]
        assert iterated == books

    def test_empty_collection(self):
        collection = BookCollection()
        assert len(collection) == 0
        assert list(collection) == []