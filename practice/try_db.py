import psycopg2

connection = psycopg2.connect(
    # 'postgres://<db_user>:<db_password>@<db_host>:<db_port>/<db_name>'
    dsn='postgres://postgres:postgres@localhost:5432/db_z14'
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM customer;")

result = cursor.fetchall()
print(result)

items = []
for i in range(100):
    user_name = f'User_{i}'
    email = f'email_{i}@gmail.com'
    items.append(f"('{user_name}', '{email}')")

cursor.execute(f"""
INSERT INTO customer (name, email)
VALUES {','.join(items)};
""")

connection.commit()

connection.close()


