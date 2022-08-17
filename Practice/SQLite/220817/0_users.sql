CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

SELECT * FROM users WHERE age >= 30;
SELECT first_name FROM users WHERE age >= 30;
SELECT first_name, age FROM users WHERE age >= 30 AND last_name = '김';

-- 집계 함수
SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users WHERE age >= 30;
SELECT *, MAX(balance) FROM users;
SELECT AVG(balance) FROM users WHERE age >= 30;

-- LIKE
SELECT * FROM users WHERE age LIKE '2_';
SELECT * FROM users WHERE phone LIKE '02-%';
SELECT * FROM users WHERE first_name LIKE '%준';
SELECT * FROM users WHERE phone LIKE '%-5114-%';

-- ORDER BY
SELECT * FROM users ORDER BY age ASC LIMIT 10;
SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;
SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;