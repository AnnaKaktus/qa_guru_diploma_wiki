from selene import by, have
from selene.support.shared import browser
from pages.main_page import page


def test_short_url():
    page.open_page("Ramesses_II")
    page.use_tool("short_url")
    browser.element(by.text("Ramesses II")).click()
    browser.element("#ooui-2").should(have.value_containing("https://w.wiki"))
    browser.element("#ooui-1").should(have.text("https://w.wiki/_dAw"))
