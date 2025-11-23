# name의 값이 love 글자를 포함한 데이터를 조회
SELECT
  *
FROM
  tracks
WHERE
  name LIKE '%love%'

# Genereld의 값이 1이고, Milliseconds의 값이 300000 이상인 데이터를 모두 조회 -> UnitPrice 기준으로 내림차순 정렬
SELECT
  *
FROM
  tracks
WHERE
  "GenreId" = 1
  AND "Milliseconds" >= 300000
ORDER BY
  "UnitPrice" DESC

# GenreId별로 그룹화 하여, GenreId와 각 그룹별 데이터의 수를 조회하시오.
# 단, 그룹별 데이터 수는 TotalTracks 필드로 표기하여 나타내시고.

SELECT GenreId, COUNT(*) AS TotalTracks
FROM tracks
GROUP BY "GenreId";

# GenreId별로 그룹화하여, GenreId를 활용한 UnitPrice의 총합을 계산하여 조회
# 단, UnitPrice의 총합은 TotalPrice의 필드로 표기, 그 중, TotalPrice의 값이 100이상인 데이터들만 조회

SELECT GenreId, SUM(UnitPrice) AS TotalPrice
FROM tracks
GROUP BY "GenreId"
HAVING TotalPrice >= 100;