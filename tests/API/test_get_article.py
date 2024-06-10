from jsonschema import validate
from schemas.schemas_wiki import get_page
import allure
import pytest
from utils.api import request_get


@allure.label("owner", "Anna")
@allure.epic("wiki REST API")
@allure.feature("Get the article API request")
@allure.label("api")
@pytest.mark.API
def test_api_get_article():
    with allure.step("Send 'Get article' API request"):
        result = request_get("page/Ramesses_II/bare")
    with allure.step("Check the response"):
        assert result.status_code == 200
        validate(result.json(), schema=get_page)


@allure.label("owner", "Anna")
@allure.epic("wiki REST API")
@allure.feature("Get the article API request")
@allure.label("api")
@pytest.mark.API
def test_api_get_not_existed_article():
    with allure.step("Tests 'Get article' API request for the article that not exist"):
        result = request_get("page/Ramesses_IXXX/bare")
    with allure.step("Check the response, be sure that error was risen"):
        assert result.status_code == 404
