# 함수와 제어문 (2)

## 주요 개념

### 1. 반복문
- **for 문**: 시퀀스(리스트, 튜플, 문자열 등)를 순회
- **while 문**: 조건이 참인 동안 반복
- **break**: 반복문 종료
- **continue**: 다음 반복으로 건너뛰기

### 2. 딕셔너리 조작
- **키-값 접근**: `dict['key']` 또는 `dict.get('key')`
- **키 존재 확인**: `key in dict`
- **딕셔너리에 추가**: `dict[new_key] = value`
- **중첩 딕셔너리**: 딕셔너리 안에 딕셔너리

### 3. API 요청
- **requests 모듈**: HTTP 요청 보내기
- **JSON 데이터**: `response.json()`으로 파싱
- **데이터 처리**: API 응답 데이터를 반복문으로 처리

## 예시 코드

### API 요청과 데이터 필터링
```python
import requests
from pprint import pprint as print

API_URL = 'https://jsonplaceholder.typicode.com/users'

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

def censorship(company, name):
    if company in black_list:
        print(f'{company} 소속의 {name} 은/는 등록할 수 없습니다.')
        return False
    else:
        print('이상 없습니다.')
        return True

def create_user(user_list):
    censored_user_list = {}

    for user in user_list:
        company = user['company']['name']
        name = user['username']

        # blacklist 체크
        if censorship(company, name):
            # company 키가 없으면 리스트 생성 후 추가
            if company not in censored_user_list:
                censored_user_list[company] = []
            censored_user_list[company].append(name)

    return censored_user_list

# API 데이터 요청
response = requests.get(API_URL).json()

# create_user 실행
result = create_user(response)

# 최종 결과 출력
print(result)
```

### 기본 반복문
```python
# for 문
for i in range(5):
    print(i)

# 리스트 순회
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# 딕셔너리 순회
person = {'name': '홍길동', 'age': 20}
for key, value in person.items():
    print(f'{key}: {value}')
```

## 기본 코드 템플릿

```python
# for 문으로 리스트 순회
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# 조건문과 반복문 결합
for num in range(10):
    if num % 2 == 0:
        print(f'{num}은 짝수')
    else:
        print(f'{num}은 홀수')

# 딕셔너리 동적 생성
result_dict = {}
for i in range(5):
    key = f'key_{i}'
    if key not in result_dict:
        result_dict[key] = []
    result_dict[key].append(i)

# API 요청 기본 구조
import requests
response = requests.get('API_URL').json()
for item in response:
    # 데이터 처리
    pass
```

## 연습 파일
- `ws_4_4.py`: API 요청과 데이터 필터링
