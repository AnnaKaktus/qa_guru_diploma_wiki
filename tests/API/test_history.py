from jsonschema import validate
from schemas.schemas_wiki import get_history_count
import allure
import pytest
from utils.api import request_get


@allure.label("owner", "Anna")
@allure.epic("wiki REST API")
@allure.feature("History count API request")
@allure.label("api")
@pytest.mark.API
def test_api_history_count():
    with allure.step("Send 'Get history' API request"):
        result = request_get("page/Ramesses_II/history/counts/anonymous")
    with allure.step("Check the response"):
        assert result.status_code == 200
        validate(result.json(), schema=get_history_count)
