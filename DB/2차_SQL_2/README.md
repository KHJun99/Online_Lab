# SQL 기초 (2)

## 주요 개념

### 1. 데이터 조작
- **INSERT**: 데이터 추가
- **UPDATE**: 데이터 수정
- **DELETE**: 데이터 삭제

### 2. 집계 함수
- **COUNT()**: 개수
- **SUM()**: 합계
- **AVG()**: 평균
- **MAX()**: 최대값
- **MIN()**: 최소값

### 3. GROUP BY
- **그룹화**: 특정 컬럼 기준 그룹화
- **HAVING**: 그룹 조건

## 예시 코드

### INSERT
```sql
-- 데이터 추가
INSERT INTO users (name, email, age)
VALUES ('홍길동', 'hong@example.com', 25);

-- 여러 행 추가
INSERT INTO users (name, email, age)
VALUES
  ('김철수', 'kim@example.com', 30),
  ('이영희', 'lee@example.com', 28);
```

### UPDATE
```sql
-- 데이터 수정
UPDATE users
SET age = 26
WHERE name = '홍길동';

-- 여러 컬럼 수정
UPDATE users
SET age = 26, email = 'new@example.com'
WHERE id = 1;
```

### DELETE
```sql
-- 데이터 삭제
DELETE FROM users
WHERE id = 1;

-- 조건부 삭제
DELETE FROM users
WHERE age < 18;
```

### 집계 함수
```sql
-- 개수
SELECT COUNT(*) FROM users;
SELECT COUNT(DISTINCT city) FROM users;

-- 합계, 평균
SELECT SUM(price) FROM orders;
SELECT AVG(age) FROM users;

-- 최대, 최소
SELECT MAX(price) FROM products;
SELECT MIN(created_at) FROM articles;
```

### GROUP BY
```sql
-- 그룹화
SELECT city, COUNT(*) as user_count
FROM users
GROUP BY city;

-- HAVING 조건
SELECT city, COUNT(*) as user_count
FROM users
GROUP BY city
HAVING COUNT(*) >= 5;
```

## 기본 코드 템플릿

### CRUD 기본
```sql
-- Create
INSERT INTO table_name (column1, column2)
VALUES (value1, value2);

-- Read
SELECT * FROM table_name;

-- Update
UPDATE table_name
SET column1 = value1
WHERE condition;

-- Delete
DELETE FROM table_name
WHERE condition;
```
