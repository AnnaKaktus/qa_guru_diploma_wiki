from wikipedia_project_tests.pages.ui.main_page import page
import allure
import pytest


class TestLanguages:
    @allure.label("owner", "Anna")
    @allure.epic("wiki main")
    @allure.feature("Check change the langauge to Russian")
    @allure.label("web")
    @pytest.mark.ui
    def test_language_change(self):
        page.open_page("Ramesses_II")
        page.change_language()
        page.check_article_header("Рамсес II")
