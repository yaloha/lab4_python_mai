class Book:
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: int) -> None:
        """Инициализация книги"""
        self._title = title
        self._author = author
        self._year = year
        self._genre = genre
        self._isbn = isbn

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def year(self) -> int:
        return self._year

    @property
    def genre(self) -> str:
        return self._genre

    @property
    def isbn(self) -> int:
        return self._isbn

    def __str__(self) -> str:
        """Возвращение строки с информацией об книге"""
        return f'"{self._title}" by {self._author} ({self._year})'

    def __hash__(self) -> hash:
        """Хэширование книг"""
        return hash(str(self))

    def __repr__(self) -> str:
        """Подробная информация об книге"""
        return f'Book({self._title}, {self._author}, {self._year}, {self._genre}, {self._isbn})'

    def __eq__(self, other: "Book") -> bool:
        """Сравнение книг"""
        if not isinstance(other, Book):
            return False
        return self._isbn == other._isbn


class EBook(Book):
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: int, size: int, pages: int, file_ext: str) -> None:
        """Инициализация электронной книги"""
        super().__init__(title, author, year, genre, isbn)
        self._size = size
        self._pages = pages
        self._file_ext = file_ext
        self._how_much_read = 0

    @property
    def size(self) -> int:
        return self._size

    @property
    def pages(self) -> int:
        return self._pages

    @property
    def file_ext(self) -> int:
        return self._file_ext

    @property
    def how_much_read(self) -> int:
        return self._how_much_read

    def progress(self, read_pages: int) -> None:
        """Обновление количества прочитанных страниц"""
        self._how_much_read += read_pages

    def __str__(self) -> str:
        """Возвращение строки с информацией об электронной книге"""
        book_str = super().__str__()
        return f"{book_str} [E, {self._file_ext}, {self._size}MB, " \
               f"{self._how_much_read / self._pages * 100}% of book is read through]"
    
    def __eq__(self, other) -> bool:
        """Сравнение электронных книг"""
        if not isinstance(other, EBook):
            return False

        book_equal = super().__eq__(other)
        ebook_equal = (self._size == other._size and
                       self._pages == other._pages and
                       self._file_ext == other._file_ext)

        return book_equal and ebook_equal

    def __hash__(self):
        """Хэширование электронных книг"""
        return hash(str(self))
    


