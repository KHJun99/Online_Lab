# age가 18세 미만인 유저를 age 기준으로 내림차순으로 정렬하여 조회
SELECT *
FROM users
WHERE
  age < 18
ORDER BY
  age DESC;

# age가 18세 미만인 유저의 last_name과 age 필드만 출력
# last_name 기준으로 우선 오른차순, last_name 이 같은 경우 age 기준 내림차순 정렬
SELECT last_name, age
FROM users
WHERE
  age < 18
ORDER BY
  last_name, age DESC;

# 2번과 동일한 조회흘 하되, last_name과 age가 동일한 중복 데이터를 제외하고 조회
SELECT DISTINCT last_name, age 
FROM users
WHERE
  age < 18
ORDER BY
  last_name, age DESC;
