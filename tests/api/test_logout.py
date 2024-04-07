import os
import allure
from pages.ui.main_page import page

@allure.label("owner", "Anna")
@allure.epic("wiki main")
@allure.feature("Logout")
@allure.label("web")
def test_logout():
    page.open_page()
    page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_VALID"))
    page.logout()
    page.check_logged_out()
