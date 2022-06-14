<template>
  <div>
    <div class="page-name">
      <div class="name my-2"><h3><strong>Popular Movie Chart</strong></h3></div>
    </div>
    <div class="d-flex flex-wrap justify-content-center">
      <div class="movie-card mx-2 my-2" style="width:250px;" v-for="movie in movies" :key="movie.id">
        <router-link :to="{ name: 'movie', params: {moviePk: movie.id, movieTitle: movie.title} }">
          <b-img style="width:250px; height:360px;" fluid :src="image(movie.poster_path)" alt="Movie Img"></b-img>
        </router-link>
        <div @click="goDetail(movie.id, movie.title)" class="movie-information">
          <div class="title"><strong>{{ movie.title }}</strong></div>
          <p class="movie-release-date"><small>{{ movie.release_date }}</small></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'MovieList',
    computed: {
      ...mapGetters(['movies'])
    },
    methods: {
      ...mapActions(['fetchMovies']),
      image(poster_path) {
        return `https://image.tmdb.org/t/p/w300/${poster_path}`},
      goDetail(id, title){
        this.$router.push({ name: 'movie', params: {moviePk: id, movieTitle: title} })
      }
    },
    created() {
      this.fetchMovies()
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
