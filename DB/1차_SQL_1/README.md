# SQL 기초 (1)

## 주요 개념

### 1. SQL이란?
- **Structured Query Language**: 구조화된 쿼리 언어
- **데이터베이스 관리**: 데이터 조작 및 정의
- **RDBMS**: 관계형 데이터베이스 관리 시스템

### 2. 기본 명령어
- **SELECT**: 데이터 조회
- **FROM**: 테이블 지정
- **WHERE**: 조건 지정
- **ORDER BY**: 정렬

## 예시 코드

### 기본 조회
```sql
-- 모든 데이터 조회
SELECT * FROM users;

-- 특정 컬럼 조회
SELECT name, email FROM users;

-- 조건부 조회
SELECT * FROM users WHERE age >= 20;

-- 정렬
SELECT * FROM users ORDER BY name ASC;
SELECT * FROM users ORDER BY created_at DESC;
```

### WHERE 조건
```sql
-- 비교 연산자
SELECT * FROM products WHERE price > 10000;
SELECT * FROM products WHERE price <= 50000;

-- 논리 연산자
SELECT * FROM products WHERE price >= 10000 AND price <= 50000;
SELECT * FROM products WHERE category = 'electronics' OR category = 'books';

-- LIKE (패턴 매칭)
SELECT * FROM users WHERE name LIKE '김%';  -- 김으로 시작
SELECT * FROM users WHERE email LIKE '%@gmail.com';  -- @gmail.com으로 끝
```

## 기본 코드 템플릿

### SELECT 기본
```sql
-- 기본 조회
SELECT column1, column2 FROM table_name;

-- 조건 조회
SELECT * FROM table_name
WHERE condition;

-- 정렬
SELECT * FROM table_name
ORDER BY column_name ASC|DESC;

-- 제한
SELECT * FROM table_name
LIMIT 10;
```
