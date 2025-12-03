/*
  아래에 코드를 작성해주세요.
*/

// 1. 검색창 & 버튼 마크업
const searchInput = document.querySelector('.search-box__input')
const searchButton = document.querySelector('.search-box__button')
const searchResult = document.querySelector('.search-result')
const loadingList = document.querySelector('.search-result--loadingList')

// Last.fm API 설정
const API_KEY = '07579b579289f1d000fd54553e39ccf5'
const API_URL = 'https://ws.audioscrobbler.com/2.0/'

// 무한 스크롤을 위한 변수
let currentPage = 1
let currentKeyword = ''
let isLoading = false
let observer = null
let hasMoreResults = true

// 2. 버튼에 클릭 이벤트 달기
searchButton.addEventListener('click', () => {
  const keyword = searchInput.value.trim()

  if (!keyword) {
    alert('검색어를 입력해주세요.')
    return
  }

  // 새로운 검색 시 초기화
  currentKeyword = keyword
  currentPage = 1
  searchResult.innerHTML = ''
  hasMoreResults = true

  // 기존 observer 해제
  if (observer) {
    observer.disconnect()
    observer = null
  }

  // 첫 페이지 로드
  fetchAlbums(keyword, currentPage)
})

// 앨범 검색 함수
function fetchAlbums(keyword, page) {
  if (isLoading) return

  isLoading = true

  // Loader 표시
  loadingList.style.display = 'block'

  // Ajax 요청 보내기
  axios({
    method: 'get',
    url: API_URL,
    params: {
      method: 'album.search',
      album: keyword,
      api_key: API_KEY,
      format: 'json',
      page: page,
      limit: 10
    }
  })
  .then((response) => {
    // API 응답 성공 시 로딩 숨김
    loadingList.style.display = 'none'

    // 요청이 성공적인 경우
    const albums = response.data.results.albummatches.album

    // 결과가 없거나 적으면 더 이상 로드하지 않음
    if (!albums || albums.length === 0) {
      hasMoreResults = false
      isLoading = false
      return
    }

    // 기존 sentinel 제거 (있다면)
    const oldSentinel = document.getElementById('sentinel')
    if (oldSentinel) {
      oldSentinel.remove()
    }

    // 응답 받은 앨범 검색 결과를 DOM 조작으로 추가
    albums.forEach(album => {
      // 이미지 태그 만들기
      const cardImg = document.createElement('img')
      cardImg.src = album.image[1]['#text']

      // div 태그 만들고, 클래스 부여하기
      const card = document.createElement('div')
      card.classList.add('search-result__card')

      // div 태그에 이미지 태그 추가하기
      card.appendChild(cardImg)

      // div 태그 만들고, 클래스 부여하기
      const textDiv = document.createElement('div')
      textDiv.classList.add('search-result__text')

      // h2 태그 만들어서 아티스트 이름 추가
      const artistName = document.createElement('h2')
      artistName.textContent = album.artist

      // p 태그 만들어서 앨범 이름 추가
      const albumName = document.createElement('p')
      albumName.textContent = album.name

      // textDiv에 h2, p 태그 추가
      textDiv.appendChild(artistName)
      textDiv.appendChild(albumName)

      // card에 textDiv 추가
      card.appendChild(textDiv)

      // search-result에 card 추가
      searchResult.appendChild(card)
    })

    // 무한 스크롤을 위한 sentinel 요소를 맨 마지막에 추가
    const sentinel = document.createElement('div')
    sentinel.id = 'sentinel'
    searchResult.appendChild(sentinel)

    // Intersection Observer 설정 (처음 한 번만)
    if (page === 1) {
      setupInfiniteScroll()
    }

    isLoading = false
  })
  .catch((error) => {
    console.error('앨범 검색 실패:', error)
    loadingList.style.display = 'none'
    isLoading = false
  })
}

// Infinite Scrolling 설정 (Intersection Observer API 사용)
function setupInfiniteScroll() {
  // Intersection Observer 생성
  observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      // sentinel이 화면에 보이면 다음 페이지 로드
      // hasMoreResults가 true일 때만 추가 로드
      if (entry.isIntersecting && !isLoading && currentKeyword && hasMoreResults) {
        currentPage++
        fetchAlbums(currentKeyword, currentPage)
      }
    })
  }, {
    rootMargin: '100px' // 100px 전에 미리 로드
  })

  // sentinel 관찰 시작
  const sentinel = document.getElementById('sentinel')
  if (sentinel) {
    observer.observe(sentinel)
  }
}
