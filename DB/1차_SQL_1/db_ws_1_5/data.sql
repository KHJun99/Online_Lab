-- Active: 1762829274058@@127.0.0.1@3306
-- age가 30세 이상이면서 balance가 1000 이상인 사용자들의 정보를 조회
SELECT *
FROM users
WHERE
  age >= 30 AND balance >= 1000;

-- balance가 1000 이하인 사용자들 중에서 age가 20세 이하인 사용자의 정보를 조회
SELECT *
FROM users
WHERE
  balance <= 1000 AND age <= 20;

-- first_name이 '현'으로 시작하고 country가 '제주특별자치도'인 사용자들 중에서 가장 age가 많은 사용자의 정보를 조회
SELECT *
FROM users
WHERE
  first_name LIKE '현%'
  AND
  country = '제주특별자치도'
ORDER BY
  age DESC
LIMIT
  1;

-- last_name이 '박'이고 age가 25세 이상인 사용자들 중에서 가장 age가 어린 사용자 정보 조회
SELECT *
FROM users
WHERE
  last_name = '박'
  AND
  age >= 25
ORDER BY
  age ASC
LIMIT
  1;

-- first_name이 '재은'이거나 '영일'인 사용자들중에서 balance가 가장 많은 사용자의 정보 조회
SELECT *
FROM users
WHERE
  first_name = '재은'
  OR
  first_name = '영일'
ORDER BY
  balance DESC
LIMIT
  1;

-- 각 country별로 가장 많은 balance를 가진 사용자의 정보를 조회하고 balance를 내림차순 정렬
SELECT u.*
FROM users u
WHERE u.balance = (
  SELECT MAX(u2.balance)
  FROM users u2
  WHERE u2.country = u.country
)
ORDER BY u.balance DESC;

-- age가 30세 이상이면서, balance가 age가 30세 이상인 사용자들의 평균 balance보다 높은 사용자 정보 조회
SELECT u.*
FROM users u
WHERE
  u.age >= 30 AND
  u.balance > (
    SELECT AVG(u2.balance)
    FROM users u2
    WHERE age >= 30
  )
