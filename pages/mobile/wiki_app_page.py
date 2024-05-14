from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class WikiAppPage:

    def skip_onboarding(self):
        with step("Пропустить необязательный шаг"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()

    def check_login(self, login):
        with step("Проверка логина"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/menu_icon")).click()
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/main_drawer_account_name")).should(have.text(login))

    def login(self, login, password):
        with step("Авторизация"):
            self.skip_onboarding()
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/menu_icon")).click()
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/main_drawer_login_button")).click()
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/create_account_login_button")).click()
            browser.element((AppiumBy.XPATH, "//android.widget.EditText[@text=\"Username\"]")).type(login)
            browser.element((AppiumBy.XPATH, "//android.widget.EditText[@text=\"Password\"]")).type(password)
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/login_button")).click()
            browser.element((AppiumBy.ID, "android:id/button2")).click()

    def logout(self):
        with step("Логаут"):
            browser.element((AppiumBy.XPATH, "//android.widget.TextView[@text=\"Settings\"]")).click()
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/logoutButton")).click()
            browser.element((AppiumBy.ID, "android:id/button1")).click()

    def search(self, search_text=""):
        with step("Поиск статьи"):
            self.skip_onboarding()
            browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(
                have.text("Search Wikipedia")).click()
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(search_text)

    def check_first_header(self, header=""):
        with step("Check article header"):
            results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
            results.should(have.size_greater_than(0))
            results.first.should(have.text(header))

    def search_and_open(self, article_name=""):
        with step("Search and open article"):
            self.search(article_name)
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")).click()

    def check_no_results(self):
        with step("Check no results message"):
            results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/results_text"))
            results.should(have.size_greater_than(0))
            results.first.should(have.text("No results"))

    def check_web_view_opened(self):
        with step("Check web view opened"):
            results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_contents_container"))
            results.should(have.size_greater_than(0))

    def open_languages_list(self):
        with step("Open languages list"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/page_language")).click()

    def change_language_to_index(self, index=0):
        with step("Change language"):
            browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/localized_language_name"))[index].click()

    def check_first_language(self, language):
        with step("Check first language in the list"):
            result = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/localized_language_name"))[0]
            result.should(have.text(language))


wiki_app_page = WikiAppPage()
