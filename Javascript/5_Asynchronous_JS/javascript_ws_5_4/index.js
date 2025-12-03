/*
  아래에 코드를 작성해주세요.
*/

// 1. 검색창 & 버튼 마크업
const searchInput = document.querySelector('.search-box__input')
const searchButton = document.querySelector('.search-box__button')
const searchResult = document.querySelector('.search-result')

// Last.fm API 설정
const API_KEY = ''
const API_URL = 'https://ws.audioscrobbler.com/2.0/'

// 2. 버튼에 클릭 이벤트 달기
searchButton.addEventListener('click', fetchAlbums)

// 2. 클릭 이벤트 발생 시 Ajax 요청 보내기
function fetchAlbums() {
  // 검색어 가져오기
  const keyword = searchInput.value.trim()

  if (!keyword) {
    alert('검색어를 입력해주세요.')
    return
  }

  // Ajax 요청 보내기
  axios({
    method: 'get',
    url: API_URL,
    params: {
      method: 'album.search',
      album: keyword,
      api_key: API_KEY,
      format: 'json',
      limit: 10
    }
  })
  .then((response) => {
    // 요청이 성공적인 경우
    const albums = response.data.results.albummatches.album

    // 기존 검색 결과 초기화
    searchResult.innerHTML = ''

    // 응답 받은 앨범 검색 결과를 DOM 조작으로 추가
    albums.forEach(album => {
      // 3. 검색 결과 (DOM & Event)
      // 앨범 반수한 HTML 요소를 생성하여 응답 결과로부터 추출한 데이터 추가

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
  })
  .catch((error) => {
    console.error('앨범 검색 실패:', error)
    alert('앨범 검색에 실패했습니다.')
  })
}
