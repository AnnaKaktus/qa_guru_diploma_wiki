from selene.support.shared import browser
from selene import by
import allure

from pages.dashboard_page import DashboardPage
from pages.books_page import BooksPage


def test_search_by_author():
    dashboard_page = DashboardPage()
    books_page = BooksPage()

    with allure.step("Вводим в поле поиска имя автора"):
        dashboard_page.open_page()
        dashboard_page.search_book("Ленин")
        books_page.open_book_page("Государство и революция")


def test_search_by_name():
    dashboard_page = DashboardPage()

    with allure.step("Вводим в поле поиска название книги"):
        dashboard_page.open_page()
        dashboard_page.search_book("Государство и революция")
        browser.element(by.text("Владимир Ленин")).click()
