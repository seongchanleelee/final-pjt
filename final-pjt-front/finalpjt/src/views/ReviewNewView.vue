<template>
  <div>
    <h3 class="new-writing">새로운 글 쓰기</h3>
    <hr>
    <review-form :review="review" action="create"></review-form>

  </div>
</template>

<script>
  import ReviewForm from '@/components/ReviewForm.vue'
  export default {
    name: 'ReviewNewView',
    components: { ReviewForm },
    data() {
      return {
        review: {
          pk: null,
          movie_title: '',
          title: '',
          content: '',
        }
      }
    },
  }
</script>

<style>
.new-writing {
  color: black;
  text-align: center;
  margin-top: 15px;
}
</style>
