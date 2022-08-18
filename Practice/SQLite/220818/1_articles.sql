CREATE TABLE articles (
  title TEXT NOT NULL,
  content TEXT NOT NULL
);

INSERT INTO articles VALUES ('1번 제목', '1번 내용');

ALTER TABLE articles RENAME TO news;

ALTER TABLE news ADD COLUMN created_at TEXT;
INSERT INTO news (title, content) VALUES ('2번 제목', '2번 내용');
INSERT INTO news VALUES ('3번 제목', '3번 내용', datetime('now'));

ALTER TABLE news ADD COLUMN subheading TEXT DEFAULT '소제목';
INSERT INTO news VALUES ('4번 제목', '4번 내용', datetime('now'), '4번 소제목');