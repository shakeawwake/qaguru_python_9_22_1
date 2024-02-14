### Локальный запуск автотестов на эмуляторе
1. Клонировать репозиторий на свой локальный компьютер при помощи git clone
2. Создать и активировать виртуальное окружение
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```
3. Установить зависимости с помощью pip
  ```bash
  pip install -r requirements.txt
  ```
4. Установить необходимое для эмуляции андроида на PC
  ```bash
  appium --base-path /wb/hub
  ```
5. Запустить эмулятор через Android Studio

6. Использовать команду для локального запуска тестов: 
  ```bash
  pytest -sv -m local tests/tests_android/test_android.py --context='local'
  ```
7. Получить отчёт allure:
```bash
allure serve allure-results
```
 
### Локальный запуск автотестов на bs

1. Выполнить
```bash
 pytest -sv -m bs tests/tests_android/test_android.py --context='bs'
```
2. Получить отчёта allure:
```bash
allure serve allure-results