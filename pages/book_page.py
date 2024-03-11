from selene.support.shared import browser
from selene import have


class BookPage:
    def add_book(self):
        browser.element(".ant-row-center button svg").click()

    def remove_book(self):
        browser.element(".ant-row-center button svg").click()
        browser.element(".ant-popover-inner-content>div:last-of-type>div:last-of-type").should(
            have.text("Удалить из моих книг")).click()
