from .books import Book

class BookCollection:
    def __init__(self, books: list[Book] = None) -> None:
        """Инициализация коллекции книг"""
        self._books = books.copy() if books else []

    def __getitem__(self, item: int | slice) -> "Book | BookCollection":
        """Получение по номеру айтема или слайсу"""
        if isinstance(item, slice):
            return BookCollection(self._books[item])
        else:
            return self._books[item]

    def __len__(self) -> int:
        """Получение количества книг"""
        return len(self._books)

    def __iter__(self):
        """Получение итератора"""
        return iter(self._books)

    def add(self, book: Book) -> None:
        """Добавляет книгу в коллекцию"""
        self._books.append(book)

    def remove(self, book: Book) -> None:
        """Удаляет книгу из коллекции"""
        if book in self._books:
            self._books.remove(book)