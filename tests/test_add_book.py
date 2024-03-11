import allure
import os

from pages.dashboard_page import DashboardPage
from pages.books_page import BooksPage
from pages.book_page import BookPage


def test_add_book_to_my_books():
    dashboard_page = DashboardPage()
    books_page = BooksPage()
    book_page = BookPage()

    author = "Ленин"
    name = "Государство и революция"

    with allure.step("Авторизации перед добавлением книги"):
        dashboard_page.open_page()
        dashboard_page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_VALID"))
    with allure.step("Добавление книги"):
        dashboard_page.search_book(author)
        books_page.open_book_page(name)
        book_page.add_book()
        books_page.open_books_page()
        # если можно открыть страницу книги, значит, она была добавлена
        books_page.open_book_page(name)
    with allure.step("Удаление книги после добавления"):
        book_page.remove_book()
