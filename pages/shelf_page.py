from selene.support.shared import browser
from selene import have, by
from pages.books_page import BooksPage


class ShelfPage:
    def open_shelf_page(self):
        books_page = BooksPage()
        books_page.open_books_page()
        browser.element(by.text("Мои полки")).click()

    def create_shelf(self, name, description):
        browser.element(by.text("Создать полку")).click()
        browser.element("input[id=name]").type(name)
        browser.element("textarea[id=description]").type(description)
        browser.element("button.ant-btn-primary").should(have.text("Сохранить")).click()

    def remove_shelf(self, name):
        browser.element(by.text(name)).click()
        browser.element(by.text("Изменить")).click()
        browser.element(by.text("Удалить полку")).click()
        browser.element(".ant-modal-footer button.ant-btn-primary").should(have.text("Удалить полку")).click()
