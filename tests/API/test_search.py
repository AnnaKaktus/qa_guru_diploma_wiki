from jsonschema import validate
from schemas.schemas_wiki import get_search
from utils.api import request_get
import allure
import pytest


@allure.label("owner", "Anna")
@allure.epic("wiki REST API")
@allure.feature("Search API request")
@allure.label("api")
@pytest.mark.API
def test_api_search():
    with allure.step("Send api request"):
        result = request_get("search/page?q=Ramesses&limit=1")
    with allure.step("Check the response"):
        assert result.status_code == 200
        validate(result.json(), schema=get_search)
