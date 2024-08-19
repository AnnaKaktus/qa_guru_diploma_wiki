import os
import allure
from wikipedia_project_tests.pages.ui.main_page import page
import pytest


class TestAuth:

    @allure.label("owner", "Anna")
    @allure.epic("wiki main")
    @allure.feature("Web login")
    @allure.label("web")
    @pytest.mark.ui
    def test_auth_with_valid_creds(self):
        page.open_page()
        page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_VALID"))
        page.check_logged_user("Ann.Kaktus")

    @allure.label("owner", "Anna")
    @allure.epic("wiki main")
    @allure.feature("Web login")
    @allure.label("web")
    @pytest.mark.ui
    def test_auth_with_invalid_creds(self):
        page.open_page()
        page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_INVALID"))
        page.check_auth_error()
