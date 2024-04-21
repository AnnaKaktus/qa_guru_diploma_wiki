from jsonschema import validate
from schemas.schemas_wiki import get_search, get_page
import allure
from utils.api import request_get


@allure.label("owner", "Anna")
@allure.epic("wiki REST API")
@allure.feature("Test get article API request")
@allure.label("api")
def test_api_get_article():
    with allure.step("get article api request"):
        result = request_get("page/Ramesses_II/bare")
        assert result.status_code == 200
        validate(result.json(), schema=get_page)


@allure.label("owner", "Anna")
@allure.epic("wiki REST API")
@allure.feature("Test get not existed article API request")
@allure.label("api")
def test_api_get_not_existed_article():
    with allure.step("get not existed article api request"):
        result = request_get("page/Ramesses_IXXX/bare")
        assert result.status_code == 404
