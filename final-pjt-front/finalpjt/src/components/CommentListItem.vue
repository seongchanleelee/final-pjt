<template>
  <li class="comment-list-item mt-2">
    <router-link class="username fw-bold" :to="{ name: 'profile', params: { username: comment.user.username } }">
      {{ comment.user.username }}
    </router-link>: 
    
    <span v-if="!isEditing">{{ payload.content }}</span>

    <span v-if="isEditing">
      <input class="editing-input" type="text" v-model="payload.content">
      <button class="button mx-3" @click="onUpdate">수정</button> 
      <button class="button" @click="switchIsEditing">삭제</button>
    </span>
  <!-- 댓글 좋아요 버튼 추가 -->
    <span v-if="currentUser.username === comment.user.username && !isEditing">
      <button class="button mx-2" @click="switchIsEditing">수정</button> 
      <button class="button mx-3" @click="deleteComment(payload)">삭제</button>
    </span>

     <!-- Review Like UI -->
    <span>
       <font-awesome-icon class="mx-2" style="color:red;" icon="fa-solid fa-heart" beat/>:
      <button class="button" @click="likeComment(payload)">{{ likeCount }}</button>
    </span>
  </li>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        reviewPk: this.comment.review,
        commentPk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser', 'com']),
    likeCount() {
        return this.comment.like_users?.length
    }
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment', 'likeComment', 'fetchComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },
  created() {
    this.fetchComment(this.payload)
  }

}
</script>

<style>
.comment-list-item {
  list-style: none;

}

.username {
  text-decoration: none;
  color: black;
}

.button {
  border-radius: 10px;
  background-color: coral;
  border: 2px coral;
  color: white;
}

.editing-input {
  background-color: rgb(246, 242, 242);
  border: 2px solid rgb(243, 112, 64);
  outline-color: rgb(243, 112, 64);
  border-radius: 10px;
}
</style>