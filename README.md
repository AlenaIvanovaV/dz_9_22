## Проект UI автотестов demoqa.com

<!-- Технологии -->

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="./attachments/logo/pycharm.svg"></code>
  <code><img width="5%" title="Python" src="./attachments/logo/Python-logo-notext.svg"></code>
  <code><img width="5%" title="Pytest" src="./attachments/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="./attachments/logo/selene.png"></code>
 <code><img width="5%" title="Selene" src="./attachments/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="./attachments/logo/git-logo.svg"></code>
  <code><img width="5%" title="Allure Report" src="./attachments/logo/allure-Report-logo.svg"></code>
  <code><img width="5%" title="Jenkins" src="./attachments/logo/jenkins1.png"></code>
  <code><img width="5%" title="Selenoid" src="./attachments/logo/selenoid-logo.svg"></code>
</p>

### Что выполняет тест:
- [x] Заполняет данные формы
- [x] Отправляет заполненные данные
- [x] Проверяет правильность заполненных данных

<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="attachments/logo/jenkins.png"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/qa_quru_jenkins/)

##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение, через виртуальную машину при помощи Selenoid.
![This is an image](attachments/screenshots/jenkins.png)

<!-- Allure report -->

### <img width="3%" title="Allure Report" src="attachments/logo/allure_report.png"> Allure report

##### После прохождения тестов, результаты автоматически сохраняются. Чтобы посмотреть Allure отчет нужно нажать на иконке allure report у сборки.
![This is an image](attachments/screenshots/allure.png)

##### Во вкладке Suites находятся подробные данные о прохождении теста с приложенными логами, скриншотами и видео о прохождении теста
![This is an image](attachments/screenshots/allure-report.png)

##### Видео прохождение теста
![This is an image](attachments/video/0cf16075bf6fde5422f9073ac99a42b5.gif)


<!-- Telegram -->

### <img width="3%" title="Telegram" src="resources/logo/Telegram.svg"> Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах, а также ссылка на allure report.

![This is an image](attachments/screenshots/tg_report.png)