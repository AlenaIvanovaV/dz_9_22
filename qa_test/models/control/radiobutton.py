from selene import have


def set_gender(elements, *by_texts):
  for value in by_texts:
    elements.element_by(have.text(value)).click()
