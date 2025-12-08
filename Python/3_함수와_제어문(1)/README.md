# 함수와 제어문 (1)

## 주요 개념

### 1. 함수 정의
- **함수 선언**: `def` 키워드 사용
- **매개변수**: 함수에 전달되는 값
- **반환값**: `return` 키워드로 값 반환
- **기본 매개변수**: 매개변수에 기본값 지정

### 2. 제어문
- **조건문**: `if`, `elif`, `else`
- **비교 연산자**: `>`, `<`, `>=`, `<=`, `==`, `!=`
- **논리 연산자**: `and`, `or`, `not`

### 3. 함수 호출
- **위치 인자**: 순서대로 전달
- **키워드 인자**: 매개변수 이름으로 전달
- **기본값**: 인자를 전달하지 않으면 기본값 사용

## 예시 코드

### 기본 함수 정의와 호출
```python
def add_numbers(a, b):
    return a + b

# 함수 호출
print(add_numbers(3, 5))  # 8
```

### 여러 타입의 함수
```python
# 곱셈 함수
def my_multi(number_1, number_2):
    return number_1 * number_2

# 조건문이 있는 함수
def is_negative(number):
    if number <= 0:
        return True
    return False

# 기본 매개변수가 있는 함수
def default_arg_func(default='기본 값'):
    return default

# 함수 호출
result_1 = my_multi(2, 3)           # 6
result_2 = is_negative(3)           # False
result_3 = default_arg_func()       # '기본 값'
result_4 = default_arg_func('다른 값')  # '다른 값'

print(result_1)
print(result_2)
print(result_3)
print(result_4)
```

### 조건문 사용
```python
def check_number(num):
    if num > 0:
        return "양수"
    elif num < 0:
        return "음수"
    else:
        return "0"

print(check_number(5))   # "양수"
print(check_number(-3))  # "음수"
print(check_number(0))   # "0"
```

## 기본 코드 템플릿

```python
# 기본 함수 구조
def function_name(parameter1, parameter2):
    # 함수 본문
    result = parameter1 + parameter2
    return result

# 기본 매개변수가 있는 함수
def greet(name='Guest'):
    return f'안녕하세요, {name}님!'

# 조건문이 있는 함수
def check_age(age):
    if age >= 18:
        return '성인'
    else:
        return '미성년자'

# 함수 호출
result = function_name(10, 20)
print(result)

print(greet())           # 기본값 사용
print(greet('홍길동'))    # 인자 전달
print(check_age(20))
```

## 연습 파일
- `ws_3_a.py`: 함수 정의와 기본 매개변수
- `hw_3_2.py`: 덧셈 함수 작성
