from utils.api import request_post
import allure
import pytest


@allure.label("owner", "Anna")
@allure.epic("wiki REST API")
@allure.feature("Transform API request")
@allure.label("api")
@pytest.mark.api
def test_api_search():
    with allure.step("Send 'transform html to wiki' API request"):
        result = request_post("transform/html/to/wikitext", {"html": "<h1>header</h1><p>paragraph</p>"})
    with allure.step("Check the response"):
        assert result.status_code == 200
        assert result.text == "= header =\nparagraph"
