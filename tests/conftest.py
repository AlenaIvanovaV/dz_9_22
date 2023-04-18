import pytest
from selene.support.shared import browser
from qa_test.utils import attach


@pytest.fixture(scope="function", autouse=True)
def open_browser():
  browser.config.base_url = 'https://demoqa.com'
  browser.config.window_width = 1600
  browser.config.window_height = 1440
  yield
  attach.add_html(browser)
  attach.add_screenshot(browser)
  attach.add_logs(browser)
  attach.add_video(browser)
  browser.close()
