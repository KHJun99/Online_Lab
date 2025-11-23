-- zoo 테이블에 species 열을 추가한다. 값은 TEXT를 받을 수 있어야 한다.
ALTER TABLE zoo
ADD COLUMN species TEXT;

-- zoo테이블에 삽압되어 있는 모든 데이터에 species 값을 추가하여 수정한다.
UPDATE zoo
SET species = 'Panthera leo'
WHERE name = 'Lion';

UPDATE zoo
SET species = 'Loxodonta africana'
WHERE name = 'Elephant';

UPDATE zoo
SET species = 'Giraffa camelopardalis'
WHERE name = 'Giraffe';

UPDATE zoo
SET species = 'Cebus capucinus'
WHERE name = 'Monkey';

-- 모든 데이터의 height 값을 2.54가 곱해진 값으로 수정한다.
UPDATE zoo
SET height = height * 2.54;

-- zoo 테이블의 모든 데이터를 조회하여 출력
SELECT *
FROM zoo
