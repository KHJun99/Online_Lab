from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv

API_URL = "https://www.aladin.co.kr/ttb/api/ItemList.aspx"

# .env 로드
load_dotenv()
API_KEY = os.getenv("ALADIN_TTB_KEY")

params = {
    'ttbkey' : API_KEY,
    'QueryType' : 'ItemNewSpecial',
    'MaxResults' : 20,
    'start' : 1,
    'SearchTarget' : 'Book',
    'Output' : 'JS',
    'Version' : '20131101'
}

def fetch_books():
    """API에서 책 데이터를 가져오는 함수"""
    if not API_KEY:
        return []
    
    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data.get('item', [])

def transform(items):
    """필요한 필드만 추출"""
    results = []
    for it in items:
        results.append({
            'isbn' : it.get('isbn13') or it.get('isbn'),
            'author' : it.get('author'),
            'title' : it.get('title'),
            'pub_date' : it.get('pubDate')
        })
    return results

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    books = transform(fetch_books())
    return render(request, 'recommend.html', {'books':books})