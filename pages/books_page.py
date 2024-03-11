from selene.support.shared import browser
from selene import by


class BooksPage:
    def open_books_page(self):
        browser.element(by.text("Мои книги")).click()

    def open_book_page(self, name):
        browser.element(by.text(name)).click()
