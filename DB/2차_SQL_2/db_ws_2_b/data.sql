-- Active: 1762838284732@@127.0.0.1@3306
-- 'InvoiceId'와 "invoiceDate"열만 선택하여 조회
SELECT "InvoiceId", "InvoiceDate"
FROM invoices;

-- "BillingCountry" 값이 "USA"이고 "Total"이 10보다 큰 레코드만 선택하여 조회
SELECT *
FROM invoices
WHERE
  "BillingCountry" = 'USA' AND
  "Total" > 10;

-- "BillingCity"가 "London"이거나 "Berlin"인 레코드를 선택하여 조회
SELECT *
FROM invoices
WHERE
  "BillingCity" = 'London' OR
  "BillingCity" = 'Berlin';

-- "Total"이 가장 큰 레코드를 선택하여 조회
SELECT *
FROM invoices
ORDER BY
  "Total" DESC
LIMIT
  1;

-- "InvoiceDate"가 2013년 3월 31일 이후이고 "Total"이 3보다 큰 레코드만 선택하여 조회
SELECT *
FROM invoices
WHERE
  "InvoiceDate" >= '2013-03-31' AND
  "Total" > 3;

-- "Billingcountry"이 'USA'이고 "BillinState"가 'California'이며 "Total"이 10보다 큰 레코드를 선택하여 조회
SELECT *
FROM invoices
WHERE
  "BillingCountry" = 'USA' AND
  "BillingState" = 'CA' AND
  "Total" > 10;

-- "BillingCountry" 이 'Canada'이고 "BillingState"이 'Ontario'이며 "BillingCity"가 'Toronto'인 레코드를 선택하여 조회
SELECT *
FROM invoices
WHERE
  "BillingCountry" = 'Canada' AND
  "BillingState" = 'ON' AND
  "BillingCity" = 'Toronto';

-- "InvoiceDate"가 2023년 1월 1일 이전이고 ("Total"이 50보다 이상이거나 "BillingCountry"이 'Brazil'인) 레코드를 선택하여 조회
SELECT *
FROM invoices
WHERE
  "InvoiceDate" < '2023-01-01' AND
  ("Total" >= 50 OR "BillingCountry" = 'Brazil');