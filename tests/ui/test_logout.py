import os
import allure
import pytest
from wikipedia_project_tests.pages.ui.main_page import page

class TestLogout:
    @allure.label("owner", "Anna")
    @allure.epic("wiki main")
    @allure.feature("Logout")
    @allure.label("web")
    @pytest.mark.ui
    def test_logout(self):
        page.open_page()
        page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_VALID"))
        page.logout()
        page.check_logged_out()
