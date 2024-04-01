from selene import have
from selene.support.shared import browser
from pages.main_page import page


def test_languauge_change():
    page.open_page("Ramesses_II")
    browser.element("#p-lang-btn-checkbox").click()
    browser.element(".interwiki-ru").click()
    browser.element("#firstHeading").should(have.text("Рамсес II"))
