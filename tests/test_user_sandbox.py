from selene import have
from selene.support.shared import browser
from pages.user_sandbox_page import sandbox_page


def test_show_notes():
    sandbox_page.open()
    sandbox_page.edit_preview("")
    browser.element("#wikiPreview .ombox").should(have.text("This is the user sandbox of Ann.Kaktus"))

def test_edit():
    sandbox_page.open()
    sandbox_page.edit_preview("A NEW PREVIEW FOR THE MY PAGE")
    browser.element("#wikiPreview .mw-content-ltr").should(have.text("A NEW PREVIEW FOR THE MY PAGE"))
    sandbox_page.clear_preview()
    browser.element("#wikiPreview .mw-content-ltr").should(have.no.text("A NEW PREVIEW FOR THE MY PAGE"))