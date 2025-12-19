import pytest
from src.internal import Book, EBook


class TestBook:
    def test_book_init(self):
        book = Book("1984", "Оруэлл", 1949, "Антиутопия", 123456)
        assert book.title == "1984"
        assert book.author == "Оруэлл"
        assert book.year == 1949
        assert book.genre == "Антиутопия"
        assert book.isbn == 123456

    def test_book_str(self):
        book = Book("Преступление и наказание", "Достоевский", 1866, "Роман", 789012)
        assert str(book) == '"Преступление и наказание" by Достоевский (1866)'

    def test_book_repr(self):
        book = Book("Мастер и Маргарита", "Булгаков", 1967, "Роман", 345678)
        expected = "Book(Мастер и Маргарита, Булгаков, 1967, Роман, 345678)"
        assert repr(book) == expected

    def test_book_eq(self):
        book1 = Book("Книга", "Автор", 2000, "Жанр", 111111)
        book2 = Book("Другая книга", "Автор", 2000, "Жанр", 111111)
        book3 = Book("Книга", "Автор", 2000, "Жанр", 222222)
        assert book1 == book2
        assert book1 != book3
        assert book1 != "не книга"

    def test_book_hash(self):
        book1 = Book("Книга", "Автор", 2000, "Жанр", 111111)
        book2 = Book("Книга", "Автор", 2000, "Жанр", 111111)
        assert hash(book1) == hash(book2)


class TestEBook:
    def test_ebook_init(self):
        ebook = EBook("1984", "Оруэлл", 1949, "Антиутопия", 123456, 2, 328, "pdf")
        assert ebook.size == 2
        assert ebook.pages == 328
        assert ebook.file_ext == "pdf"
        assert ebook._how_much_read == 0

    def test_ebook_progress(self):
        ebook = EBook("Книга", "Автор", 2000, "Жанр", 111111, 1, 100, "epub")
        ebook.progress(50)
        assert ebook._how_much_read == 50

    def test_ebook_str_with_progress(self):
        ebook = EBook("Книга", "Автор", 2000, "Жанр", 111111, 1, 200, "pdf")
        ebook.progress(100)
        assert "50.0%" in str(ebook)

    def test_ebook_eq(self):
        ebook1 = EBook("Книга", "Автор", 2000, "Жанр", 111111, 1, 100, "pdf")
        ebook2 = EBook("Книга", "Автор", 2000, "Жанр", 111111, 1, 100, "pdf")
        ebook3 = EBook("Книга", "Автор", 2000, "Жанр", 111111, 2, 100, "epub")
        assert ebook1 == ebook2
        assert ebook1 != ebook3
        assert ebook1 != Book("Книга", "Автор", 2000, "Жанр", 111111)

    def test_ebook_parent(self):
        ebook = EBook("Книга", "Автор", 2000, "Жанр", 111111, 1, 100, "pdf")
        assert isinstance(ebook, Book)
        assert hasattr(ebook, 'title')
        assert hasattr(ebook, 'author')