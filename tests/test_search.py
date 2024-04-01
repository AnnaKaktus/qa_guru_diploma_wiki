from selene import by
from selene.support.shared import browser
from pages.main_page import page


def test_search_existing_article():
    page.open_page()
    page.search("ramesses")
    browser.element(by.text("Ramesses II")).click()


def test_search_not_existing_article():
    page.open_page()
    page.search("rameghgh")
    browser.element(".mw-search-createlink").click()
