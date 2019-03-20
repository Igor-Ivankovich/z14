# Lesson 1 22/01/2019
 Для тех кто будет заново все делать в linux

1. Скачать питон https://www.python.org/downloads/
2. Установить pip. https://pip.pypa.io/en/stable/installing/
3. Установить virtualenv - `pip install virtualenv` https://virtualenv.pypa.io/en/stable/installation/
4. Создать переменную окружения. **ЗАПОМНИТЕ РАСПОЛОЖЕНИЕ ПЕРЕМЕННОЙ** `virtualenv env1`
5. Активироать окружение `source env1/bin/activate` (Для unix стистем), 
Для Windows - `cd env1/scripts` `activate`
6. Установить пакет ipython - `pip install ipython`
7. Интерактивный режим - в консоли `ipython`
### Documentation
- https://docs.python.org/3/tutorial/introduction.html
- https://docs.python.org/3/tutorial/controlflow.html
- https://docs.python.org/3/tutorial/datastructures.html
### Books
- http://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf
- http://uchcom7.botik.ru/L/prog/python/python_01.pdf

### Homework (homework1)
- Поставить linux
- Поставить PyCharm
- Почитать 3 ссылки по документации
1. Вводятся три целых числа. Определить какое из них наибольшее.
2. Вводятся два целых числа. Проверить делится ли первое на второе. Вывести на экран сообщение об этом, а также остаток (если он есть) и частное (в любом случае).
3. Перевести число *бит*, введенное пользователем, в байты или килобайты в зависимости от его выбора.

### Homework*
1. Вводится число. Проверить является ли число палиндромом.
2. Вводится буква. Определить, это код английской буквы или какой-либо иной символ

# Lesson 2 25/01/2019
### Documentation 
- https://www.learnpython.org/en/Loops
- https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
- https://www.w3schools.com/python/python_functions.asp

### Homework (homework2)

# Lesson 3 29/01/2019
### Documentation 
- https://www.w3schools.com/python/python_lambda.asp - лямбда функции
- https://docs.python.org/3.3/library/functions.html - встроенные функции
- https://www.tutorialspoint.com/python/python_modules.htm - модули

### Homework (homework3)

# Lesson 4 2/01/2019
### Documentation
- https://git-scm.com/book - книга
- http://schacon.github.io/git/gittutorial.html - туториал
```
Как подтянуть изменения в ваш форк?
git remote add upstream https://github.com/tima-akulich/z14.git
git fetch upstream
git checkout master
git rebase upstream/master
```

### Homework (homework4)

# Lesson 5 5/01/2019
### Documentation
- https://docs.python.org/3.7/library/string.html - строки
- https://en.wikipedia.org/wiki/Regular_expression - регулярные выражения
- https://docs.python.org/3/library/re.html - как работать в python

# Lesson 6 8/01/2019
### Documentation
- https://en.wikipedia.org/wiki/Serialization - сериализация
- https://www.pythonforbeginners.com/cheatsheet/python-file-handling - работа с файлами
- https://docs.python.org/3/library/pickle.html - pickle
- https://docs.python.org/3/library/csv.html - csv
- https://docs.python.org/2/library/xml.etree.elementtree.html - xml
- https://docs.python.org/3/library/json.html - json

# Lesson 7 12/02/2019
### Documentation
- https://docs.python.org/3.7/tutorial/classes.html - дока по классам

# Lesson 8 19/02/2019
### Documentation
- https://docs.python.org/3/tutorial/errors.html - работа с исключениями
- https://habr.com/ru/post/186608/ - магические методы
- https://pillow.readthedocs.io/en/stable/handbook/tutorial.html - работа с картинками

# Lesson 9 22/02/2019
### Documentation
- https://habr.com/ru/post/186608/ - магические методы
- https://habr.com/ru/post/145835/ - метаклассы
- https://habr.com/ru/post/122082/ - дескрипторы
- https://pythonworld.ru/osnovy/with-as-menedzhery-konteksta.html - менеджеры контекста

# Lesson 10 26/02/2019
### Documentation
- https://en.wikipedia.org/wiki/Software_testing - про тестирование
- https://docs.python.org/3/library/unittest.html - юнитесты
- https://coverage.readthedocs.io/en/v4.5.x/cmd.html - покрытие

homework - покрыть unit-тестами функции из домашки homework6 (положить в tests.py)

# Lesson 11 1/03/2019
### Documentation
- https://docs.python.org/3/library/unittest.mock.html - моки
- https://www.tutorialspoint.com/sql/sql-quick-guide.htm

### homework
Потренироваться создавать табилцы в postgresql с разными полями.

Типы полей - http://www.postgresqltutorial.com/postgresql-data-types/

# Lesson 12 5/03/2019
### Documentation
- https://www.tutorialspoint.com/sql/sql-quick-guide.htm - гайд по sql
- https://khashtamov.com/ru/postgresql-python-psycopg2/ - библиотека psycopg2

### homework
```
1.
Представим что мы создаем приложение для прохождения каких-либо тестов.

Описать схему базы данных для этого приложения (таблицы и связи)

Какие будут таблицы - тесты, вопросы, варианты ответа, пользователи, ответы пользователей. Придумать поля у каждой таблицы. 
Пользователь может отвечать на вопрос один раз. 
Правильный вариант ответа только один.

2*
Не представляем приложение, а пишем.
Необходимо написать консольное приложения для тестирования пользователя.
Данные хранить в бд из задачи 1.
```

# Lesson 13 20/03/2019
### Documentation
- https://docs.sqlalchemy.org/en/latest/ - дока по алхимии
- https://www.datacamp.com/courses/introduction-to-relational-databases-in-python?tap_a=5644-dce66f&tap_s=128604-f35052 - курс по алхимии
- https://ru.wikipedia.org/wiki/HTTP - что такое http
- https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BA%D0%B8_HTTP
- https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B7%D0%B0%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BA%D0%BE%D0%B2_HTTP - список заголовков

### homework
1. Переписать sql с homework12 на SqlAlchemy
