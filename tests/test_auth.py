from selene.support.shared import browser
from selene import by
import allure
import os

from pages.dashboard_page import DashboardPage


def test_auth_with_valid_creds():
    page = DashboardPage()
    with allure.step("Открываем страницу дашборда для проверки верного логина"):
        page.open_page()
    with allure.step("Проверка логина"):
        page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_VALID"))
        browser.element(".ant-col-xs-0 .cy-user-header-avatar").click()


def test_auth_with_invalid_creds():
    page = DashboardPage()
    with allure.step("Открываем страницу дашборда для проверки неверного пароля"):
        page.open_page()
    with allure.step("Проверка логина с неверным паролем"):
        page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_INVALID"))
        browser.element(by.text("Неверно введен пароль.")).click()
