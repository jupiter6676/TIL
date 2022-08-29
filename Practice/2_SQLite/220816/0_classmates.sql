-- SQLite
CREATE TABLE classmates (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

-- rowid
INSERT INTO classmates VALUES (1, '홍길동', 30, '서울');
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 30, '서울');

SELECT rowid, * FROM classmates;

-- CREATE
INSERT INTO classmates VALUES
('홍길동', 30, '서울'),
('김철수', 30, '제주'),
('이호영', 26, '인천'),
('박민희', 29, '대구'),
('최혜영', 28, '전주')

-- READ
SELECT rowid, name FROM classmates;
SELECT rowid, name FROM classmates LIMIT 1;
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
SELECT * FROM classmates WHERE address='서울';
SELECT DISTINCT age FROM classmates;