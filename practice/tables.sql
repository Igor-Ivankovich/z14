CREATE DATABASE db_z14;
\c db_z14;


CREATE TABLE customer (
  id SERIAL PRIMARY KEY,
  name VARCHAR (100) NOT NULL,
  email VARCHAR (100) UNIQUE
);

-- ALTER TABLE customer ADD COLUMN age SMALLINT ;
-- ALTER TABLE customer DROP COLUMN age;
-- ALTER TABLE customer ALTER COLUMN email TYPE VARCHAR (50);

CREATE TABLE product (
  id SERIAL PRIMARY KEY,
  name VARCHAR (100) NOT NULL,
  price NUMERIC
);

CREATE TABLE purchase (
  id SERIAL PRIMARY KEY,
  customer_id INTEGER REFERENCES customer(id),
  datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE purchase_journal (
  purchase_id INTEGER REFERENCES purchase(id),
  product_id INTEGER REFERENCES product(id),
  count INTEGER CHECK (count >= 0),
  PRIMARY KEY (purchase_id, product_id)
);

SELECT * FROM customer;
SELECT email,name FROM customer;
SELECT * FROM customer LIMIT 2;
SELECT * FROM customer LIMIT 2 OFFSET 3;

INSERT INTO customer (name, email) VALUES
('Bill', 'email'),
('Tim', 'email2'),
('Alex', 'email3@gmail.com'),
('Kolya', 'email4@mail.ru'),
('Steve', 'email5@gmail.com');

SELECT * FROM customer WHERE id > 4;
SELECT * FROM customer WHERE email='email';
SELECT * FROM customer WHERE email LIKE '%gmail.com';
SELECT * FROM customer WHERE email LIKE '%gmail.com' AND id>1;
SELECT * FROM customer WHERE email LIKE '%gmail.com' AND id>1 LIMIT 1 OFFSET 1;

UPDATE customer SET name='Nikolay' WHERE name='Kolya';

DELETE FROM customer WHERE id=1;
TRUNCATE customer;

INSERT INTO purchase (customer_id) VALUES (3), (4), (5);

SELECT customer.name,purchase.datetime FROM purchase
  JOIN customer ON purchase.customer_id=customer.id;

SELECT customer.name,purchase.datetime FROM purchase
  RIGHT JOIN customer ON purchase.customer_id=customer.id;

SELECT customer.name,purchase.datetime FROM customer
  LEFT JOIN purchase ON purchase.customer_id=customer.id;

SELECT customer.name,purchase.datetime FROM customer
  LEFT JOIN purchase ON purchase.customer_id=customer.id WHERE purchase.datetime IS NULL;