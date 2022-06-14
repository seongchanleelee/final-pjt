<template>
  <div>
    <p class="fs-4 fw-bold mt-3 mx-3">[{{ review.movie_title }}] {{ review.title }}</p>

    <hr>
    <p class="fw-bold fs-5 mt-3 mx-3">
      {{ review.content }}
    </p>
    <!-- Review Edit/Delete UI -->
    <div v-if="isAuthor">
      <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
        <button class="button-edit mt-3 mx-3 ">수정</button>
        
      </router-link>
      <button class="button-delete" v-if="!isSpecific" @click="deleteReview(reviewPk)">삭제</button>
      <button class="button-delete" v-if="isSpecific" @click="deleteReview2({reviewPk: reviewPk, movieTitle: review.movie_title })">삭제</button>
    </div>
    <!-- Review Like UI -->
    <div class=" mt-3 mx-3">
      <font-awesome-icon icon="fa-solid fa-heart" style="color:red;"  beat/>
      :
      <button class="button-like"
        @click="likeReview(reviewPk)"
      >{{ likeCount }}</button>
    </div>

    <hr />
    <!-- Comment UI -->
    <comment-list :comments="review.comments"></comment-list>

  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'



  export default {
    name: 'ReviewDetail',
    components: { CommentList },
    data() {
      return {
        reviewPk: this.$route.params.reviewPk,
        isSpecific: this.$route.params.isSpecific,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'review']),
      likeCount() {
        return this.review.like_users?.length
      }
    },
    methods: {
      ...mapActions([
        'fetchReview',
        'likeReview',
        'deleteReview',
        'deleteReview2',
      ])
    },
    created() {
      this.fetchReview(this.reviewPk)
    },
  }
</script>

<style>
.button-edit {
  color: coral;
  background-color: rgb(246, 242, 242);
  border: 2px solid coral;
  outline-color: coral;
  border-radius: 10px;
}

.button-delete {
  color: coral;
  background-color: rgb(246, 242, 242);
  border: 2px solid coral;
  outline-color: coral;
  border-radius: 10px;
}

.button-like {
  color: rgb(246, 242, 242);
  background-color: coral;
  
  border: 2px solid coral;
  outline-color: coral;
  border-radius: 10px;
}
</style>


