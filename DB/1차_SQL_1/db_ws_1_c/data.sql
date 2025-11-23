# songs에서 음악의 장르(genre)를 기준으로 그룹화
SELECT genre, COUNT(*) AS count
FROM songs
GROUP BY
  genre;

# songs에서 각 그룹별로 음악의 수를 계산
SELECT genre, COUNT(*) AS count, AVG(duration) AS average_duration
FROM songs
GROUP BY genre;