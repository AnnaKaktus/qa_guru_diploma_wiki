from pages.ui.user_sandbox_page import sandbox_page
import pytest
import allure


class TestUserSandbox:

    @allure.label("owner", "Anna")
    @allure.epic("wiki sandbox")
    @allure.feature("Edit in the sandbox")
    @allure.label("web")
    @pytest.mark.ui
    @pytest.mark.xfail()
    def test_edit(self):
        text = "A NEW PREVIEW FOR THE MY PAGE"
        sandbox_page.open("Ann.Kaktus")
        sandbox_page.edit_preview(text)
        sandbox_page.check_have_text(text)
        sandbox_page.clear_preview()
        sandbox_page.check_have_no_text(text)
