-- CASE
SELECT
  age,
  CASE
    WHEN age <= 18 THEN '청소년'
    WHEN age <= 30 THEN '청년'
    WHEN age <= 64 THEN '중장년'
  END
FROM users LIMIT 5;

-- 1. 단일행 서브쿼리
SELECT COUNT(*) FROM users
WHERE age = (SELECT MIN(age) FROM users);

SELECT COUNT(*) FROM users
WHERE balance > (SELECT AVG(balance) FROM users);

SELECT COUNT(*) FROM users
WHERE country = (
  SELECT country
  FROM users
  WHERE last_name = '유' AND first_name = '은정'
);

SELECT
  (SELECT COUNT(*) FROM users) AS 총인원,
  (SELECT AVG(balance) FROM users) AS 평균연봉,
  (SELECT AVG(age) FROM users) AS 평균나이
;

-- 2. 다중행 서브쿼리
SELECT country FROM users
WHERE last_name = '이' AND first_name = '은정';

SELECT COUNT(*) FROM users
WHERE country IN (
  SELECT country FROM users
  WHERE last_name = '이' AND first_name = '은정'
);

-- 3. 다중칼럼 서브쿼리
SELECT
  last_name,
  MIN(age)
FROM users
GROUP BY last_name;

SELECT
  last_name,
  first_name,
  age
FROM users
WHERE (last_name, age) IN (
  SELECT last_name, MIN(age) FROM users
  GROUP BY last_name
)
ORDER BY last_name, age;