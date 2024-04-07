from pages.ui.main_page import page
import allure

@allure.label("owner", "Anna")
@allure.epic("wiki main")
@allure.feature("Check change the langauge to Russian")
@allure.label("web")
def test_language_change():
    page.open_page("Ramesses_II")
    page.change_language()
    page.check_article_header("Рамсес II")
