from jsonschema import validate
from schemas.schemas_wiki import get_page, error_json
import allure
import pytest
from wikipedia_project_tests.utils.api import request_get


@allure.label("owner", "Anna")
@allure.epic("wiki REST API")
@allure.feature("Get article API request")
@allure.label("api")
@pytest.mark.api
def test_api_get_article(base_url):
    with allure.step("Send 'Get article' API request"):
        result = request_get(base_url, "page/Ramesses_II/bare")
    with allure.step("Check the response"):
        assert result.status_code == 200
        validate(result.json(), schema=get_page)
        assert result.json()["title"] == "Ramesses II"

@allure.label("owner", "Anna")
@allure.epic("wiki REST API")
@allure.feature("Get article API request, not existed")
@allure.label("api")
@pytest.mark.api
def test_api_get_not_existed_article(base_url):
    with allure.step("Tests 'Get article' API request for the article that not exist"):
        result = request_get(base_url, "page/Ramesses_IXXX/bare")
    with allure.step("Check the response, be sure that error was risen"):
        assert result.status_code == 404
        validate(result.json(), schema=error_json)
