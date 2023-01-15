import pytest
from selene.support.shared import browser


@pytest.fixture()
def set_browser_size_window():
    browser.config.window_height = 1920
    browser.config.window_width = 1080


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1600
    browser.config.window_height = 1440

    yield

    browser.close()
