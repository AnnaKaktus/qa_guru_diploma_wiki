from selene import browser, have
import allure
from pages.ui.main_page import page
import os


class UserSandboxPage:
    def open(self, name):
        with allure.step("Открываем песочницу страницы пользователя"):
            page.open_page()
            page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_VALID"))
            page.open_page("Special:EditPage/User:" + name + "/sandbox")

    def edit_preview(self, text):
        with allure.step("Редактируем в песочнице"):
            browser.element("#wpTextbox1").type(text)
            browser.element("#wpPreviewWidget input").click()

    def clear_preview(self):
        with allure.step("Очистка превью песочницы"):
            browser.element("#wpTextbox1").clear()
            browser.element("#wpPreview").click()

    def check_sandbox(self, name):
        with allure.step("Проверка песочницы"):
            browser.element("#wikiPreview").should(have.text("To start a page called " + name))

    def check_have_text(self, text):
        with allure.step("Проверка наличия текста в редакторе"):
            browser.element("#wikiPreview .mw-content-ltr").should(have.text(text))

    def check_have_no_text(self, text):
        with allure.step("Проверка отсутствия текста в редакторе"):
            browser.element("#wikiPreview .mw-content-ltr").should(have.no.text(text))


sandbox_page = UserSandboxPage()
