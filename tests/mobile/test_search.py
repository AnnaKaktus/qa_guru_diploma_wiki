import allure
from pages.mobile.wiki_app_page import wiki_app_page


class TestSearch:

    @allure.label("owner", "Anna")
    @allure.epic("wiki mobile")
    @allure.feature("Check article search")
    @allure.label("mobile")
    def test_search_wiki(self):
        wiki_app_page.search("Ramesses II")
        wiki_app_page.check_first_header("Ramesses II")

    @allure.label("owner", "Anna")
    @allure.epic("wiki mobile")
    @allure.feature("Check not existing article search result")
    @allure.label("mobile")
    def test_search_wiki_not_exist(self):
        wiki_app_page.search("rghrht")
        wiki_app_page.check_no_results()
