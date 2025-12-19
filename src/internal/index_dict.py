from internal import Book

class IndexDict:
    def __init__(self) -> None:
        """Инициализация индексов"""
        self._isbn_index: dict[int, Book] = {}
        self._author_index: dict[str, list[Book]] = {}
        self._year_index: dict[int, list[Book]] = {}
        self._genre_index: dict[str, list[Book]] = {}

    def __getitem__(self, key: int | str) -> Book | list[Book]:
        """Получение книг по ключу (isbn, автор или год)"""
        if isinstance(key, int):
            if key in self._isbn_index:
                return self._isbn_index[key]
            elif key in self._year_index:
                return self._year_index[key]
            else:
                raise KeyError(f"{key} не найден")
        elif isinstance(key, str):
            if key in self._author_index:
                return self._author_index[key]
            elif key in self._genre_index:
                return self._genre_index[key]
            elif key in self._genre_index:
                return self._genre_index[key]
            else:
                raise KeyError(f'"{key}" не найден')
        else:
            raise TypeError(f"Ключ должен быть int или str")

    def __len__(self) -> int:
        """Количество уникальных книг по isbn"""
        return len(self._isbn_index)

    def __iter__(self):
        """Итерация по isbn книг"""
        return iter(self._isbn_index)

    def add_book(self, book: Book) -> bool:
        """Добавление книги в индексы, если уже есть среди isbn то возвращаем False"""
        if book._isbn in self._isbn_index:
            return False
        self._isbn_index[book._isbn] = book

        if book._author not in self._author_index:
            self._author_index[book._author] = []
        self._author_index[book._author].append(book)

        if book._year not in self._year_index:
            self._year_index[book._year] = []
        self._year_index[book._year].append(book)

        if book._genre not in self._genre_index:
            self._genre_index[book._genre] = []
        self._genre_index[book._genre].append(book)

        return True

    def remove_book(self, book: Book) -> bool:
        """Удаление книги из индексов, если ее нет среди isbn то возвращаем False"""
        if book._isbn not in self._isbn_index:
            return False

        del self._isbn_index[book._isbn]

        if book._author in self._author_index:
            author_books = self._author_index[book._author]
            author_books[:] = [b for b in author_books if b._isbn != book._isbn]
            if not author_books:
                del self._author_index[book._author]

        if book._year in self._year_index:
            year_books = self._year_index[book._year]
            year_books[:] = [b for b in year_books if b._isbn != book._isbn]
            if not year_books:
                del self._year_index[book._year]

        if book._genre in self._genre_index:
            genre_books = self._genre_index[book._genre]
            genre_books[:] = [b for b in genre_books if b._genre != book._genre]
            if not genre_books:
                del self._genre_index[book._genre]

        return True
