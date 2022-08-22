-- users 테이블 생성
CREATE TABLE users (
  id INT PRIMARY KEY,
  name TEXT,
  role_id INT
);

INSERT INTO users VALUES
  (1, '관리자', 1),
  (2, '김철수', 2),
  (3, '이영희', 2);

-- role 테이블 생성
CREATE TABLE role (
  id INT PRIMARY KEY,
  title TEXT
);

INSERT INTO role VALUES
  (1, 'admin'),
  (2, 'staff'),
  (3, 'student');

-- articles 테이블 생성
CREATE TABLE articles (
  id INT PRIMARY KEY,
  title TEXT,
  content TEXT,
  user_id INT
);

INSERT INTO articles VALUES 
  (1, '1번글', '111', 1),
  (2, '2번글', '222', 2),
  (3, '3번글', '333', 1),
  (4, '4번글', '444', NULL);


-- 1. 사용자와 각각의 역할 출력
SELECT *
FROM users INNER JOIN role
ON users.role_id = role.id;

-- 2. staff 사용자를 역할과 함께 출력
SELECT *
FROM users INNER JOIN role
ON users.role_id = role.id
WHERE role.id = 2;

-- 3. 사용자와 각각의 역할을 이름의 내림차순으로 출력
SELECT *
FROM users INNER JOIN role
ON users.role_id = role.id
ORDER BY users.name DESC;

-- 4. 모든 게시글을 사용자 정보와 함께 출력
SELECT *
FROM articles LEFT OUTER JOIN users
ON articles.user_id = users.id;

-- 4. 작성자가 있는 모든 게시글을 사용자 정보와 함께 출력
SELECT *
FROM articles LEFT OUTER JOIN users
ON articles.user_id = users.id
WHERE articles.user_id IS NOT NULL;

-- 5. 모든 게시글과 모든 사용자 정보 출력
SELECT *
FROM articles FULL OUTER JOIN users
ON articles.user_id = users.id;

-- 6. users와 role의 CROSS JOIN 결과 출력
SELECT *
FROM users CROSS JOIN role;