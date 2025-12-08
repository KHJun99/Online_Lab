# 파이썬 기초 문법 (2)

## 주요 개념

### 1. 문자열 처리
- **이스케이프 문자**: `\n` (개행), `\'` (작은따옴표), `\"` (큰따옴표), `\t` (탭)
- **다중 라인 문자열**: 따옴표 3개 사용 `'''` 또는 `"""`
- **문자열 연결**: `+` 연산자 또는 콤마로 연결

### 2. 리스트와 복사
- **얕은 복사(Shallow Copy)**: 참조만 복사
- **깊은 복사(Deep Copy)**: `copy.deepcopy()` 사용하여 완전히 독립적인 복사본 생성
- **리스트 인덱싱**: 2차원 리스트 접근 `list[i][j]`

### 3. 비교 연산자
- **식별 연산자**: `is`, `is not` - 객체의 동일성 비교
- **동등 연산자**: `==`, `!=` - 값의 동등성 비교

## 예시 코드

### 이스케이프 문자와 다중 라인 출력
```python
print('다음은 이형기 시인의 "낙화"의 한 구절이다.\n'
      '- 1연\n'
      '	가야할 때 언제인가를\n'
      '	분명히 알고 가는 이의\n'
      '	뒷모습은 얼마나 아름다운가.\n'
      '\n'
      '나는 이 시를 보며 \'나는 내가 가야할 때가 언제일까?\' 를 생각해 보았다.'
)
```

### 깊은 복사와 리스트 수정
```python
import copy

catalog = [
    ['시간의 틈', '반짝임의 어둠', '망각의 경계'],
    ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'],
    ['황금의 칼날', '비열한 간신', '무명의 영웅'],
    ['성공의 열쇠', '내면의 변화', '목표의 달성'],
]

# 깊은 복사 생성
backup_catalog = copy.deepcopy(catalog)

# 원본 수정
catalog[3][0] = '성공을 향한 한 걸음'
catalog[3][1] = '내 삶의 변화'
catalog[3][2] = '목표 달성의 비밀'

# 식별 연산자로 비교
print(catalog is backup_catalog)  # False

print('backup_catalog : ')
print(backup_catalog)  # 원본 유지

print('catalog : ')
print(catalog)  # 수정된 버전
```

## 기본 코드 템플릿

```python
# 다중 라인 문자열
text = '''
여러 줄에
걸친
문자열
'''

# 이스케이프 문자 사용
print('줄바꿈\n탭\t따옴표\'')

# 깊은 복사
import copy
original_list = [[1, 2], [3, 4]]
copied_list = copy.deepcopy(original_list)

# 2차원 리스트 접근
matrix = [[1, 2, 3], [4, 5, 6]]
element = matrix[0][1]  # 2

# 식별 연산자
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # True
print(a is c)  # False
print(a == c)  # True
```

## 연습 파일
- `ws_2_1.py`: 이스케이프 문자와 다중 라인 출력
- `ws_2_5.py`: 깊은 복사와 리스트 수정
