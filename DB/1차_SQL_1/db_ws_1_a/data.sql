# 테이블 생성
CREATE TABLE songs(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT,
  artist TEXT,
  album TEXT,
  genre TEXT,
  duration INTEGER
)

# 데이터 5개 삽입
INSERT INTO songs (id, title, artist, album, genre, duration)
VALUES 
    (1, 'Song 1', 'Artist 1', 'Album 1', 'Pop', 200),
    (2, 'Song 2', 'Artist 2', 'Album 2', 'Rock', 300),
    (3, 'Song 3', 'Artist 3', 'Album 3', 'Hip Hop', 250),
    (4, 'Song 4', 'Artist 4', 'Album 4', 'Electronic', 180),
    (5, 'Song 5', 'Artist 5', 'Album 5', 'R&B', 320);

# 특정 음악의 제목(title) 업데이트
UPDATE songs
SET title = 'New Title'
WHERE id = 1;