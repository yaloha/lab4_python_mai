import pytest
from src.internal import Book, Library, EBook


class TestLibrary:
    def test_library_init(self):
        library = Library()
        assert len(library) == 0
        assert repr(library) == "books=0, indexed=0"

    def test_add_book_to_lib(self):
        library = Library()
        book = Book("Книга", "Автор", 2000, "Жанр", 111111)

        result = library.add_book(book)
        assert result is True
        assert len(library) == 1
        assert book in library
        assert repr(library) == "books=1, indexed=1"

    def test_remove_book_from_lib(self):
        library = Library()
        book = Book("Книга", "Автор", 2000, "Жанр", 111111)

        library.add_book(book)
        result = library.remove_book(book)

        assert result is True
        assert len(library) == 0
        assert book not in library

    def test_search_funcs(self):
        library = Library()
        book1 = Book("Книга1", "Автор1", 2000, "Фантастика", 111111)
        book2 = Book("Книга2", "Автор1", 2001, "Драма", 222222)
        book3 = Book("Книга3", "Автор2", 2000, "Фантастика", 333333)
        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)

        author_results = library.search_by_author("Автор1")
        assert len(author_results) == 2

        year_results = library.search_by_year(2000)
        assert len(year_results) == 2

        genre_results = library.search_by_genre("Фантастика")
        assert len(genre_results) == 2

        isbn_result = library.search_by_isbn(111111)
        assert isbn_result == book1

        non_existent = library.search_by_isbn(999999)
        assert non_existent is None

    def test_lib_plus_operator(self):
        library = Library()
        book = Book("Книга", "Автор", 2000, "Жанр", 111111)
        result = library + book
        assert isinstance(result, Library)
        assert book in library
        assert len(library) == 1

    def test_update_indexes(self):
        library = Library()
        book = Book("Книга", "Автор", 2000, "Жанр", 111111)
        library._books.add(book)
        assert repr(library) == "books=1, indexed=0"
        library.update_indexes()
        assert repr(library) == "books=1, indexed=1"
        assert book in library.search_by_author("Автор")


    def test_add_ebook_to_lib(self):
        library = Library()
        ebook = EBook("1984", "Оруэлл", 1949, "Антиутопия", 123456, 2, 123, "pdf")

        result = library.add_book(ebook)
        assert result is True
        assert len(library) == 1
        assert ebook in library
        assert repr(library) == "books=1, indexed=1"

    def test_search_ebook_by_author(self):
        library = Library()
        ebook1 = EBook("Книга1", "Автор1", 2000, "Жанр1", 111111, 1, 200, "epub")
        ebook2 = EBook("Книга2", "Автор1", 2001, "Жанр2", 222222, 2, 300, "pdf")
        book3 = Book("Книга3", "Автор2", 2000, "Жанр3", 333333)

        library.add_book(ebook1)
        library.add_book(ebook2)
        library.add_book(book3)

        author_results = library.search_by_author("Автор1")
        assert len(author_results) == 2
        assert all(isinstance(b, EBook) for b in author_results)