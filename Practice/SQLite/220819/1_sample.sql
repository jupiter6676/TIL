-- 3.
SELECT * FROM albums ORDER BY Title DESC LIMIT 5;

-- 4.
SELECT COUNT(*) AS '고객 수' FROM customers;

-- 5.
SELECT FirstName AS 이름, LastName AS 성
FROM customers
WHERE Country = 'USA'
ORDER BY FirstName DESC
LIMIT 5;

SELECT * FROM customers
WHERE Country = 'USA';

-- 6.
SELECT COUNT(*) AS 송장수 FROM invoices
WHERE BillingPostalCode IS NOT NULL;

-- 7.
SELECT * FROM invoices
WHERE BillingPostalCode IS NULL
ORDER BY InvoiceDate DESC LIMIT 5;

-- 8.
SELECT COUNT(*) FROM invoices
WHERE strftime('%Y', InvoiceDate) = '2013';

-- 9.
SELECT
  CustomerId AS 고객ID,
  FirstName AS 이름,
  LastName AS 성
FROM customers
WHERE SUBSTR(FirstName, 1, 1) = 'L'
ORDER BY CustomerId;

-- 10.
SELECT
  COUNT(*) AS '고객 수',
  Country AS '나라'
FROM customers
GROUP BY Country
ORDER BY COUNT(*) DESC LIMIT 5;

-- 11.
SELECT ArtistId, COUNT(*) AS '앨범 수'
FROM albums
GROUP BY ArtistId
ORDER BY COUNT(*) DESC LIMIT 1;

-- 12.
SELECT ArtistId, COUNT(*) AS '앨범 수'
FROM albums
GROUP BY ArtistId
HAVING COUNT(*) >= 10
ORDER BY COUNT(*) DESC;

-- 13.
SELECT COUNT(*), Country, State
FROM customers
WHERE State IS NOT NULL
GROUP BY Country, State
ORDER BY COUNT(*) DESC, Country DESC LIMIT 5;

-- 14.
SELECT
  CustomerId,
  CASE
    WHEN Fax IS NULL THEN 'X'
    ELSE 'O'
  END AS 'FAX 유/무'
FROM customers
ORDER BY CustomerId LIMIT 5;

-- 15.
SELECT
  LastName, FirstName,
  CAST(strftime('%Y', date('now')) AS INT)
  - CAST(strftime('%Y', BirthDate) AS INT) + 1 AS 나이
FROM employees
ORDER BY EmployeeId;

-- 16.
-- 앨범 수가 가장 많은 ArtistId와, 그 사람의 앨범 수
SELECT ArtistId, COUNT(*) AS '앨범 수'
FROM albums
GROUP BY ArtistId
ORDER BY COUNT(*) DESC LIMIT 1;

-- 앨범 수가 가장 많은 ArtistId에 해당하는 사람의 이름
SELECT ArtistId, Name FROM artists
WHERE ArtistId = (
  SELECT ArtistId
  FROM albums
  GROUP BY ArtistId
  ORDER BY COUNT(*) DESC LIMIT 1
);

-- 17.
SELECT GenreId, COUNT(*) FROM tracks
GROUP BY GenreId
ORDER BY COUNT(*) LIMIT 1;

SELECT Name FROM genres
WHERE GenreId = 25;

SELECT GenreId, Name FROM genres
WHERE GenreId = (
  SELECT GenreId FROM tracks
  GROUP BY GenreId
  ORDER BY COUNT(*) LIMIT 1
);

-- 18. 자유
SELECT
  ArtistId,
  Name,
  (SELECT MAX(mycount)
   FROM (SELECT COUNT(*) AS mycount FROM albums GROUP BY ArtistId))
   AS '앨범 수'
FROM artists
WHERE ArtistId = (
  SELECT ArtistId
  FROM albums
  GROUP BY ArtistId
  ORDER BY COUNT(*) DESC LIMIT 1
);