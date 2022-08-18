-- 문자열 함수
SELECT phone, SUBSTRING(phone, -4) AS '전화번호 뒤 4자리' FROM users;
SELECT country, LENGTH(country) FROM users;
SELECT phone, REPLACE(phone, '-', ' ') FROM users;
SELECT last_name || first_name AS '이름' FROM users;

-- GROUP BY
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
SELECT last_name, COUNT(*) FROM users GROUP BY last_name HAVING age >= 40;