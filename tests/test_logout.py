from selene.support.shared import browser
import allure
import os

from pages.dashboard_page import DashboardPage


def test_logout():
    page = DashboardPage()
    with allure.step("Открываем страницу дашборда и логинимся для проверки логаута"):
        page.open_page()
        page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_VALID"))
    with allure.step("Проверки логаута"):
        page.logout()
        browser.element(".ant-col-xs-0 .cy-login-button").click()
