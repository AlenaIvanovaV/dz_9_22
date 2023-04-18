import os

from selene.support.shared import browser

import tests


def input_files(element, file):
  browser.element(element).set_value(
    os.path.abspath(os.path.join(os.path.dirname(tests.__file__), f'files/{file}'))
  )
