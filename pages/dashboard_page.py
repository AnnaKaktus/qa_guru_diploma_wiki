from selene.support.shared import browser
from selene import have, by
from time import sleep


class DashboardPage:
    def open_page(self):
        browser.open("https://mybook.ru/dashboard/")

    def login(self, login, password):
        browser.element(".ant-col-xs-0 .cy-login-button").should(have.text("Войти")).click()
        browser.element(".cy-login-email-input").type(login)
        browser.element("[type=\"password\"]").type(password)
        sleep(1)
        browser.element(".cy-login-submit-button").click()

    def logout(self):
        browser.element(".ant-col-xs-0 .cy-user-header-avatar").click()
        browser.element(by.text("Выйти")).click()
        sleep(1)

    def search_book(self, search):
        browser.element("[placeholder=\"Книга или автор\"]").type(search)

    def open_book_page(self, title):
        browser.element(by.text(title)).click()
