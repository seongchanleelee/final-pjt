<template>
  <div>
      <h3 class="movie-title fw-bold mt-2">
        [{{ movieTitle }}] 관련글
      </h3>
      <ul class="review-ul">
      <!-- movieDetail에서 버튼을 눌렀을 시 나오는 게시글 -->
      <li v-for="review in reviews" :key="review.pk" v-show="movieTitle===review.movie_title">
      <!-- v-show="review.movie.title==" -->
       
        <!-- 작성자 -->
        <span class="fw-bold fs-6">
          {{ review.user.username }} : 
        </span>

        <!-- 글 이동 링크 (제목) -->
        <router-link class="review-title"
          :to="{ name: 'review', params: {reviewPk: review.pk, isSpecific: true } }">
          <span class="fs-5">
            {{ review.title }}
          </span>
        </router-link>

        <!-- 댓글 개수/좋아요 개수 -->
        <p class="fw-bold">
          댓글:({{ review.comment_count }})
          <font-awesome-icon class="mx-2" style="color:red;" icon="fa-solid fa-heart" beat/>:{{ review.like_count }}
        </p>
        <hr>
      </li>

    </ul>
   
  </div>
</template>


<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'ReviewList',
    data() {
      return {
        movieTitle : this.$route.params.movieTitle
      }
    },
    computed: {
      ...mapGetters(['reviews'])
    },
    methods: {
      ...mapActions(['fetchReviews'])
    },
    created() {
      this.fetchReviews()
    },
  }
</script>


<style>
.movie-title {
  color: black;
  text-align: center;

}

.review-ul {
  list-style:none;
}

</style>