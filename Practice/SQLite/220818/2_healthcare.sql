-- 1
SELECT smoking, COUNT(*) FROM healthcare
WHERE smoking != ''
GROUP BY smoking;

-- 2
SELECT is_drinking, COUNT(*) FROM healthcare
WHERE is_drinking != ''
GROUP BY is_drinking;

-- 3 (HAVING X, WHERE O)
SELECT is_drinking, COUNT(*) FROM healthcare
WHERE is_drinking != '' AND blood_pressure != ''
GROUP BY is_drinking HAVING blood_pressure > 200;

SELECT is_drinking, COUNT(*) FROM healthcare 
WHERE blood_pressure > 200 AND blood_pressure != ''
GROUP BY is_drinking;

-- 4
SELECT sido, COUNT(*) FROM healthcare
GROUP BY sido
HAVING COUNT(*) >= 50000;

-- 5
SELECT height, COUNT(*) FROM healthcare
GROUP BY height
ORDER BY COUNT(*) DESC LIMIT 5;

-- 6
SELECT weight, height, COUNT(*) FROM healthcare
GROUP BY height, weight
LIMIT 5;

-- 7
SELECT is_drinking, AVG(waist), COUNT(*) FROM healthcare
WHERE is_drinking != ''
GROUP BY is_drinking;

-- 8
SELECT
  gender,
  ROUND(AVG(va_left), 2) AS '평균 왼쪽 시력',
  ROUND(AVG(va_right), 2) AS '평균 오른쪽 시력'
FROM healthcare
WHERE va_left != '' AND va_right != ''
GROUP BY gender;

-- 9
SELECT
  age,
  AVG(height) AS '평균 키',
  AVG(weight) AS '평균 몸무게'
FROM healthcare
WHERE height >= 160 AND weight >= 60
GROUP BY age;

-- 10
SELECT
  is_drinking,
  smoking,
  AVG(weight / (height * height * 0.0001)) AS '평균 BMI'
FROM healthcare
WHERE is_drinking != '' AND smoking != ''
GROUP BY is_drinking, smoking;

-- 11. 자유
SELECT
  is_drinking,
  smoking,
  AVG(weight / (height * height * 0.0001)) AS '평균 BMI'
FROM healthcare
WHERE is_drinking != '' AND smoking != ''
GROUP BY is_drinking, smoking
HAVING '평균 BMI' > 24;