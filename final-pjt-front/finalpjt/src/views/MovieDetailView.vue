<template>
  <div>
    <div class="movie-detail">
      <div class="movie-detail-image" :style="{ backgroundImage: `url(${image(movie.poster_path)})` }"></div>
      <div class="movie-content d-flex">
        <div class="movie-poster">
          <img class="mt-2 " style="height:80vh;" :src="image(movie.poster_path)"/>
        </div>
        <div class="ml-4 w-75">
          <h1 class="movie-title" style="color: #dddddddd;">{{ movie.title }}</h1>
          <div class="movie-information-wrapper mt-4 d-flex align-items-center">
            <div class="ml-2 d-flex mx-3">
              <!-- <div class="genres" v-for="genre in movie.movie_genres" :key="genre.id">
                {{ genre }}
              </div> -->
              <p class="genres my-1">{{ movie.genreStr }}</p>
            </div> 
          </div>
          <p class="movie_vote_average mx-3"><small>평점: {{ movie.vote_average }}</small></p>
          <p class="movie_releasedate mx-3"><small>개봉: {{ movie.release_date }}</small></p>
          <div class="movie-overview mx-3 mt-3">{{ movie.overview }}</div>
        
          <b-button v-b-toggle.my-collapse variant="danger" class="reviewBtn mt-3 mx-3">예매하기</b-button>
          <!-- 리뷰 보러가기 -->
          <router-link :to="{ name: 'SpecificReview', params: {movieTitle: movie.title} }">
            <b-button variant="danger" class="reviewBtn mt-3 mx-3">관람평 보기</b-button>
          </router-link>
          <!-- 추천 영화 보러가기 -->
          <!-- <router-link :to="{ name: 'movieRecommend', params: {movieId: movie.movieId} }">
            <b-button variant="danger" class="reviewBtn mt-3 mx-3">추천영화</b-button>
          </router-link> -->
          <!-- 쿼리 사용 추천영화 보러가기 (새로고침시 홈화면으로 이동??)-->
          <router-link :to="{ name: 'movieRecommend', query: {movieId: movie.movieId} }">
            <b-button variant="danger" class="reviewBtn mt-3 mx-3">추천영화</b-button>
          </router-link>

          <b-collapse id="my-collapse">
            <b-card bg-variant="dark" text-variant="white" style="max-width: 10rem;" title="">
              <a class="cinema" href="http://www.cgv.co.kr/ticket" >CGV</a>
              <br>
              <a class="cinema" href="https://www.lottecinema.co.kr/NLCHS/Ticketing" >Lotte</a>
              <br>
              <a class="cinema" href="https://www.megabox.co.kr/booking?rpstMovieNo=" >MegaBox</a>
            </b-card>
          </b-collapse>
          <!-- 에고편... 실패 -->
          <!-- <div class="mx-3" v-if="videos">
            <hr>
            <h2 style="color: white;">Movie Trailer</h2>
            <iframe 
              :src="videoURL(videos[0].id.videoId)"
              :key='AIzaSyA98RDq0Q5W9FIFkm5ouJTbXH779vBFlm4'
              width="400"
              height="225"
              frameborder="0"></iframe>
            <h3 class="trailer-title" style="color: white;">{{ videos[0].snippet.title }}</h3>
            <hr>
          </div> -->
        </div>
        </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import { mapGetters, mapActions } from 'vuex'
  const API_URL = 'https://www.googleapis.com/youtube/v3/search'
  const API_KEY = 'AIzaSyA98RDq0Q5W9FIFkm5ouJTbXH779vBFlm4'
  
  export default {
    name: 'MovieDetail',
    data() {
      return {
        moviePk: this.$route.params.moviePk,
        movieTitle: this.$route.params.movieTitle,
        // 유튜브 영상 데이터
        inputValue: '',
        videos: [],
        video:{
          type:Object,
          required: true,
        }
      }
    },
    computed: {
      ...mapGetters(['movie']),
      // videoURL(){
      //   const videoId = this.video.id.videoId
      //   return `https://www.youtube.com/embed/${videoId}`
      // }
    },
    methods: {
      image(poster_path) {
        return `https://image.tmdb.org/t/p/w300/${poster_path}`},
      movieName(movie_title) {
        return `${movie_title}`},
      ...mapActions([
        'fetchMovie',
      ]),
      videoURL(videoId){
      // const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    },

    onInputKeyword(inputText){
      this.inputValue = inputText

      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.inputValue,
      }

      axios({
        method: 'get',
        url: API_URL,
        params
      })
      .then(result => {
        // console.log(result.data.items)
        this.videos = result.data.items
      })
      .catch(err => {
        console.log(err)
      })
    },
    },
    created() {
      this.fetchMovie(this.moviePk)
      //this.movieTitle = this.movieTitle + ' 예고편'
      //this.onInputKeyword(this.movieTitle)
    },
  }
</script>

<style>
.movie-detail {
  /* z-index: 99; */
  position: relative;
  padding: 40px 40px;
}

.movie-detail-image {
  background-size: cover;
  height: 100vh;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
  /* filter: grayscale(px); */
}

.movie-detail-image::after {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  min-height: 100vh;
  background-color: rgb(20, 20, 20);
  opacity: 0.8;
  content: "";
  display: block;
}

.movie-poster{
  margin-right: 50px;
}

.movie-content {
  position: relative;
  z-index: 999;
  
}
.movie-title {
  margin-left: 5px;
  color: #dddddddd;
  text-align: left;
}
.movie-information-wrapper {
  font-size: 13px;
  color: #dddddddd;
}
.genres {
  display: flex;
  align-items: center;
  color: #dddddddd;
}
.genres:not(:first-of-type)::before {
  content: "/";
  /* background-color: white; */
  /* display: inline-block; */
  margin-bottom: 4px;
  margin-left: 6px;
  margin-right: 1px;
  font-size: 20px;
}
.movie_vote_average{
  color: #dddddddd;
}
.movie_releasedate{
  color: #dddddddd;
}
.movie-overview {
  max-width: 80%;
  font-size: 14px;
  color: #dddddddd;
}
.cgv{
  color: rgb(224, 81, 81);
}
.homepage-link:hover {
  opacity: 0.5;
}

.reviewBtn {
    display: inline-block;
    width: 120px;
    height: 35px;
    /* background: url(../images/sprite/sprite_btn.png) 0 0 no-repeat; */
    font-family: 'Noto Sans KR', 'CJONLYONENEW', '맑은 고딕', '돋움', Dotum, sans-serif;
    vertical-align: top;
    background: rgb(241, 131, 131);
    color: azure;
}

.cinema {
  color: coral;
  text-decoration: none;
}
</style>
