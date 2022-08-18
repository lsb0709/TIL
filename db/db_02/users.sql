-- SQLite
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

.mode csv
.import users.csv users
.tables

SELECT * FROM users WHERE age >= 30;

SELECT first_name FROM users WHERE age >= 30;

SELECT age, first_name FROM users WHERE age >= 30 and last_name = '김';

SELECT COUNT(*) FROM users;

SELECT AVG(age) FROM users WHERE age >= 30;

SELECT first_name, MAX(balance) FROM users;

SELECT AVG(balance) FROM users WHERE age >= 30;

SELECT * FROM users WHERE age LIKE '2_';

SELECT * FROM users WHERE phone LIKE '02-%';

SELECT * FROM users WHERE first_name LIKE '%준';

SELECT * FROM users WHERE phone LIKE '%-5114-%';

SELECT * FROM users ORDER BY age ASC LIMIT 10;

SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;

SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10; 