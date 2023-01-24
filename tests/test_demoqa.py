from selene.support.shared import browser

from qa_test.models.data.studentform import*
from qa_test.models.pages import practice_form


def test_fill_form(open_browser):
    browser.open('/automation-practice-form')

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

    practice_form.fill_data(aivanova)
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
