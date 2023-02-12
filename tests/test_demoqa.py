import allure
from selene.support.shared import browser
from qa_test.models.data.studentform import*
from qa_test.models.pages import practice_form
from allure_commons._allure import attach
from qa_test.utils import attach

def test_fill_form(open_browser):


    aivanova = Form(last_name='Alena',
                    first_name='Ivanova',
                    number='7927563999',
                    email='alena@mail.ru',
                    gender=Gender.Female,
                    subjects=[Subject.English],
                    hobby=[Hobby.Sports],
                    birthday=date(1995, 9, 4),
                    state=State.NCR,
                    city=City.Delhi,
                    address='Астрахань',
                    image='img.png'

                    )

    with allure.step("Открываем форму регистрации"):
      browser.open('/automation-practice-form')
    with allure.step('Заполняем данные'):
          practice_form.fill_data(aivanova)
    with allure.step('Отправляем форму'):
          practice_form.submit()
    with allure.step('Проверяем форму'):
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
