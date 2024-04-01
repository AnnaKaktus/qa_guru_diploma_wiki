from selene.support.shared import browser
import allure
from pages.main_page import page
import os


class UserSandboxPage:
    def open(self):
        with allure.step("Открываем песочницу страницы пользователя"):
            page.open_page()
            page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_VALID"))
            page.open_page("Special:EditPage/User:Ann.Kaktus/sandbox")
            # browser.element(".vector-user-menu").click()
            # browser.element("#pt-sandbox").click()

    def edit_preview(self, text):
        with allure.step("Редактируем в песочнице"):
            browser.element("#wpTextbox1").type(text)
            browser.element("#wpPreview").click()

    def clear_preview(self):
        with allure.step("Очистка превью песочницы"):
            browser.element("#wpTextbox1").clear()
            browser.element("#wpPreview").click()


sandbox_page = UserSandboxPage()
