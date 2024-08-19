import os
import allure
import pytest
from wikipedia_project_tests.pages.mobile.wiki_app_page import wiki_app_page


class TestAuthMobile:

    @allure.label("owner", "Anna")
    @allure.epic("wiki mobile")
    @allure.feature("Mobile login")
    @allure.label("mobile")
    @pytest.mark.api
    def test_login(self):
        wiki_app_page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_VALID"))
        wiki_app_page.check_login("Ann.Kaktus")
        wiki_app_page.logout()
