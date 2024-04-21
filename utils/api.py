import requests
import allure

base_url = "https://en.wikipedia.org/w/rest.php/v1/"


def request_get(url):
    with allure.step("GET request " + url):
        return requests.get(base_url + url)


def request_post(url, json):
    with allure.step("POST request " + url):
        return requests.post(base_url + url, json=json)
