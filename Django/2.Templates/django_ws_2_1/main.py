import requests
import os
import json
from dotenv import load_dotenv

# 알라딘 Open API 기본 URL
API_URL = "https://www.aladin.co.kr/ttb/api/ItemList.aspx"

# .env 파일을 읽어 환경변수 로드
load_dotenv()
# 환경변수에서 ALADIN_TTB_KEY 값 가져오기 (발급받은 API 키)
API_KEY = os.getenv("ALADIN_TTB_KEY")

# API 요청에 필요한 파라미터 설정
params = {
    'ttbkey': API_KEY,                  # 발급받은 TTBKey
    'QueryType': 'ItemNewSpecial',      # 신간/특별분류 (ItemNewAll = 전체 신간, ItemNewSpecial = 추천 신간)
    'MaxResults': 50,                   # 최대 50권까지 가져오기
    'start': 1,                         # 시작 위치 (페이지네이션)
    'SearchTarget': 'Book',             # 도서만 검색
    'Output': 'JS',                     # 응답을 JSON으로 받기
    'Version': '20131101'               # API 버전 (최신)
}

def fetch_books():
    """
    알라딘 API에서 책 데이터를 가져오는 함수
    - API_KEY가 없으면 에러 발생
    - 정상 호출 시 JSON 데이터 중 'item' 리스트 반환
    """
    if not API_KEY:
        raise RuntimeError("⚠️ API_KEY가 없습니다. 환경변수 ALADIN_TTB_KEY를 설정하거나 직접 문자열로 지정하세요.")
    
    # GET 요청 보내기
    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()  # 요청 실패 시 예외 발생
    data = response.json()       # JSON 응답 파싱
    return data.get('item', [])  # 'item' 키에 책 리스트가 들어 있음

def transform(items):
    """
    원본 응답 데이터에서 필요한 필드만 추출해 새로운 리스트 생성
    - 국제 표준 도서 번호 (isbn13 우선, 없으면 isbn)
    - 저자
    - 제목
    - 출간일
    """
    results = []
    for it in items:
        results.append({
            "국제 표준 도서 번호" : it.get('isbn13') or it.get('isbn'),
            "저자" : it.get('author'),
            "제목" : it.get('title'),
            "출간일" : it.get('pubDate'),
        })
    return results

def main():
    """
    실행 메인 함수
    - API에서 책 목록 가져오기
    - 필요한 필드만 추출(transform)
    - 보기 좋게 JSON 형태로 출력
    """
    books = fetch_books()
    slim_books = transform(books)
    print(json.dumps(slim_books, ensure_ascii=False, indent=2))  # ensure_ascii=False → 한글 깨짐 방지
    
# 프로그램 실행
main()
