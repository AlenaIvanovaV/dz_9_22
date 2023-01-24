from selene import command
from selene import have
from selene.support.shared import browser
from qa_test.models.data.studentform import*

from qa_test.models import control
from qa_test.models.control import dropdown, checkbox, datepicker, radiobutton, modal
from qa_test.utils import files


def type_user(name, lastname, number, mail):
    browser.element('#firstName').type(name)
    browser.element('#lastName').type(lastname)
    browser.element('#userEmail').type(mail)
    browser.element('#userNumber').type(number)


def select_city(city):
    dropdown.dropdown_select('#city', city.value[0])


def select_state(state):
    dropdown.dropdown_select('#state', state.value[0])


def checkbox_select(hobby):
    browser.element('[for="hobbies-checkbox-2"]').perform(command.js.scroll_into_view)
    for r in hobby:
     checkbox.checkboxes_click(browser.all('[for^="hobbies-checkbox"]'), r.value[0])



def radio_select(gender):
    radiobutton.set_gender(browser.all('[for^=gender-radio]'), gender.value[0])


def subjects(subject):
    browser.element('#subjectsInput').type(subject).press_enter()


def picture(path_to_picture):
    files.input_files('#uploadPicture', path_to_picture)


def submit():
    browser.element('#submit').press_enter()


def set_address(value):
    browser.element('#currentAddress').type(value)


def birthday_date(birthday):
    datepicker.set_date(day=birthday.day, month=birthday.month, year=birthday.year)


def submitted(data):
    rows = control.modal.dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))

def fill_data(form: Form):
     type_user(form.last_name,form.first_name,form.number,form.email)
     radio_select(form.gender)
     checkbox_select(form.hobby)
     select_state(form.state)
     select_city(form.city)
     birthday_date(form.birthday)
     set_address(form.address)
     picture(form.image)
     subjects(form.subjects)

