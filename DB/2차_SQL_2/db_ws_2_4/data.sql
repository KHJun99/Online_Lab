-- Active: 1762849215212@@127.0.0.1@3306
-- transactions 테이블 생성
CREATE TABLE transactions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  amount TEXT,
  transaction_date DATE,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

-- transactions 테이블에 최소 4개 이상의 데이터를 삽입한다.
INSERT INTO transactions (user_id, amount, transaction_date)
VALUES
  (1, '500', '2024-03-15'),
  (2, '700', '2024-03-16'),
  (1, '200', '2024-03-17'),
  (3, '1000', '2024-03-18');

-- user테이블의 각 user별 first_name, last_name, amount, transaction_date 조회
SELECT
  u.first_name,
  u.last_name,
  t.amount,
  t.transaction_date
FROM transactions t
INNER JOIN users u ON t.user_id = u.id;


-- user테이블의 각 user별 first_name, last_name, amount, transaction_date 조회
-- 거래일자가 '2024-03-16' 이후인 데이터만
SELECT
  u.first_name,
  u.last_name,
  t.amount,
  t.transaction_date
FROM transactions t
INNER JOIN users u ON t.user_id = u.id
WHERE t.transaction_date > '2024-03-16';

-- users 테이블의 각 user별 first_name, last_name, 총 거래량 (total_amount) 조회
-- user id를 기준으로 그룹화하여 해당 user의 amount 총 량을 출력할 수 있어야 한다.
SELECT
  u.first_name,
  u.last_name,
  SUM(t.amount) AS 'total_amount'
FROM transactions t
INNER JOIN users u ON t.user_id = u.id
GROUP BY u.id, u.first_name, u.last_name;