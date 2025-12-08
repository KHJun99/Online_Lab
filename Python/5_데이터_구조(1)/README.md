# 데이터 구조 (1)

## 주요 개념

### 1. 리스트 메소드
- **append()**: 리스트 끝에 요소 추가
- **extend()**: 리스트에 다른 리스트의 모든 요소 추가
- **pop()**: 지정된 인덱스의 요소 제거 및 반환
- **remove()**: 첫 번째로 일치하는 요소 제거
- **index()**: 요소의 인덱스 찾기
- **sort()**: 리스트 정렬
- **reverse()**: 리스트 역순 정렬

### 2. 리스트 컴프리헨션
- **기본 형태**: `[expression for item in iterable]`
- **조건 포함**: `[expression for item in iterable if condition]`
- **간결한 코드**: 반복문을 한 줄로 표현

### 3. 데이터 필터링
- **조건문으로 필터링**: 특정 조건을 만족하는 요소만 선택
- **새 리스트 생성**: 원본 리스트를 유지하면서 필터링된 새 리스트 생성

## 예시 코드

### 짝수 필터링
```python
def even_elements(lst):
    new_number = []
    new_lst = []

    for num in lst:
        # 짝수 확인 조건문
        if num % 2 == 0:
            # pop 메소드를 이용하여 기존 리스트에서 제거 후 해당 값 반환
            idx = lst.pop(lst.index(num))
            new_number.append(idx)

    # 선별된 new_number(짝수)를 새로운 리스트에 추가
    new_lst.extend(new_number)
    return new_lst

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)  # [2, 4, 6, 8, 10]
```

### 리스트 메소드 활용
```python
# append - 요소 추가
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

# extend - 리스트 확장
my_list.extend([5, 6, 7])
print(my_list)  # [1, 2, 3, 4, 5, 6, 7]

# pop - 요소 제거 및 반환
last_item = my_list.pop()
print(last_item)  # 7
print(my_list)    # [1, 2, 3, 4, 5, 6]

# remove - 특정 값 제거
my_list.remove(3)
print(my_list)  # [1, 2, 4, 5, 6]

# index - 인덱스 찾기
idx = my_list.index(4)
print(idx)  # 2
```

### 리스트 컴프리헨션
```python
# 기본 리스트 컴프리헨션
numbers = [1, 2, 3, 4, 5]
squared = [n**2 for n in numbers]
print(squared)  # [1, 4, 9, 16, 25]

# 조건을 포함한 리스트 컴프리헨션
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)  # [2, 4]

# 짝수만 제곱
even_squared = [n**2 for n in numbers if n % 2 == 0]
print(even_squared)  # [4, 16]
```

## 기본 코드 템플릿

```python
# 리스트 생성 및 조작
my_list = []

# 요소 추가
my_list.append(1)
my_list.extend([2, 3, 4])

# 요소 제거
removed_item = my_list.pop(0)  # 첫 번째 요소 제거
my_list.remove(3)  # 값 3 제거

# 요소 찾기
if 2 in my_list:
    index = my_list.index(2)
    print(f'2는 인덱스 {index}에 있습니다')

# 리스트 정렬
my_list.sort()
my_list.reverse()

# 리스트 컴프리헨션으로 필터링
filtered_list = [x for x in my_list if x > 0]

# 리스트 컴프리헨션으로 변환
transformed_list = [x * 2 for x in my_list]
```

## 연습 파일
- `ws_5_5.py`: 리스트 메소드를 활용한 짝수 필터링
