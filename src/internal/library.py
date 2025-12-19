from internal import Book, IndexDict, BookCollection
class Library:
    def __init__(self) -> None:
        """Инициализация библиотеки с коллекцией книг и индексами"""
        self._books = BookCollection()
        self._indexes = IndexDict()

    def __len__(self) -> int:
        """Количество книг"""
        return len(self._books)

    def __contains__(self, book: Book) -> bool:
        """Проверка наличия книги в библиотеке"""
        return book in self._books

    def __repr__(self) -> str:
        """Выводит количество книг и проиндексированных книг"""
        return f"books={len(self._books)}, indexed={len(self._indexes)}"

    def add_book(self, book: Book) -> bool:
        """Добавление книги в библиотеку (false сли уже есть)"""
        if book in self._books:
            return False

        self._books.add(book)
        return self._indexes.add_book(book)

    def remove_book(self, book: Book) -> bool:
        """Удаление книги из библиотеки (false если уже есть)"""
        if book not in self._books:
            return False

        self._books.remove(book)
        return self._indexes.remove_book(book)

    def search_by_author(self, author: str) -> BookCollection:
        """Поиск книг по автору"""
        try:
            books = self._indexes[author]
            return BookCollection(books if isinstance(books, list) else [])
        except KeyError:
            return BookCollection()

    def search_by_year(self, year: int) -> BookCollection:
        """Поиск книг по году"""
        try:
            books = self._indexes[year]
            return BookCollection(books if isinstance(books, list) else [])
        except KeyError:
            return BookCollection()

    def search_by_isbn(self, isbn: int) -> Book | None:
        """Поиск книги по isbn"""
        try:
            return self._indexes[isbn]
        except KeyError:
            return None

    def search_by_genre(self, genre: str) -> BookCollection:
        """Поиск книг по жанру"""
        try:
            books = self._indexes[genre]
            return BookCollection(books if isinstance(books, list) else [])
        except KeyError:
            return BookCollection()

    def __add__(self, book: Book) -> 'Library':
        """Реализация добавления книги через +"""
        self.add_book(book)
        return self

    def update_indexes(self) -> None:
        self._indexes = IndexDict()
        for book in self._books:
            self._indexes.add_book(book)