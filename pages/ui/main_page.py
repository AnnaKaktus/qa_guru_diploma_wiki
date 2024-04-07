from selene import have, by, browser
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

    def open_link(self, name):
        browser.element(by.text(name)).click()

    def check_not_found(self):
        browser.element(".mw-search-createlink").should(have.text("does not exist"))

    def change_language(self, lang="ru"):
        browser.element("#p-lang-btn-checkbox").click()
        browser.element(".interwiki-" + lang).click()

    def use_tool(self, tool):
        selectors = dict(upload="#t-upload", info="#t-info", permalink="#t-permalink", short_url="#t-urlshortener")
        with allure.step("Использование инструмента"):
            browser.element("#vector-page-tools-dropdown-checkbox").click()
            browser.element(selectors[tool]).click()

    def check_logged_user(self, name):
        with allure.step("Проверка логина"):
            browser.element("#pt-userpage-2").should(have.text(name))

    def check_logged_out(self):
        with allure.step("Проверка отсутствия логина"):
            browser.element("#pt-createaccount-2").should(have.text("Create account"))

    def check_auth_error(self):
        with allure.step("Проверка ошибки входа"):
            browser.element(".mw-message-box-error").should(have.text("Incorrect username or password entered"))

    def check_article_header(self, header):
        with allure.step("Проверка названия статьи"):
            browser.element("#firstHeading").should(have.text(header))

    def check_short_url_created(self):
        with allure.step("Проверка создания short url"):
            browser.element("#ooui-2").should(have.value_containing("https://w.wiki"))
            browser.element("#ooui-1").should(have.text("https://w.wiki/_dAw"))


page = WikiMainPage()
