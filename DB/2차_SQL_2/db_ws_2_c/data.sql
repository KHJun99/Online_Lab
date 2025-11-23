-- Active: 1762838284732@@127.0.0.1@3306
-- "BillingCountry"를 기준으로 그룹화하고, 각 나라별 총 판매액을 계산하여 조회
SELECT "BillingCountry", SUM("Total") AS "TotalSales"
FROM invoices
GROUP BY "BillingCountry";

--"InvoiceDate"를 연도별로 그룹화하고, 각 연도별 총판매액을 계산하여 조회
SELECT
  -- STRFTIME : SQLite의 날짜/시간 형식 변환 함수
  -- '%Y' : 연도만 추출, '%m' : 월만 추출, '%d' : 일만 추출
  -- '%Y-%m' : 연-월 형식, '%Y-%m-%d' : 연-월-일 형식
  STRFTIME('%Y', "InvoiceDate") AS "YEAR",
  SUM("Total") AS "TotalSales"
FROM invoices
GROUP BY STRFTIME('%Y', "InvoiceDate");

-- "BillingCountry"이 'USA'이고 "InvoiceDate"가 2010년 01월 01 이후인 레코드를 "BillingState"를
-- 기준으로 그룹화하고, 각 주별로 총 주문 금액을 계산하여 조회하시오.
SELECT "BillingState", SUM("Total") AS "TotalSales"
FROM invoices
WHERE
  "BillingCountry" = 'USA' AND
  "InvoiceDate" > '2010-01-01'
GROUP BY
  "BillingState";

--"BillingCountry"이 'Germany'이거나 'BillingCountry"이 'France'인 레코드를 "BillingCountry"를
-- 기준으로 그룹화하고, 각 나라별로 최대 주문 금액을 계산하여 조회
SELECT "BillingCountry", MAX("Total") AS "MaxOrderAmount"
FROM invoices
WHERE
  "BillingCountry" = 'Germany' OR
  "BillingCountry" = 'France'
GROUP BY
  "BillingCountry";