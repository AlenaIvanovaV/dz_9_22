from selene import command
from selene import have
from selene.support.shared import browser
from qa_test.models import control
from qa_test.models.control import dropdown, checkbox, datepicker, radiobutton, modal
from qa_test.utils import files


def type_user(name, lastname, number, mail):
  browser.element('#firstName').type(name)
  browser.element('#lastName').type(lastname)
  browser.element('#userEmail').type(mail)
  browser.element('#userNumber').type(number)


def select_city(city):
  dropdown.dropdown_select('#city', city)


def select_state(state):
  dropdown.dropdown_select('#state', state)


def checkbox_select(hobby):
  browser.element('[for="hobbies-checkbox-2"]').perform(command.js.scroll_into_view)
  checkbox.checkboxes_click(browser.all('[for^="hobbies-checkbox"]'), hobby)


def radio_select(gender):
  radiobutton.set_gender(browser.all('[for^=gender-radio]'), gender)


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
  rows = browser.element('.modal-content').all('tbody tr')
  for row, value in data:
    rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))


def fill_data(a):
  type_user(a.last_name, a.first_name, a.number, a.email)
  radio_select(a.gender)
  checkbox_select(a.hobby)
  select_state(a.state)
  select_city(a.city)
  birthday_date(a.birthday)
  set_address(a.address)
  picture(a.image)
  subjects(a.subjects)
