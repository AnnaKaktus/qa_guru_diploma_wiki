import requests
import allure
import json
from requests import Response
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_xml(browser):
    xml = browser.driver.page_source
    allure.attach(body=xml, name="screen xml dump", attachment_type=allure.attachment_type.XML, extension=".xml")


def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')


def attach_bstack_video(session_id, login, password):
    bstack_session = requests.get(f"https://api.browserstack.com/app-automate/sessions/{session_id}.json",
                                  auth=(login, password)).json()
    video_url = bstack_session["automation_session"]["video_url"]

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name="video recording",
        attachment_type=allure.attachment_type.HTML,
    )


def response_attaching(response: Response, response_type="json"):
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    if response.request.body:

        allure.attach(
            body=json.dumps(response.request.body, indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )

        attachment_type = AttachmentType.JSON
        body = json.dumps(response.request.body, indent=4, ensure_ascii=True)
        if response_type == "text":
            AttachmentType.TEXT
            body = response.request.body

        allure.attach(
            body=body,
            name="Response",
            attachment_type=attachment_type,
            extension=response_type,
        )
