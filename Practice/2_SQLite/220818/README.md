# 3일차 실습

## 사전 확인

### 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

### Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

### table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
CREATE TABLE healthcare (
    id PRIMARY KEY,        
    sido INTEGER NOT NULL, 
    gender INTEGER NOT NULL,
    age INTEGER NOT NULL,  
    height INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    waist REAL NOT NULL,   
    va_left REAL NOT NULL, 
    va_right REAL NOT NULL,

    blood_pressure INTEGER 
    NOT NULL,
    smoking INTEGER NOT NULL,
    is_drinking BOOLEAN NOT NULL
);
```

## 문제

###  1. 흡연 여부(smoking)로 구분한 각 그룹의 컬럼명과 그룹의 사람의 수를 출력하시오.

```sql 
SELECT smoking, COUNT(*) FROM healthcare
GROUP BY smoking
HAVING smoking != '';
```

```sql
SELECT smoking, COUNT(*) FROM healthcare
WHERE smoking != ''
GROUP BY smoking;
```

```
smoking  COUNT(*)
-------  --------
1        626138
2        189808
3        183711
```



###  2. 음주 여부(is_drinking)로 구분한 각 그룹의 컬럼명과 그룹의 사람의 수를 출력하시오.

```sql 
SELECT is_drinking, COUNT(*) FROM healthcare
GROUP BY is_drinking
HAVING is_drinking != '';
```

```sql
SELECT is_drinking, COUNT(*) FROM healthcare
WHERE is_drinking != ''
GROUP BY is_drinking;
```

```
is_drinking  COUNT(*)
-----------  --------
0            415119
1            584685
```



### 3. 음주 여부로 구분한 각 그룹에서 혈압(blood_pressure)이 200 이상인 사람의 수를 출력하시오.✨

```sql
SELECT is_drinking, COUNT(*) FROM healthcare 
WHERE blood_pressure > 200 AND blood_pressure != ''
GROUP BY is_drinking;
```

```
is_drinking  COUNT(*)
-----------  --------
0            92
1            120
```



### 4. 시도(sido)에 사는 사람의 수가 50000명 이상인 시도의 코드와 그 시도에 사는 사람의 수를 출력하시오.✨

```sql
SELECT sido, COUNT(*) FROM healthcare
GROUP BY sido
HAVING COUNT(*) >= 50000;
```

```
sido  COUNT(*)
----  --------
11    166231
26    69025
28    58345
41    247369
47    54438
48    68530
```



### 5. 키(height)를 기준으로 구분하고, 각 키와 사람의 수를 출력하시오.✨

> 단, 사람의 수를 기준으로 내림차순으로 5개까지 출력하시오.

```sql
SELECT height, COUNT(*) FROM healthcare
GROUP BY height
ORDER BY COUNT(*) DESC LIMIT 5;
```

```
height  COUNT(*)
------  --------
160     184993
155     181306
165     179352
170     152585
150     128555
```



### 6. 키(height)와 몸무게(weight)를 기준으로 구분하고, 몸무게와, 키, 해당 그룹의 사람의 수를 출력하시오. 

> 단, 사람의 수를 기준으로 내림차순 5개까지 출력하시오.

```sql
SELECT weight, height, COUNT(*) FROM healthcare
GROUP BY height, weight
LIMIT 5;
```

```
weight  height  COUNT(*)
------  ------  --------
30      130     60
35      130     99
40      130     83
45      130     76
50      130     35
```



### 7. 음주 여부에 따라 평균 허리 둘레(waist)와 사람의 수를 출력하시오.

```sql 
SELECT is_drinking, AVG(waist), COUNT(*) FROM healthcare
WHERE is_drinking != ''
GROUP BY is_drinking;
```

```
is_drinking  AVG(waist)        COUNT(*)
-----------  ----------------  --------
0            81.2128249971711  415119
1            83.1541594191841  584685
```



### 8. 각 성별(gender)의 평균 왼쪽 시력(va_left)과 평균 오른쪽 시력(va_right)를 출력하시오.

> 단, 평균 왼쪽 시력과 평균 오른쪽 시력의 컬럼명을 '평균 왼쪽 시력' '평균 오른쪽 시력'로 표시하고, 평균 시력은 소수점 둘째 자리까지 출력하시오.

```sql
SELECT
  gender,
  ROUND(AVG(va_left), 2) AS '평균 왼쪽 시력',
  ROUND(AVG(va_right), 2) AS '평균 오른쪽 시력'
FROM healthcare
WHERE va_left != '' AND va_right != ''
GROUP BY gender;
```

```
gender  평균 왼쪽 시력  	평균 오른쪽 시력
------  --------  		---------
1       0.98      		0.99
2       0.88      		0.88
```



### 9. 각 나이대(age)의 평균 키와 평균 몸무게를 출력하시오.

> 단, 평균 키와 평균 몸무게의 컬럼명을 '평균 키' '평균 몸무게'로 표시하고, 평균키가 160 이상 평균 몸무게가 60 이상인 데이터만 출력하시오.

```sql
SELECT
  age,
  AVG(height) AS '평균 키',
  AVG(weight) AS '평균 몸무게'
FROM healthcare
WHERE height >= 160 AND weight >= 60
GROUP BY age;
```

```
age  평균 키              평균 몸무게
---  ----------------  ----------------
9    170.073317084153  74.6230875400112
10   169.013565369597  72.955825591311
11   167.877275577439  71.5467245047953
12   166.925936123348  70.1916299559471
13   166.169523057842  69.4060773480663
14   165.430575579461  68.8058666962404
15   164.935418953531  68.1024515184779
16   164.667795726941  67.4339933993399
17   164.377547554348  67.0134171195652
18   163.844580777096  65.4754601226994
```



### 10. 음주 여부(is_drinking)와 흡연 여부(smoking)에 따른 평균 BMI를 출력하시오.

> 단, 음주 여부 또는 흡연 여부가 공백이 아닌 행만 사용하세요.

```sql
SELECT
  is_drinking,
  smoking,
  AVG(weight / (height * height * 0.0001)) AS '평균 BMI'
FROM healthcare
WHERE is_drinking != '' AND smoking != ''
GROUP BY is_drinking, smoking;
```

```
is_drinking  smoking  평균 BMI
-----------  -------  ----------------
0            1        23.8724603942955
0            2        24.6073677352564
0            3        24.3193273448558
1            1        23.9341328992508
1            2        25.0333550564281
1            3        24.6363247421328
```



### 11. 자유

> 음주 여부(is_drinking)와 흡연 여부(smoking)에 따른 평균 BMI이 24 이상인 것만 출력

```sql
SELECT
  is_drinking,
  smoking,
  AVG(weight / (height * height * 0.0001)) AS 평균BMI
FROM healthcare
WHERE is_drinking != '' AND smoking != ''
GROUP BY is_drinking, smoking
HAVING 평균BMI >= 24;
```

```
is_drinking  smoking  평균BMI
-----------  -------  ----------------
0            2        24.6073677352564
0            3        24.3193273448558
1            2        25.0333550564281
1            3        24.6363247421328
```