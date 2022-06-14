<template>
  <div>
    <div class="page-name">
      <div class="name my-2"><h3><strong>{{ profile.username }}'s page</strong></h3></div>
    </div>
    <hr class="bg-light">

    <h4 class="mx-4 my-4"> <strong>My Reviews</strong></h4>

    <ul class="community-ul">
      <li v-for="review in profile.reviews" :key="review.pk">
        <!-- {{ review }} -->
        <div><strong>[{{ review.movie_title }}] 관련된 글</strong></div>
        <router-link class="review-title" :to="{ name: 'review', params: { reviewPk: review.pk } }">
          <span class="fs-4">{{ review.title }}</span>
        </router-link><br>
        <span><small>last update: </small></span>
        <span><small>{{ review.updated_at.split("-")[0] }}</small></span>/
        <span><small>{{ review.updated_at.split("-")[1] }}</small></span>/
        <span><small>{{ review.updated_at.split("-")[2].split("T")[0] }}</small></span>.
        <span><small>{{ review.updated_at.split("-")[2].split("T")[1].split(":")[0] }}</small></span>:
        <span><small>{{ review.updated_at.split("-")[2].split("T")[1].split(":")[1] }}</small></span>
        <hr>
      </li>
    </ul>

    <h4 class="mx-4 my-4"> <strong>My Likes</strong></h4>

    <ul class="community-ul">
      <li v-for="review in profile.like_reviews" :key="review.pk">
        <!-- {{ review }} -->
        <div><strong>[{{ review.movie_title }}] 관련된 글</strong></div>
        <router-link class="like-review-title" :to="{ name: 'review', params: { reviewPk: review.pk } }">
          <span class="fs-4">{{ review.title }}</span>
        </router-link><br>
        <span><small>last update: </small></span>
        <span><small>{{ review.updated_at.split("-")[0] }}</small></span>/
        <span><small>{{ review.updated_at.split("-")[1] }}</small></span>/
        <span><small>{{ review.updated_at.split("-")[2].split("T")[0] }}</small></span>.
        <span><small>{{ review.updated_at.split("-")[2].split("T")[1].split(":")[0] }}</small></span>:
        <span><small>{{ review.updated_at.split("-")[2].split("T")[1].split(":")[1] }}</small></span>
        <hr>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile'])
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>

<style>
.page-name {
  display: flex;
  justify-content: start;
  margin-left: 10px;
  font-family: 'Noto Sans KR', 'CJONLYONENEW', '맑은 고딕', '돋움', Dotum, sans-serif;
}

.community-ul {
  list-style: none;
}

.review-title {
  text-decoration: none;
  color: orange;
}

.like-review-title{
  text-decoration: none;
  color: red;
}
</style>
