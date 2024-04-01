from selene import have
from selene.support.shared import browser
import os

from pages.main_page import page


def test_auth_with_valid_creds():
    page.open_page()
    page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_VALID"))
    browser.element("#pt-userpage-2").click()


def test_auth_with_invalid_creds():
    page.open_page()
    page.login(os.getenv("LOGIN_VALID"), os.getenv("PASSWORD_INVALID"))
    browser.element(".mw-message-box-error").should(have.text("Incorrect username or password entered"))
