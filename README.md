# 1학기 관통 프로젝트


## url구성
- 로그인화면
  - api/v1/accounts/signup
  - api/v1/accounts/login
  - api/v1/accounts/logout
- 홈 화면(영화 목록 카드 형식)
  - api/v1/movies/(main)
  - api/v1/movies/int:num/(detail)
  - api/v1/movies/recommended
  - api/v1/movies/category?name=(고른목록 ex) atcion)/ (router) (토글로 장르)
- 카테고리
  - api/v1/category/
-댓글
  - api/v1/movies/<int:num>/  

## django DataBase
1. dj-rest-auth, django-allauth 라이브러리 사용. (로그인, 회원가입시 token자동생성)
2. authtoken_token이란 테이블에 token key가 생기고, (1) token을 발급받았고, (2)로그인 되어있는 계정만 댓글,좋아요,detail조회 권한을 부여
3. logout하면 authtoken_token에서 key가 지워지고 권한잃음


- 만들 기능들
  - nav bar
  - router를 이용
  - main -> body(card)
  - App.vue -> cardBodys(종속) -> cardItems
  - carddetail
  - 댓글 기능
  - 댓글 좋아요(더블 클릭시)

### 5/20(금)
- main페이지.카드 → 1.그림 , 2.제목, 3.평점 4.개봉날짜 

### 5/23(월)

1. movies 메인, 디테일 페이지 만들기.
2. movies 디테일에서 community로 넘어가는 버튼 동작
3. comment의 좋아요 수.
4. movies.js라는 module 만들기.
5. 시간이 남는다면 css작업 조금.

### 5/24(화)

1. vue css
2. 영화 추천 새로고침시 404notfound 시간이 남는다면 해결하기.

### 5/25(수)

1. movie디테일 페이지 trailer추가