from src.internal import Book


class IndexDict:
    def __init__(self) -> None:
        """Инициализация индексов"""
        self.isbn_index: dict[int, Book] = {}
        self.author_index: dict[str, list[Book]] = {}
        self.year_index: dict[int, list[Book]] = {}
        self.genre_index: dict[str, list[Book]] = {}

    def __getitem__(self, key: int | str) -> Book | list[Book]:
        """Получение книг по ключу (isbn, автор или год)"""
        if isinstance(key, int):
            if key in self.isbn_index:
                return self.isbn_index[key]
            elif key in self.year_index:
                return self.year_index[key]
            else:
                raise KeyError(f"{key} не найден")
        elif isinstance(key, str):
            if key in self.author_index:
                return self.author_index[key]
            elif key in self.genre_index:
                return self.genre_index[key]
            elif key in self.genre_index:
                return self.genre_index[key]
            else:
                raise KeyError(f'"{key}" не найден')
        else:
            raise TypeError(f"Ключ должен быть int или str")

    def __len__(self) -> int:
        """Количество уникальных книг по isbn"""
        return len(self.isbn_index)

    def __iter__(self):
        """Итерация по isbn книг"""
        return iter(self.isbn_index)

    def add_book(self, book: Book) -> bool:
        """Добавление книги в индексы, если уже есть среди isbn то возвращаем False"""
        if book.isbn in self.isbn_index:
            return False
        self.isbn_index[book.isbn] = book

        if book.author not in self.author_index:
            self.author_index[book.author] = []
        self.author_index[book.author].append(book)

        if book.year not in self.year_index:
            self.year_index[book.year] = []
        self.year_index[book.year].append(book)

        if book.genre not in self.genre_index:
            self.genre_index[book.genre] = []
        self.genre_index[book.genre].append(book)

        return True

    def remove_book(self, book: Book) -> bool:
        """Удаление книги из индексов, если ее нет среди isbn то возвращаем False"""
        if book.isbn not in self.isbn_index:
            return False

        del self.isbn_index[book.isbn]

        if book.author in self.author_index:
            author_books = self.author_index[book.author]
            author_books[:] = [b for b in author_books if b.isbn != book.isbn]
            if not author_books:
                del self.author_index[book.author]

        if book.year in self.year_index:
            year_books = self.year_index[book.year]
            year_books[:] = [b for b in year_books if b.isbn != book.isbn]
            if not year_books:
                del self.year_index[book.year]

        if book.genre in self.genre_index:
            genre_books = self.genre_index[book.genre]
            genre_books[:] = [b for b in genre_books if b.genre != book.genre]
            if not genre_books:
                del self.genre_index[book.genre]

        return True
