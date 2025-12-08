# Asynchronous with Django - Django와 비동기 통신

## 주요 개념

### 1. AJAX (Asynchronous JavaScript And XML)
- **비동기 통신**: 페이지 새로고침 없이 서버와 통신
- **JSON 데이터**: JavaScript Object Notation
- **RESTful API**: Django에서 제공하는 API

### 2. Django와 JavaScript 연동
- **Django View**: JSON 응답 반환
- **JavaScript Fetch**: Django API 호출
- **CSRF Token**: Django의 보안 토큰

### 3. Fetch with Django
- **GET 요청**: 데이터 조회
- **POST 요청**: 데이터 생성
- **PUT/PATCH**: 데이터 수정
- **DELETE**: 데이터 삭제

### 4. CSRF 토큰 처리
```javascript
// CSRF 토큰 가져오기
function getCookie(name) {
  let cookieValue = null
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';')
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim()
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
        break
      }
    }
  }
  return cookieValue
}

const csrftoken = getCookie('csrftoken')
```

## 예시 코드

### Django API 호출 (GET)
```javascript
// Django에서 게시글 목록 가져오기
async function getPosts() {
  try {
    const response = await fetch('/api/posts/')
    const data = await response.json()
    console.log(data)
    return data
  } catch (error) {
    console.error('에러:', error)
  }
}

// 게시글 목록 표시
getPosts().then(posts => {
  posts.forEach(post => {
    console.log(post.title, post.content)
  })
})
```

### Django API 호출 (POST)
```javascript
// Django에 새 게시글 생성
async function createPost(title, content) {
  const csrftoken = getCookie('csrftoken')

  try {
    const response = await fetch('/api/posts/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken
      },
      body: JSON.stringify({
        title: title,
        content: content
      })
    })

    const data = await response.json()
    console.log('생성됨:', data)
    return data
  } catch (error) {
    console.error('에러:', error)
  }
}

// 사용
createPost('새 글 제목', '새 글 내용')
```

### 좋아요 기능 구현
```javascript
// 좋아요 토글
async function toggleLike(postId) {
  const csrftoken = getCookie('csrftoken')

  try {
    const response = await fetch(`/api/posts/${postId}/like/`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrftoken
      }
    })

    const data = await response.json()

    // UI 업데이트
    const likeButton = document.querySelector(`#like-${postId}`)
    likeButton.textContent = data.is_liked ? '좋아요 취소' : '좋아요'

    const likeCount = document.querySelector(`#like-count-${postId}`)
    likeCount.textContent = data.like_count

  } catch (error) {
    console.error('에러:', error)
  }
}
```

### 댓글 작성 및 표시
```html
<!-- HTML -->
<form id="commentForm">
  <input type="text" id="commentContent">
  <button type="submit">댓글 작성</button>
</form>
<div id="commentList"></div>

<script>
// 댓글 작성
const commentForm = document.querySelector('#commentForm')
commentForm.addEventListener('submit', async (event) => {
  event.preventDefault()

  const content = document.querySelector('#commentContent').value
  const postId = 1  // 게시글 ID
  const csrftoken = getCookie('csrftoken')

  const response = await fetch(`/api/posts/${postId}/comments/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({ content: content })
  })

  const comment = await response.json()

  // 댓글 목록에 추가
  const commentList = document.querySelector('#commentList')
  const commentDiv = document.createElement('div')
  commentDiv.textContent = comment.content
  commentList.appendChild(commentDiv)

  // 입력 필드 초기화
  event.target.reset()
})
</script>
```

## 기본 코드 템플릿

### Django API 통신 클래스
```javascript
class DjangoAPI {
  constructor(baseURL) {
    this.baseURL = baseURL
    this.csrftoken = this.getCookie('csrftoken')
  }

  getCookie(name) {
    let cookieValue = null
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';')
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim()
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
          break
        }
      }
    }
    return cookieValue
  }

  async get(endpoint) {
    const response = await fetch(`${this.baseURL}${endpoint}`)
    return await response.json()
  }

  async post(endpoint, data) {
    const response = await fetch(`${this.baseURL}${endpoint}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': this.csrftoken
      },
      body: JSON.stringify(data)
    })
    return await response.json()
  }

  async delete(endpoint) {
    const response = await fetch(`${this.baseURL}${endpoint}`, {
      method: 'DELETE',
      headers: {
        'X-CSRFToken': this.csrftoken
      }
    })
    return response.ok
  }
}

// 사용
const api = new DjangoAPI('/api')
const posts = await api.get('/posts/')
const newPost = await api.post('/posts/', { title: '제목', content: '내용' })
```

### 실시간 검색 구현
```javascript
const searchInput = document.querySelector('#search')
let timeout = null

searchInput.addEventListener('input', (event) => {
  clearTimeout(timeout)

  timeout = setTimeout(async () => {
    const query = event.target.value

    if (query.length > 0) {
      const response = await fetch(`/api/search/?q=${query}`)
      const results = await response.json()

      // 결과 표시
      displayResults(results)
    }
  }, 300)  // 300ms 디바운싱
})

function displayResults(results) {
  const resultsDiv = document.querySelector('#results')
  resultsDiv.innerHTML = ''

  results.forEach(result => {
    const div = document.createElement('div')
    div.textContent = result.title
    resultsDiv.appendChild(div)
  })
}
```

## 연습 파일
- Django REST API와 JavaScript Fetch 연동
- CSRF 토큰 처리
- 비동기 데이터 CRUD
