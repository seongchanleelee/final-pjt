import axios from 'axios'
//import router from '@/router'
import drf from '@/api/drf'
import router from '@/router'

//import _ from 'lodash'

export default {
  // namespaced: true,
  state: {
    movies: [],
    movie: {},
    movieRecommend: [],
  },

  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    movieRecommend: state => state.movieRecommend,
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_MOVIERECOMMEND: (state, movieRecommend) => state.movieRecommend = movieRecommend,
  },

  actions: {
    fetchMovies({ commit }) {
      /* 게시글 목록 받아오기
      GET: movies URL
        성공하면
          응답으로 받은 게시글들을 state.articles에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.movies.movies(),
        method: 'get',
        // headers: getters.authHeader,
      })
        .then(res => {
          console.log(res.data)
          commit('SET_MOVIES', res.data)
        })
        .catch(err => console.error(err.response))
    },
    // movie detail
    fetchMovie({ commit }, moviePk) {
      axios({
        url:drf.movies.movieDetail(moviePk),
        method: 'get',

      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => {
          console.log(err)
          if (err.response.status ===404) {
            router.push({ name: 'NotFound404'})
          }
        })
    },
    fetchRecommendMovies({ commit }, movieId) {
      /* 추천 영화 목록 받아오기
      GET: movies URL
        성공하면
          응답으로 받은 게시글들을 state.articles에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.movies.movieRecommend(movieId),
        method: 'get',
        // headers: getters.authHeader,
      })
        .then(res => {
          console.log(res.data)
          commit('SET_MOVIERECOMMEND', res.data)
        })
        .catch(err => console.error(err.response))
    },
  },
}
