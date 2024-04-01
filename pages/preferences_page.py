from selene.support.shared import browser
import allure
from pages.main_page import page
import os


class PreferencesPage:
    def open(self):
        with allure.step("Открываем настройки пользователя"):
            page.open_page()
            page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_VALID"))
            page.open_page("Special:Preferences")

    def change_signature(self, signature):
        with allure.step("Изменение подписи"):
            browser.element("#ooui-php-34").clear()
            browser.element("#ooui-php-34").type(signature)
            browser.element("#prefcontrol button").click()


preferences_page = PreferencesPage()
