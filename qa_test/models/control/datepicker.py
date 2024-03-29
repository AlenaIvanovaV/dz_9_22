from selene.support.shared import browser


def set_date(day, month, year):
  browser.element('#dateOfBirthInput').click()
  browser.element('.react-datepicker__month-select').click()
  browser.element(f'[value="{month}"]').click()
  browser.element('.react-datepicker__year-select').click()
  browser.element(f'[value="{year}"]').click()
  browser.element(f'.react-datepicker__day--00{day}').click()
