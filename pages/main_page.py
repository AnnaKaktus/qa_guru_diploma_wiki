from selene.support.shared import browser
from selene import have, by
import allure


class WikiMainPage:
    def open_page(self, page=""):
        with allure.step("Открываем главную страницу"):
            browser.open(page)

    def login(self, login, password):
        with allure.step("Логин"):
            browser.element("#pt-login-2").should(have.text("Log in")).click()
            browser.element("#wpName1").type(login)
            browser.element("#wpPassword1").type(password)
            browser.element("#wpLoginAttempt").click()

    def logout(self):
        with allure.step("Логаут"):
            browser.element("#vector-user-links-dropdown-checkbox").click()
            browser.element("#pt-logout").click()

    def search(self, search_string):
        with allure.step("Поиск"):
            browser.element("#p-search").click()
            browser.element(".cdx-text-input__input").type(search_string).submit()

    def use_tool(self, tool):
        selectors = dict(upload="#t-upload", info="#t-info", permalink="#t-permalink", short_url="#t-urlshortener")
        with allure.step("Использование инструмента"):
            browser.element("#vector-page-tools-dropdown-checkbox").click()
            browser.element(selectors[tool]).click()


page = WikiMainPage()
