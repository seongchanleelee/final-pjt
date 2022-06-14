<template>
  <nav class="navbar navbar-expand-lg bg-danger justify-content-between">
    <div class="icon mx-4">
      <img @click="goHome()" class="icon-img mx-1" width=40px src="@/assets/film.png" alt="icon">
    </div>
    <div class="menu justify-content-end">
      <ul class="nav-ul">
      <li class="nav-li">
        <router-link :to="{ name: 'movies' }" class="text-white text-decoration-none">Home</router-link>
      </li>

      <li v-if="isLoggedIn" class="nav-li">
        <router-link :to="{ name: 'reviews' }" class="text-white text-decoration-none">Community</router-link>
      </li>

      <li v-if="!isLoggedIn" class="nav-li">
        <router-link :to="{ name: 'login' }" class="text-white text-decoration-none">Login</router-link>
      </li>
      <li v-if="!isLoggedIn" class="nav-li">
        <router-link :to="{ name: 'signup' }" class="text-white text-decoration-none">Signup</router-link>
      </li>

      <li v-if="isLoggedIn" class="nav-li">
        <router-link :to="{ name: 'reviewNew' }" class="text-white text-decoration-none">New</router-link>
      </li>
      <li v-if="isLoggedIn" class="nav-li">
        <router-link :to="{ name: 'profile', params: { username } }" class="text-white text-decoration-none">
          {{ currentUser.username }}'s page
        </router-link>
      </li>
      <li v-if="isLoggedIn" class="nav-li">
        <router-link :to="{ name: 'logout' }" class="text-white text-decoration-none">Logout</router-link>
      </li>
    </ul>
    </div>
  </nav>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
    methods: {
      goHome(){
        this.$router.push({ name: 'movies' })
      }
    },
  }
</script>

<style>
nav {
  background: linear-gradient(to right, red,orange)
}

.nav-ul{
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-li{
  margin: 0 0 0 0;
  margin-left: 10px;
  margin-right: 10px;
  margin-top: 10px;
  margin-bottom: 10px;
  padding: 0 0 0 0;
  border : 0 0 0 0;
  float: left;
}
.a{ 
  margin: 10;

}

</style>
