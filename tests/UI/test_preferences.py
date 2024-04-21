from pages.ui.preferences_page import preferences_page
import allure


class TestPreferences:


    @allure.label("owner", "Anna")
    @allure.epic("wiki preferences")
    @allure.feature("Change the signature")
    @allure.label("web")
    def test_change_signature(self):
        preferences_page.open()
        preferences_page.change_signature("Anna Kaktusova")
        preferences_page.test_signature("Anna Kaktusova")
        preferences_page.change_signature("Ann.Kaktus")
