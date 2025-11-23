-- Active: 1762880021826@@127.0.0.1@3306
-- orders 테이블을 생성
CREATE TABLE orders (
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_date DATE,
  total_amount REAL
);

-- orders 테이블에 서로 다른 데이터 최소 3개 이상 삽입
INSERT INTO orders (order_date, total_amount)
VALUES
  ('2023-07-15', 50.99),
  ('2023-07-16', 75.5),
  ('2023-07-17', 30.25);

-- customers 테이블을 생성
CREATE TABLE customers (
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  email TEXT,
  phone TEXT
);

-- customers 테이블에 서로 다른 데이터를 최소 3개 이상 삽입
INSERT INTO customers (name, email, phone)
VALUES
  ('허균', 'hong.gildong@example.com', '010-1234-5678'),
  ('김영희', 'kim.younghee@example.com', '010-9876-5432'),
  ('이철수', 'lee.cheolsu@example.com', '010-5555-4444');

-- orders의 3번째 레코드를 삭제
DELETE FROM orders
WHERE order_id = 3;

-- customers의 1번째 레코드의 name을 '홍길동'으로 수정
UPDATE customers
SET name = '홍길동'
WHERE customer_id = 1;

-- orders와 customers의 모든 데이터 조회
SELECT *
FROM orders;

SELECT *
FROM customers;