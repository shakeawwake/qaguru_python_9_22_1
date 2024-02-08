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
  pytest -sv -m local tests/tests_android/test_android.py --context='local'
  ```
7. Получение отчёта allure:
```bash
allure serve allure-results
```
 
### Локальный запуск автотестов на bs

1. Выполните
```bash
 pytest -sv -m bs tests/tests_android/test_android.py --context='bs'
```
2. Получение отчёта allure:
```bash
allure serve allure-results