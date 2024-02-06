### Локальный запуск автотестов на эмуляторе
1. Клонируйте репозиторий на свой локальный компьютер при помощи git clone
2. Создайте и активируйте виртуальное окружение
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```
3. Установите зависимости с помощью pip
  ```bash
  pip install -r requirements.txt
  ```
4. Пройдите несколько кругов ада и установите все, что необходимо для эмуляции андроида на PC
  ```bash
  appium --base-path /wb/hub
  ```
5. Запустите эмулятор через Android Studio

6. Для запусков тестов локально используйте команду 
  ```bash
  app=app-alpha-universal-release.apk pytest -s
  ```
7. Получение отчёта allure:
```bash
allure serve allure-results
```
 
### Локальный запуск автотестов на bs

1. Выполните
```bash
 app=bs://simple.app pytest -s
```
2. Получение отчёта allure:
```bash
allure serve allure-results