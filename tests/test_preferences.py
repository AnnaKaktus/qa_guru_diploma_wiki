from selene import have
from selene.support.shared import browser
from pages.preferences_page import preferences_page


def test_change_signature():
    preferences_page.open()
    preferences_page.change_signature("Anna Kaktusova")
    browser.element("#mw-htmlform-signature").should(have.text("Anna Kaktusova"))
    preferences_page.change_signature("Ann.Kaktus")
