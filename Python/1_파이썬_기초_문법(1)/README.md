# 파이썬 기초 문법 (1)

## 주요 개념

### 1. 변수와 데이터 타입
- **변수 선언**: 파이썬에서는 자료형을 명시하지 않고 변수를 선언
- **기본 데이터 타입**: 문자열(str), 정수(int), 실수(float), 불리언(bool)

### 2. 컬렉션 자료형
- **리스트(list)**: 순서가 있는 변경 가능한 자료형 `[]`
- **튜플(tuple)**: 순서가 있는 변경 불가능한 자료형 `()`
- **딕셔너리(dict)**: 키-값 쌍으로 이루어진 자료형 `{}`
- **셋(set)**: 중복을 허용하지 않는 자료형 `{}`
- **레인지(range)**: 숫자 범위를 나타내는 자료형

### 3. 기본 입출력
- **print()**: 화면에 출력
- **type()**: 자료형 확인

## 예시 코드

### 변수 선언과 출력
```python
name = '홍길동'
age = 20
sentence_1 = '이름 : '
sentence_2 = '나이 : '

print(sentence_1, name)
print(sentence_2, age)
```

### 데이터 타입 확인
```python
string = '문자열'
integer = 10
floating_point = 3.14
a_list = [1, 2, 3, 4, 5]
dictionary = {'name': '홍길동', 'age': 20}
a_set = {1, 2, 3, 4, 5}
a_range = range(11)
a_tuple = (1, 2, 3)
boolean = True

print(type(string))        # <class 'str'>
print(type(integer))       # <class 'int'>
print(type(floating_point)) # <class 'float'>
print(type(a_list))        # <class 'list'>
print(type(dictionary))    # <class 'dict'>
print(type(a_set))         # <class 'set'>
print(type(a_range))       # <class 'range'>
print(type(a_tuple))       # <class 'tuple'>
print(type(boolean))       # <class 'bool'>
```

### Hello World
```python
word = 'Hello, World!'
print(word)
```

## 기본 코드 템플릿

```python
# 변수 선언
variable_name = value

# 출력
print(variable_name)

# 타입 확인
print(type(variable_name))

# 리스트 생성
my_list = [1, 2, 3, 4, 5]

# 딕셔너리 생성
my_dict = {'key': 'value'}
```

## 연습 파일
- `ws_1_1.py`: 변수와 print 연습
- `ws_1_2.py`: 데이터 타입 연습
- `hw_1_2.py`: Hello World 출력
