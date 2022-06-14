<template>
  <div>
    <div class="page-name">
      <div class="name my-2"><h3><strong>Recommend Related Movies</strong></h3></div>
    </div>
    <div class="d-flex flex-wrap justify-content-center">
      <div class="movie-card mx-2 my-2" style="width:250px;" v-for="movie in movieRecommend" :key="movie.id">
        <b-img style="width:250px; height:360px;" fluid :src="image(movie.poster_path)" alt="Movie Img"></b-img>
        
        <div class="movie-information">
          <div class="title"><strong>{{ movie.title }}</strong></div>
          <p class="movie-release-date"><small>{{ movie.release_date }}</small></p>
        </div>
      </div>
    </div>

    <!-- <div v-for="movie in movieRecommend" :key="movie.pk" class="row row-cols-1 row-cols-md-2 g-4 margin-top-0">
      <div class="card">
        <img :src="image(movie.poster_path)" alt="aa">
        <div class="card-body">{{ movie.title }}</div>
      </div>
    </div>     -->
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'MovieRecommendList',
    data() {
      return {
        movieId : this.$route.query.movieId
      }
    },
    computed: {
      ...mapGetters(['movieRecommend'])
    },
    methods: {
      ...mapActions(['fetchRecommendMovies']),
      image(poster_path) {
        return `https://image.tmdb.org/t/p/w300/${poster_path}`},
    },
    created() {
      this.fetchRecommendMovies(this.movieId)
    },
  }
</script>

<style>
.page-name {
  display: flex;
  justify-content: center;
  font-family: 'Noto Sans KR', 'CJONLYONENEW', '맑은 고딕', '돋움', Dotum, sans-serif;
}

.movie-information{
  background-color: rgb(241, 64, 64);
  color: white;
  font-family: 'Noto Sans KR', 'CJONLYONENEW', '맑은 고딕', '돋움', Dotum, sans-serif;
}
.title{
  text-align: center;
}
.movie-release-date{
  text-align: center;
}
</style>
