from wikipedia_project_tests.pages.ui.main_page import page
import allure
import pytest


class TestSearch:

    @allure.label("owner", "Anna")
    @allure.epic("wiki main")
    @allure.feature("Search article")
    @allure.label("web")
    @pytest.mark.ui
    def test_search_existing_article(self):
        page.open_page()
        page.search("ramesses")
        page.open_link("Ramesses II")
        page.check_article_header("Ramesses II")

    @allure.label("owner", "Anna")
    @allure.epic("wiki main")
    @allure.feature("Search article")
    @allure.label("web")
    @pytest.mark.ui
    def test_search_not_existing_article(self):
        page.open_page()
        page.search("rameghgh")
        page.check_not_found()
