from pages.mobile.wiki_app_page import wiki_app_page
import allure


class TestOpenArticleWebView:

    @allure.label("owner", "Anna")
    @allure.epic("wiki mobile")
    @allure.feature("Test if wiki article web view opened")
    @allure.label("mobile")
    def test_open_article_web_view(self):
        wiki_app_page.search_and_open("Ramesses II")
        wiki_app_page.check_web_view_opened()
