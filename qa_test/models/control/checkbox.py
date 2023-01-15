# noinspection PyUnresolvedReferences
from selene import have
from selene.support.shared import browser

def checkboxes_click(elements, *by_texts):
    for value in by_texts:
        elements.element_by(have.text(value)).click()