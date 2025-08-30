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
