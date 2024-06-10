import pytest
import allure
from pages.ui.main_page import page


class TestTools:

    @allure.label("owner", "Anna")
    @allure.epic("wiki tools")
    @allure.feature("Url shortener")
    @allure.label("web")
    @pytest.mark.ui
    @pytest.mark.xfail()
    def test_short_url(self):
        page.open_page("Ramesses_II")
        page.use_tool("short_url")
        page.check_short_url_created()
