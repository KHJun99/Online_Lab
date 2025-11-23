-- Active: 1762832045276@@127.0.0.1@3306
-- 'artists'테이블에서 모든 아티스트의 정보를 조회
SELECT *
FROM artists;

-- 'artists'테이블의 모든 데이터의 수를 조회
SELECT count(*)
FROM artists;

-- 'artists'테이블에서 Name이 'AC/DC'인 정보를 조회
SELECT "ArtistId", "Name"
FROM artists
WHERE
  Name = 'AC/DC';

-- 'artists' 테이블의 모든 데이터 중, artistid와 name만 출력
SELECT "ArtistId", "Name"
FROM artists;

-- 'artists' 테이블에서 Name이 'Gilberto Gil' 이거나 'Ed Motta'정보 조회
SELECT "ArtistId", "Name"
FROM artists
WHERE
  "Name" = 'Gilberto Gil'
  OR
  "Name" = 'Ed Motta';

-- 'artists' 테이블에서 모든 정보를 Name 기준으로 내림차순 정렬하여 조회
SELECT *
FROM artists
ORDER BY
  Name DESC;

-- 'artists' 테이블에서 이름이 'Vinicius'로 시작하는 정보를 조회(단, 2개만 출력)
SELECT "ArtistId", "Name"
FROM artists
WHERE
  "Name" LIKE 'Vinícius%'
LIMIT
  2;

-- 'artists' 테이블에서 'ArtistId'가 50번부터 70번까지의 데이터를 조회하여 'ArtistId'만 출력
SELECT "ArtistId"
FROM artists
WHERE
  "ArtistId" BETWEEN 50 AND 70;