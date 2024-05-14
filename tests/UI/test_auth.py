import os
import allure
from pages.ui.main_page import page


class TestAuth:

    @allure.label("owner", "Anna")
    @allure.epic("wiki main")
    @allure.feature("Check login with valid credentials")
    @allure.label("web")
    def test_auth_with_valid_creds(self):
        page.open_page()
        page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_VALID"))
        page.check_logged_user("Ann.Kaktus")

    @allure.label("owner", "Anna")
    @allure.epic("wiki main")
    @allure.feature("Check login with invalid credentials")
    @allure.label("web")
    def test_auth_with_invalid_creds(self):
        page.open_page()
        page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_INVALID"))
        page.check_auth_error()
