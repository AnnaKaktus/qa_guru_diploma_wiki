from wikipedia_project_tests.utils.api import request_post
import allure
import pytest


@allure.label("owner", "Anna")
@allure.epic("wiki REST API")
@allure.feature("Transform API request")
@allure.label("api")
@pytest.mark.api
def test_api_search(base_url):
    with allure.step("Send 'transform html to wiki' API request"):
        result = request_post(base_url, "transform/html/to/wikitext/Jupiter",
                              data={"html": "<h1>header</h1><p>paragraph</p>"}, response_type="text")
    with allure.step("Check the response"):
        assert result.status_code == 200
        assert result.text == "= header =\nparagraph"
