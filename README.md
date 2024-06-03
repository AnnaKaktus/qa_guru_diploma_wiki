# Проект по тестированию сайта Wikipedia

> <a target="_blank" href="https://en.wikipedia.org/wiki/Main_Page">Ссылка на  вики</a>

#### Список проверок, реализованных в автотестах

- [x] Проверка авторизации с валидными и не валидными данными
- [x] Проверка смены языка
- [x] Провека лоаута
- [x] Провека настроек пользователя
- [x] Проверка поиска по статьям с валидными и невалидными данными
- [x] Проверка формирования короткой ссылки на статью
- [x] Провкерка редактирования в "песочнице"

### Структура проекта

### Проект реализован с использованием

Python Pytest PyCharm Selenoid Selene Jenkins Allure Report Telegram

<img src="/design/logos/python-original.svg" alt="Image 1" width="45" height="45"><img src="/design/logos/pytest-original.svg" alt="Image 2" width="45" height="45"><img src="/design/logos/PyCharm_Icon.svg" alt="Image 3" width="45" height="45"><img src="/design/logos/selenoid.png" alt="Image 4" width="45" height="45"><img src="/design/logos/jenkins-original.svg" alt="Image 5" width="45" height="45">
<img src="/design/logos/allure.png" alt="Image 6" width="45" height="45"><img src="/design/logos/telegram.svg" alt="Image 7" width="45" height="45">

# Запуск автотестов выполняется на сервере Jenkins

> <a target="_blank" href="https://jenkins.autotests.cloud/job/009-AnnaKaktus_qaguru_09-15/">Ссылка на проект в
> Jenkins</a>

### Для запуска автотестов в Jenkins

#### 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/009-AnnaKaktus_qaguru_09-15/">проект</a>

![This is an image](/design/screens/jenkins.png)

#### 2. Выбрать пункт **Собрать с параметрами**

#### 3. В случае необходимости изменить параметры, выбрав значения из выпадающих списков

#### 4. Нажать **Собрать**

#### 5. Результат запуска сборки можно посмотреть в отчёте Allure

![This is an image](/design/screens/allure_screen.png)

### Локальный запуск автотестов

1. Стянуть репозиторий на свой локальный компьютер при помощи git clone
2. Создать и активировать виртуальное окружение

  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

3. Установить зависимости с помощью команды

  ```bash
  pip install -r requirements.txt
  ```

4. Для запусков тестов удаленно использовать команду

  ```bash
   python3 -m pytest
  ```

Получение отчёта allure:

```bash
allure serve allure-results
``` 

### Пример видеозаписи прохождения UI-теста

![This is an image](/design/screens/test_video.gif)

### Пример видеозаписи прохождения mobile-теста
![This is an image](/design/screens/mobile_video.gif)

### Настроено автоматическое оповещение о результатах сборки Jenkins в Telegram-бот

![This is an image](/design/screens/tg_screen.png)