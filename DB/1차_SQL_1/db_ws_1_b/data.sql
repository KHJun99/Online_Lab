# songs에서 모든 음악 데이터 조회
SELECT *
FROM songs

# songs에서 음악의 제목(title)을 기준으로 내림차순으로 정렬
SELECT *
FROM songs
ORDER BY
  title DESC;

# songs에서 특정 장르(genre)의 음악만 조회
SELECT *
FROM songs
WHERE
  genre = 'Pop';

# songs에서 플레이 시간이 3분 이상인 음악 데이터 조회
SELECT *
FROM songs
WHERE
  duration >= 180;