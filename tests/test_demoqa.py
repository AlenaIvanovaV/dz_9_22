from selene import have, command
from selene.support.shared import browser
from qa_test.models.pages import practice_form
from qa_test.models.control import dropdown

from qa_test.utils import files
def test_fill_form(open_browser):
    browser.open('/automation-practice-form')
    practice_form.type_user('Alena','Ivanova','7927563999','alena@mail.ru')
    practice_form.checkbox_select('Sports')
    practice_form.select_state('NCR')
    practice_form.select_city('Delhi')
    practice_form.radio_select('Female')
    practice_form.set_address('Астрахань')
    practice_form.picture('files/img.png')
    practice_form.subjects('English')
    practice_form.birthday_date('9', '1995', '04')
    practice_form.submit()
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



