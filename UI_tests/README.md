# Настройка и запуск UI тестов

Этот проект содержит UI тесты, которые можно запускать с помощью `pytest`.


## Инструкция по настройке
1.Создайте виртуальное окружение:

 
    python -m venv venv

2.Активируйте виртуальное окружение:\
1)На Windows:

    venv\Scripts\activate
2)На macOS/Linux:

   
    source venv/bin/activate

3.Установка зависимостей:

 
    pip install -r requirements.txt

4.Запуск теста:


    pytest -s -v --tb=line test1.py 



