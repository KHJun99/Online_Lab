-- ERD를 참고하여 zoo.sqlite3에 zoo 테이블 생성
CREATE TABLE zoo (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  eat TEXT,
  weight INT,
  height INT,
  age INT
);

-- zoo 테이블에 최소 4개 이상의 데이터 삽입
INSERT INTO zoo (name, eat, weight, height, age)
VALUES
    ('Lion', 'Meat', '200', '120', '5'),
    ('Elephant', 'Plnats', '5000', '300', '15'),
    ('Giraffe', 'Leaves', '1500', '550', '10'),
    ('Monkey', 'Fruits', '50', '60', '8');


-- zoo 테이블의 모든 데이터를 조회하여 출력
SELECT *
FROM zoo
