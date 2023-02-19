
from selene.support.shared import browser
from qa_test.models.data.studentform import*
from qa_test.models.pages import practice_form
import allure
from allure_commons._allure import attach
from qa_test.utils import attach
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def test_fill_form(open_browser):
  options = Options()
  selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
  options.capabilities.update(selenoid_capabilities)
  driver = webdriver.Remote(
         command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
         options=options)
  browser.config.driver = driver
  with allure.step('Открыть форму регистрации студента'):
    browser.open('/automation-practice-form')
  with allure.step('Заполняем данные'):
    practice_form.fill_data(aivanova)
  with allure.step('Сохраняем данные'):
    practice_form.submit()
  with allure.step('Проверяем данные'):
    practice_form.submitted(
              [
                  ('Student Name', 'Alena Ivanova'),
                  ('Student Email', 'alena@mail.ru'),
                  ('Gender', 'Female'),
                  ('Mobile', '7927563999'),
                  ('Date of Birth', '04 October,1995'),
                  ('Subjects', 'English'),
                  ('Hobbies', 'Sports'),
                  ('Picture', 'img.png'),
                  ('Address', 'Астрахань'),
                  ('State', 'NCR Delhi'),
              ],
          )
  attach.add_html(browser)
  attach.add_screenshot(browser)
  attach.add_logs(browser)
  attach.add_video(browser)