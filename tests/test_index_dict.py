import pytest
from src.internal import Book, IndexDict


class TestIndexDict:
    def test_indexdict_creation(self):
        index = IndexDict()
        assert len(index) == 0
        assert index.isbn_index == {}
        assert index.author_index == {}

    def test_add_book(self):
        index = IndexDict()
        book = Book("Книга", "Автор", 2000, "Жанр", 111111)

        result = index.add_book(book)
        assert result is True
        assert len(index) == 1
        assert index[111111] == book
        assert book in index["Автор"]
        assert book in index[2000]
        assert book in index["Жанр"]

    def test_add_repeated_book(self):
        index = IndexDict()
        book = Book("Книга", "Автор", 2000, "Жанр", 111111)

        index.add_book(book)
        result = index.add_book(book)
        assert result is False
        assert len(index) == 1

    def test_remove_book(self):
        index = IndexDict()
        book = Book("Книга", "Автор", 2000, "Жанр", 111111)

        index.add_book(book)
        result = index.remove_book(book)

        assert result is True
        assert len(index) == 0
        with pytest.raises(KeyError):
            _ = index[111111]

    def test_getitem_multiple(self):
        index = IndexDict()
        book1 = Book("Книга1", "Автор1", 2000, "Жанр1", 111111)
        book2 = Book("Книга2", "Автор1", 2001, "Жанр2", 222222)

        index.add_book(book1)
        index.add_book(book2)

        assert index[111111] == book1
        assert book1 in index["Автор1"]
        assert book2 in index["Автор1"]
        assert book1 in index[2000]
        assert book2 in index[2001]
        assert book1 in index["Жанр1"]
        assert book2 in index["Жанр2"]