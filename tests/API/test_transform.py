from utils.api import request_post
import allure


@allure.label("owner", "Anna")
@allure.epic("wiki REST API")
@allure.feature("Test transform API request")
@allure.label("api")
def test_api_search():
    with allure.step("transform html to wiki aoi request"):
        result = request_post("transform/html/to/wikitext", {"html": "<h1>header</h1><p>paragraph</p>"})
        assert result.status_code == 200
        assert result.text == "= header =\nparagraph"
