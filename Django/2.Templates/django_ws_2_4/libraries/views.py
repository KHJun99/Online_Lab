import requests
from django.shortcuts import render
import os
from dotenv import load_dotenv

API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
load_dotenv()
API_KEY = os.getenv('ALADIN_TTB_KEY')

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'Bestseller',
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    resp = requests.get(API_URL, params=params, timeout=10)
    # 디버그용: 요청 URL과 상태코드 로그

    resp.raise_for_status()      # 4xx/5xx 에러 발생 시 예외
    data = resp.json()           # JSON 파싱 (키가 없거나 HTML이면 여기서 예외)

    items = data.get('item', [])
    result = []
    for it in items:
        # .get() 사용으로 KeyError 방지
        result.append({
            'isbn': it.get('isbn13') or it.get('isbn'),
            'title': it.get('title'),
            'pubDate': it.get('pubDate'),
            'author': it.get('author'),
            'bestDuration': it.get('bestDuration'),  # 없는 경우 None
            'salesPoint' : it.get('salesPoint')
        })
        
    result = sorted(result, key=lambda x: x['salesPoint'] or 0, reverse=True)

    return render(request, 'recommend.html', {'result': result})