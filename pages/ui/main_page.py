from selene import have, by, browser
import allure


class WikiMainPage:
    def open_page(self, page=""):
        with allure.step("Open the main page"):
            browser.open(page)

    def login(self, login, password):
        with allure.step("Sign in"):
            browser.element("#pt-login-2").should(have.text("Log in")).click()
            browser.element("#wpName1").type(login)
            browser.element("#wpPassword1").type(password)
            browser.element("#wpLoginAttempt").click()

    def logout(self):
        with allure.step("Sign off"):
            browser.element("#vector-user-links-dropdown-checkbox").click()
            browser.element("#pt-logout").click()

    def search(self, search_string):
        with allure.step("Search of the article"):
            browser.element("#p-search").click()
            browser.element(".cdx-text-input__input").type(search_string).submit()

    def open_link(self, name):
        with allure.step("Open link by name"):
            browser.element(by.text(name)).click()

    def check_not_found(self):
        with allure.step("Check if link not found"):
            browser.element(".mw-search-createlink").should(have.text("does not exist"))

    def change_language(self, lang="ru"):
        with allure.step("Change the language"):
            browser.element("#p-lang-btn-checkbox").click()
            browser.element(".interwiki-" + lang).click()

    def use_tool(self, tool):
        selectors = dict(upload="#t-upload", info="#t-info", permalink="#t-permalink", short_url="#t-urlshortener")
        with allure.step("Use the " + tool + " tool"):
            browser.element("#vector-page-tools-dropdown-checkbox").click()
            browser.element(selectors[tool]).click()

    def check_logged_user(self, name):
        with allure.step("Check if signed in"):
            browser.element("#pt-userpage-2").should(have.text(name))

    def check_logged_out(self):
        with allure.step("Check if not signed in"):
            browser.element("#pt-createaccount-2").should(have.text("Create account"))

    def check_auth_error(self):
        with allure.step("Check if the incorrect login error was risen"):
            browser.element(".mw-message-box-error").should(have.text("Incorrect username or password entered"))

    def check_article_header(self, header):
        with allure.step("Check the article name"):
            browser.element("#firstHeading").should(have.text(header))

    def check_short_url_created(self):
        with allure.step("Check if short url was created"):
            browser.element("#ooui-2").should(have.value_containing("https://w.wiki"))
            browser.element("#ooui-1").should(have.text("https://w.wiki/_dAw"))


page = WikiMainPage()
