import pytest

@pytest.fixture
def base_url(scope="function", autouse=True):
    return "https://en.wikipedia.org/w/rest.php/v1/"