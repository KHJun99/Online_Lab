# OOP (2) - 예외 처리와 고급 OOP

## 주요 개념

### 1. 예외 처리
- **try-except**: 예외를 처리하는 구문
- **try**: 예외가 발생할 수 있는 코드 블록
- **except**: 예외 발생 시 실행되는 코드 블록
- **Exception**: 모든 내장 예외의 기본 클래스
- **특정 예외**: `ValueError`, `TypeError`, `ZeroDivisionError` 등

### 2. 예외 종류
- **ValueError**: 잘못된 값이 전달된 경우
- **TypeError**: 잘못된 타입이 전달된 경우
- **ZeroDivisionError**: 0으로 나누는 경우
- **KeyError**: 존재하지 않는 딕셔너리 키에 접근한 경우

### 3. 예외 처리 패턴
- **기본 예외 처리**: 모든 예외를 잡음
- **특정 예외 처리**: 특정 예외만 처리
- **다중 예외 처리**: 여러 종류의 예외를 각각 처리

## 예시 코드

### 기본 예외 처리
```python
def check_number():
    try:
        num = int(input('숫자를 입력하세요: '))
        if num > 0:
            print('양수입니다.')
        elif num == 0:
            print('0입니다.')
        else:
            print('음수입니다.')
    except Exception:
        print('잘못된 입력입니다.')

check_number()
```

### 특정 예외 처리
```python
def divide_numbers(a, b):
    try:
        result = a / b
        print(f'결과: {result}')
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')
    except TypeError:
        print('숫자만 입력 가능합니다.')
    except Exception as e:
        print(f'예상치 못한 오류: {e}')

divide_numbers(10, 2)   # 결과: 5.0
divide_numbers(10, 0)   # 0으로 나눌 수 없습니다.
```

### 다중 예외 처리
```python
def process_data(data):
    try:
        # 데이터 변환 시도
        number = int(data)

        # 계산 시도
        result = 100 / number

        print(f'결과: {result}')

    except ValueError:
        print('숫자로 변환할 수 없습니다.')
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')
    except Exception as e:
        print(f'오류 발생: {e}')

process_data('10')      # 결과: 10.0
process_data('abc')     # 숫자로 변환할 수 없습니다.
process_data('0')       # 0으로 나눌 수 없습니다.
```

### try-except-else-finally
```python
def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
    except FileNotFoundError:
        print('파일을 찾을 수 없습니다.')
    except Exception as e:
        print(f'오류 발생: {e}')
    else:
        print('파일을 성공적으로 읽었습니다.')
        print(content)
    finally:
        print('작업 완료')
        try:
            file.close()
        except:
            pass
```

## 기본 코드 템플릿

```python
# 기본 try-except 구조
try:
    # 예외가 발생할 수 있는 코드
    risky_operation()
except Exception:
    # 예외 처리
    print('오류가 발생했습니다.')

# 특정 예외 처리
try:
    number = int(input('숫자 입력: '))
    result = 10 / number
except ValueError:
    print('올바른 숫자를 입력하세요.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

# 예외 정보 얻기
try:
    # 코드
    pass
except Exception as e:
    print(f'오류: {e}')

# 완전한 예외 처리 구조
try:
    # 시도할 코드
    pass
except SpecificError:
    # 특정 예외 처리
    pass
except Exception as e:
    # 기타 예외 처리
    pass
else:
    # 예외가 발생하지 않은 경우
    pass
finally:
    # 항상 실행되는 코드
    pass
```

## 연습 파일
- `hw_8_2.py`: 숫자 입력 예외 처리
