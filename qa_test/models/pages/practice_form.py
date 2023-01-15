from selene import have
from selene.support.shared import browser
from qa_test.models import control
from qa_test.models.control import dropdown, checkbox,datepicker,radiobutton,modal
from selene import command
from qa_test.utils import files
def type_user(name,lastname,number,mail):
    browser.element('#firstName').type(name)
    browser.element('#lastName').type(lastname)
    browser.element('#userEmail').type(mail)
    browser.element('#userNumber').type(number)

def select_city(value):
    dropdown.dropdown_select('#city', by_text=value)


def select_state(value):
    dropdown.dropdown_select('#state', by_text=value)

def checkbox_select(hobby):
    checkbox.checkboxes_click(browser.all('[for="hobbies-checkbox-1"]'), hobby)
    browser.element('[for="hobbies-checkbox-1"]').perform(command.js.scroll_into_view)

def radio_select(gender):
    radiobutton.set_gender(browser.all('[for^=gender-radio]'),gender)

def subjects(subject):
    browser.element('#subjectsInput').type(subject).press_enter()
def picture (path_to_picture):
        files.input_files('#uploadPicture', path_to_picture)
def submit():
    browser.element('#submit').press_enter()

def set_address(value):
    browser.element('#currentAddress').type(value)
def birthday_date(month, year, day):
    datepicker.set_date(month, year, day)

def submitted(data):
    rows = control.modal.dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))



