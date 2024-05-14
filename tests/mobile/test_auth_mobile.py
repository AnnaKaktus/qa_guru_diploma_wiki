import os
import allure
from pages.mobile.wiki_app_page import wiki_app_page


class TestAuthMobile:

    @allure.label("owner", "Anna")
    @allure.epic("wiki mobile")
    @allure.feature("Check mobile login with correct credentials")
    @allure.label("mobile")
    def test_login(self):
        wiki_app_page.login(os.getenv("LOGIN_MOBILE"), os.getenv("PASSWORD_MOBILE"))
        wiki_app_page.check_login("Ann.Kaktus")
        wiki_app_page.logout()
