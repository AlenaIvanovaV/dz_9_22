import datetime
from dataclasses import dataclass
from datetime import date


@dataclass
class Form:
  first_name: str
  last_name: str
  email: str
  number: str
  address: str
  birthday: datetime.date
  hobby: str
  image: str
  gender: str
  subjects: str
  state: str
  city: str


aivanova = Form(last_name='Alena',
                first_name='Ivanova',
                number='7927563999',
                email='alena@mail.ru',
                gender='Female',
                subjects='English',
                hobby='Sports',
                birthday=date(1995, 9, 4),
                state='NCR',
                city='Delhi',
                address='Астрахань',
                image='img.png'

                )
