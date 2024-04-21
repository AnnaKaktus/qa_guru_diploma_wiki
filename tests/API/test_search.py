from jsonschema import validate
from schemas.schemas_wiki import get_search
from utils.api import request_get
import allure


@allure.label("owner", "Anna")
@allure.epic("wiki REST API")
@allure.feature("Test search API request")
@allure.label("api")
def test_api_search():
    with allure.step("search api request"):
        result = request_get("search/page?q=Ramesses&limit=1")
        assert result.status_code == 200
        validate(result.json(), schema=get_search)
