# OOP (1) - 객체지향 프로그래밍 기초

## 주요 개념

### 1. 클래스와 객체
- **클래스**: 객체를 생성하기 위한 템플릿
- **객체(인스턴스)**: 클래스로부터 생성된 실체
- **속성(Attribute)**: 객체의 데이터
- **메소드(Method)**: 객체의 동작

### 2. 생성자
- **`__init__()`**: 객체 생성 시 자동으로 호출되는 메소드
- **`self`**: 인스턴스 자신을 참조하는 매개변수
- **초기화**: 객체의 초기 상태 설정

### 3. 인스턴스 메소드
- **정의**: 첫 번째 매개변수로 `self`를 받음
- **호출**: 인스턴스를 통해 호출
- **속성 접근**: `self.attribute`로 인스턴스 속성에 접근

## 예시 코드

### 기본 클래스 정의
```python
class StringRepeater:
    def __init__(self):
        pass

    def repeat_string(self, count, word):
        self.count = count
        self.word = word
        for _ in range(count):
            print(word)

# 인스턴스 생성 및 메소드 호출
repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
# 출력:
# Hello
# Hello
# Hello
```

### 속성을 가진 클래스
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'안녕하세요, 제 이름은 {self.name}이고 {self.age}살입니다.')

# 인스턴스 생성
person1 = Person('홍길동', 20)
person1.introduce()  # 안녕하세요, 제 이름은 홍길동이고 20살입니다.
```

### 메소드로 속성 수정
```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count

# 사용 예시
counter = Counter()
counter.increment()
counter.increment()
print(counter.get_count())  # 2
```

## 기본 코드 템플릿

```python
# 기본 클래스 구조
class ClassName:
    def __init__(self, param1, param2):
        # 인스턴스 속성 초기화
        self.attribute1 = param1
        self.attribute2 = param2

    def method_name(self):
        # 인스턴스 메소드
        return self.attribute1

# 클래스 인스턴스 생성
instance = ClassName('value1', 'value2')

# 메소드 호출
result = instance.method_name()

# 속성 접근
print(instance.attribute1)
print(instance.attribute2)

# 속성 수정
instance.attribute1 = 'new_value'
```

## 연습 파일
- `hw_7_2.py`: 문자열 반복 클래스
