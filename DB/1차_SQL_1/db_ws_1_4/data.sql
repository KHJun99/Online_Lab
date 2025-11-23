-- 전체 사용자의 평균 age를 구하시오
SELECT AVG(age) AS average_age
FROM users;

-- 각 country 별로 사용자 수를 구하시오
SELECT country, count(*) as user_count
FROM users
GROUP BY country

-- balance가 가장 많은 사용자의 정보 중, 가장 먼저 조회되는 한 명의 정보만 조회
SELECT *
FROM users
ORDER BY balance DESC
LIMIT 1;

-- 각 country별로 평균 balance를 구하시오
SELECT country, AVG(balance) as avg_balance
FROM users
GROUP BY country;

-- balance가 가장 많은 사용자와 가장 적은 사용자의 balance 차이를 구하시오.
SELECT MAX(balance) - MIN(balance) AS balance_difference
FROM users;