SELECT COUNT(*) FROM healthcare;

SELECT MAX(age), MIN(age) FROM healthcare;
SELECT MAX(height), MIN(height), MAX(weight), MIN(weight) FROM healthcare;

SELECT COUNT(*) FROM healthcare WHERE height BETWEEN 160 AND 170;
SELECT * FROM healthcare ORDER BY blood_pressure DESC LIMIT 5;

-- waist 속 빈 칸은 사실 NULL 값이 아닌 건가??
-- NULL이 아니라 ''였다...
SELECT waist FROM healthcare WHERE waist != '' AND is_drinking = 1 ORDER BY waist DESC LIMIT 5;

SELECT COUNT(*) FROM healthcare WHERE (va_left >= 1.5 AND va_right >= 1.5) AND is_drinking = 1;

SELECT COUNT(*) FROM healthcare WHERE blood_pressure < 120;
SELECT AVG(waist) FROM healthcare WHERE blood_pressure >= 140;
SELECT AVG(height), AVG(weight) FROM healthcare WHERE gender = 1;

-- 키 먼저 내림차순, 몸무게 내림차순
-- 그 후 두 번째 값을 출력
SELECT height, weight FROM healthcare ORDER BY height DESC, weight DESC LIMIT 1 OFFSET 1;

SELECT COUNT(*) FROM healthcare WHERE weight / (height * height * 0.0001) >= 30;
SELECT id, weight / (height * height * 0.0001) AS BMI FROM healthcare WHERE smoking = 3 ORDER BY weight / (height * height * 0.0001) DESC LIMIT 5;

-- 자유
SELECT gender, height, weight FROM healthcare WHERE va_left = '' AND va_right = '' AND age LIKE '%3' LIMIT 5;

SELECT id, blood_pressure,
  CASE WHEN blood_pressure <= 90 THEN '저혈압'
  WHEN blood_pressure < 120 THEN '정상'
  ELSE '고혈압'
  END
  AS '혈압 상태'
  FROM healthcare WHERE blood_pressure != '' LIMIT 5;
