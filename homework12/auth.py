import psycopg2
from hashlib import md5

connection = psycopg2.connect(
    dsn='postgres://postgres:postgres@localhost:5432/testing'
)
cursor = connection.cursor()


def hash_password(password):
    return md5(password.encode()).hexdigest()


print('1. Login')
print('2. Register')

answer = int(input('> '))

username = input('username? ')
password = hash_password(input('password? '))

if answer == 1:
    query = "SELECT password FROM users WHERE username='%s';"
    cursor.execute(query, username)
    result = cursor.fetchall()
    if not result:
        print('NOT FOUND')
        exit()
    db_password = result[0][0]

    if password == db_password:
        print('OK')
    else:
        print('BAD PASSWORD')
    exit()

if answer == 2:
    cursor.execute(f"""
      INSERT INTO users (username, password) VALUES
      ('{username}', '{password}');
    """)
    connection.commit()
    print('REGISTRED!')

connection.close()