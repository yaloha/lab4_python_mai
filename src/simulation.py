import random

from internal.books import Book
from internal import Library, IndexDict
from constants import TITLES, AUTHORS, GENRES, YEARS, EVENTS


def generate_random_book() -> Book:
    """Генерирует случаюгую книгу из набора констант"""
    return Book(
        title=random.choice(TITLES),
        author=random.choice(AUTHORS),
        year=random.choice(YEARS),
        genre=random.choice(GENRES),
        isbn=random.randint(1000000, 10000000)
    )


def event_add_book(library: Library) -> None:
    """Ивент на добавление книги"""
    book = generate_random_book()
    result = library.add_book(book)
    print(f"Добавление {book} {'успешно' if result else f'{book} уже есть в Library'}")


def event_remove_book(library: Library) -> None:
    """Ивент на удаление книги"""
    if len(library) == 0:
        print("Библиотека пуста, удаление невозможно")
        return
    book = random.choice(library._books)
    library.remove_book(book)
    print(f"Удалена книга {book}")


def event_search_by_author(library: Library) -> None:
    """Ивент на поиск книг по автору"""
    author = random.choice(AUTHORS)
    result = library.search_by_author(author)
    print(f'Поиск по автору "{author}": найдено {len(result)} книг: {", ".join([str(book) for book in result])}')


def event_search_by_genre(library: Library) -> None:
    """Ивент на поиск книг по жанру"""
    genre = random.choice(GENRES)
    result = library.search_by_genre(genre)
    print(f'Поиск по жанру "{genre}": найдено {len(result)} книг: {", ".join([str(book) for book in result])}')


def event_search_by_year(library: Library) -> None:
    """Ивент на поиск книг по году"""
    year = random.choice(YEARS)
    result = library.search_by_year(year)
    print(f'Поиск по году "{year}": найдено {len(result)} книг: {", ".join([str(book) for book in result])}')


def event_get_nonex_isbn(library: Library) -> None:
    """Ивент на получение книги по несуществуюшему isbn"""
    fake_isbn = random.randint(10000000, 20000000)
    book = library.search_by_isbn(fake_isbn)
    print(f"Поиск по несуществующему isbn {fake_isbn}: {book}")


def event_update_indexes(library: Library) -> None:
    """Ивент на обновление всех индексов"""
    library.update_indexes()
    print("Индексы обновлены")


EVENT_NAMES_TO_FUNCTIONS = {
    "add book": event_add_book,
    "remove book": event_remove_book,
    "search author": event_search_by_author,
    "search genre": event_search_by_genre,
    "search year": event_search_by_year,
    "get nonexistent book": event_get_nonex_isbn,
    "update indexes": event_update_indexes
}


def run_simulation(steps: int = 20, seed: int = None) -> None:
    """Основная функция запускающая симуляцию"""
    if seed is not None:
        random.seed(seed)
    library = Library()
    print("Simulation start")
    for step in range(steps):
        event = random.choice(EVENTS)
        print(f"step {step + 1}: event = {event}\n")

        EVENT_NAMES_TO_FUNCTIONS[event](library)
        print(f"library after event: {library}\n")






