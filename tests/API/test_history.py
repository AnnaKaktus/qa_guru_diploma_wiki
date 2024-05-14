from jsonschema import validate
from schemas.schemas_wiki import get_history_count
import allure
from utils.api import request_get


@allure.label("owner", "Anna")
@allure.epic("wiki REST API")
@allure.feature("Test history count")
@allure.label("api")
def test_api_history_count():
    with allure.step("get article api request"):
        result = request_get("page/Ramesses_II/history/counts/anonymous")
        print(result.json())
        assert result.status_code == 200
        validate(result.json(), schema=get_history_count)
