import allure
import os

from pages.dashboard_page import DashboardPage
from pages.shelf_page import ShelfPage


def test_add_shelf():
    dashboard_page = DashboardPage()
    shelf_page = ShelfPage()

    with allure.step("Авторизации перед добавлением полки"):
        dashboard_page.open_page()
        dashboard_page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_VALID"))
    with allure.step("Добавление полки"):
        shelf_page.open_shelf_page()
        shelf_page.create_shelf(name="test shelf", description="about my tests")

    with allure.step("Удаление полки"):
        shelf_page.remove_shelf("test shelf")
