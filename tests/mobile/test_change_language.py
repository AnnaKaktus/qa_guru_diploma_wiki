from pages.mobile.wiki_app_page import wiki_app_page
import allure


class TestChangeLanguage:
    @allure.label("owner", "Anna")
    @allure.epic("wiki mobile")
    @allure.feature("Test language check")
    @allure.label("mobile")
    def test_change_language(self):
        wiki_app_page.search_and_open("Ramesses II")
        wiki_app_page.open_languages_list()
        wiki_app_page.check_first_language("Afrikaans")
        wiki_app_page.change_language_to_index(0)
        wiki_app_page.open_languages_list()
        wiki_app_page.check_first_language("English")
