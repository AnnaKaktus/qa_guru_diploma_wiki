from selene import browser, have
import allure
from wikipedia_project_tests.pages.ui.main_page import page
import os


class PreferencesPage:
    def open(self):
        with allure.step("Open the user settings"):
            page.open_page()
            page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_VALID"))
            page.open_page("Special:Preferences")

    def change_signature(self, signature):
        with allure.step("Change the signature"):
            browser.element("#ooui-php-34").clear()
            browser.element("#ooui-php-34").type(signature)
            browser.element("#prefcontrol button").click()

    def test_signature(self, signature):
        with allure.step("Check the signature"):
            browser.element("#mw-htmlform-signature").should(have.text(signature))


preferences_page = PreferencesPage()
