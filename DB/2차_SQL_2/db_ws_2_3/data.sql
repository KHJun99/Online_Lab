-- Active: 1762846732948@@127.0.0.1@3306
-- hotels 테이블의 전체 데이터 조회
SELECT * FROM hotels

-- grades 필드의 값으 모두 대문자로 수정
UPDATE hotels
SET grade = upper(grade)

-- 수정된 전체 데이터의 grade 필드의 값만 조회
SELECT "grade"
FROM hotels

-- customers 테이블을 생성
CREATE TABLE customers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  email TEXT
)

-- reservations 테이블 생성
CREATE TABLE reservations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id INTEGER NOT NULL,
  room_num INTEGER NOT NULL,
  check_in TEXT NOT NULL,
  checi_out TEXT NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customers(id),
  FOREIGN KEY (room_num) REFERENCES rooms(room_num)
)

-- 고객 정보와 예약정보를 각각 최소 4개 이상 삽입한다.
INSERT INTO customers (name, email)
VALUES
  ('홍길동', 'john@example.com'),
  ('박지영', 'jane@esample.com'),
  ('김미영', 'alice@example.com'),
  ('이철수', 'bob@example.com')

INSERT INTO reservations (customer_id, room_num, check_in, check_out)
VALUES
  ('1', '101', '2024-03-20', '2024-03-25'),
  ('2', '202', '2024-03-21', '2024-03-24'),
  ('3', '303', '2024-03-22', '2024-03-26'),
  ('4', '404', '2024-03-23', '2024-03-27')

-- customers 테이블의 전체 데이터 조회
SELECT * FROM customers

-- reservations 테이블의 전체 데이터 조회
SELECT * FROM reservations
