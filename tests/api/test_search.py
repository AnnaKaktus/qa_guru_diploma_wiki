from pages.ui.main_page import page
import allure


@allure.label("owner", "Anna")
@allure.epic("wiki main")
@allure.feature("Search the existing article")
@allure.label("web")
def test_search_existing_article():
    page.open_page()
    page.search("ramesses")
    page.open_link("Ramesses II")
    page.check_article_header("Ramesses II")

@allure.label("owner", "Anna")
@allure.epic("wiki main")
@allure.feature("Search the unknown article")
@allure.label("web")
def test_search_not_existing_article():
    page.open_page()
    page.search("rameghgh")
    page.check_not_found()
