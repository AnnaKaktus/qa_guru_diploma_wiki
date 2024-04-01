from selene import have
from selene.support.shared import browser
import os

from pages.main_page import page


def test_logout():
    page.open_page()
    page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_VALID"))
    page.logout()
    browser.element("#pt-createaccount-2").should(have.text("Create account"))
