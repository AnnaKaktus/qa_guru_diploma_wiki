from selene import browser, have
import allure
from wikipedia_project_tests.pages.ui.main_page import page
import os


class UserSandboxPage:
    def open(self, name):
        with allure.step("Open the sandbox page"):
            page.open_page()
            page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_VALID"))
            page.open_page("Special:EditPage/User:" + name + "/sandbox")

    def edit_preview(self, text):
        with allure.step("Edit text in the sandbox"):
            browser.element("#wpTextbox1").type(text)
            browser.element("#wpPreviewWidget input").click()

    def clear_preview(self):
        with allure.step("Clear the sandbox preview"):
            browser.element("#wpTextbox1").clear()
            browser.element("#wpPreview").click()

    def check_sandbox(self, name):
        with allure.step("Check if sandbox is opened"):
            browser.element("#wikiPreview").should(have.text("To start a page called " + name))

    def check_have_text(self, text):
        with allure.step("Check the text in the sandbox"):
            browser.element("#wikiPreview .mw-content-ltr").should(have.text(text))

    def check_have_no_text(self, text):
        with allure.step("Check that the sandbox is clear"):
            browser.element("#wikiPreview .mw-content-ltr").should(have.no.text(text))


sandbox_page = UserSandboxPage()
