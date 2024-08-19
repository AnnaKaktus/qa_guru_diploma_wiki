from jsonschema import validate
from schemas.schemas_wiki import get_history_count
import allure
import pytest
from wikipedia_project_tests.utils.api import request_get


@allure.label("owner", "Anna")
@allure.epic("wiki REST API")
@allure.feature("History count API request")
@allure.label("api")
@pytest.mark.api
def test_api_history_count(base_url):
    with allure.step("Send 'Get history' API request"):
        result = request_get(base_url, "page/Ramesses_II/history/counts/anonymous")
    with allure.step("Check the response"):
        assert result.status_code == 200
        validate(result.json(), schema=get_history_count)
        assert result.json()["count"] > 1831
