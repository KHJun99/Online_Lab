# 데이터 구조 (2)

## 주요 개념

### 1. 세트(Set) 연산
- **합집합**: `set1.union(set2)` 또는 `set1 | set2`
- **교집합**: `set1.intersection(set2)` 또는 `set1 & set2`
- **차집합**: `set1.difference(set2)` 또는 `set1 - set2`
- **대칭 차집합**: `set1.symmetric_difference(set2)` 또는 `set1 ^ set2`

### 2. 가변 인자
- **`*args`**: 임의의 개수의 위치 인자를 받음
- **`**kwargs`**: 임의의 개수의 키워드 인자를 받음
- **언패킹**: 여러 값을 동시에 전달

### 3. 딕셔너리 메소드
- **keys()**: 모든 키 반환
- **values()**: 모든 값 반환
- **items()**: 모든 키-값 쌍 반환
- **get()**: 안전하게 값 가져오기

## 예시 코드

### 세트 합집합
```python
def union_sets(set1, set2):
    return set1.union(set2)

def union_multiple_sets(*sets):
    if len(sets) < 2:
        print('최소 두 개의 셋이 필요합니다.')
        return set()

    result_sets = set()

    for s in sets:
        result_sets |= s

    return result_sets

# 사용 예시
result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)  # {1, 2, 3, 4, 5}

result = union_multiple_sets({1, 2}, {3, 4}, {5, 6})
print(result)  # {1, 2, 3, 4, 5, 6}

result = union_multiple_sets({1, 2})
# 출력: 최소 두 개의 셋이 필요합니다
```

### 세트 기본 연산
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 합집합
print(set1 | set2)  # {1, 2, 3, 4, 5, 6}

# 교집합
print(set1 & set2)  # {3, 4}

# 차집합
print(set1 - set2)  # {1, 2}

# 대칭 차집합
print(set1 ^ set2)  # {1, 2, 5, 6}
```

### 가변 인자 활용
```python
# 위치 인자
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))  # 15

# 키워드 인자
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_info(name='홍길동', age=20, city='서울')
```

## 기본 코드 템플릿

```python
# 세트 생성 및 연산
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 합집합
union = set1 | set2

# 교집합
intersection = set1 & set2

# 차집합
difference = set1 - set2

# 가변 인자 함수
def process_data(*args, **kwargs):
    # 위치 인자 처리
    for arg in args:
        print(arg)

    # 키워드 인자 처리
    for key, value in kwargs.items():
        print(f'{key}: {value}')

# 딕셔너리 순회
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f'{key}: {value}')
```

## 연습 파일
- `ws_6_1.py`: 세트 합집합 연산
