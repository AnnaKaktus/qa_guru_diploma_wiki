import requests
import allure
from wikipedia_project_tests.utils import attach
from wikipedia_project_tests.utils import api_log


def api_request(base_url, endpoint, method, data=None, params=None, response_type="json"):
    url = f"{base_url}{endpoint}"
    response = requests.request(method, url, data=data, params=params)
    api_log.response_logging(response)
    attach.response_attaching(response, response_type=response_type)
    return response


def request_get(base_url, endpoint):
    with allure.step(f"GET request {endpoint}"):
        return api_request(base_url, endpoint, "GET")


def request_post(base_url, endpoint, data, response_type):
    with allure.step(f"POST request {endpoint}"):
        return api_request(base_url, endpoint, "POST", data=data, response_type=response_type)
