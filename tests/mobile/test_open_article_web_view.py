from wikipedia_project_tests.pages.mobile.wiki_app_page import wiki_app_page
import allure
import pytest


class TestOpenArticleWebView:

    @allure.label("owner", "Anna")
    @allure.epic("wiki mobile")
    @allure.feature("Test if wiki article web view opened")
    @allure.label("mobile")
    @pytest.mark.api
    def test_open_article_web_view(self):
        wiki_app_page.search_and_open("Ramesses II")
        wiki_app_page.check_web_view_opened()
