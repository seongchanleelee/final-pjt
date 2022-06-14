<template>
  <div>
    <h1 class="mx-4">Login</h1>

    <b-card v-if="authError" title="로그인 정보가 정확하지 않습니다" class="mx-4" style="max-width: 30rem;">
      <b-card-text>
        <account-error-list v-if="authError"></account-error-list>
      </b-card-text>
    </b-card>


    <b-form @submit.prevent="login(credentials)" @reset="onReset" class="mx-4 my-2">
      <b-form-group id="username" label="username:" label-for="username">
        <b-form-input id="username" v-model="credentials.username" type="text" placeholder="Enter Username" required></b-form-input>
      </b-form-group>
      <!-- <div>
        <label for="username">username: </label>
        <input v-model="credentials.username" type="text" id="username" required />
      </div> -->

      <b-form-group id="password" label="password:" label-for="password">
        <b-form-input id="password" v-model="credentials.password" type="password" placeholder="Enter password" required></b-form-input>
      </b-form-group>
      <!-- <div>
        <label for="password">password: </label>
        <input v-model="credentials.password" type="password" id="password" required />
      </div> -->

      <!-- <button>Login</button> -->
      <b-button class="mt-2" type="submit" variant="primary">Submit</b-button>
      <b-button class="mx-2 mt-2" type="reset" variant="danger">Reset</b-button>
    </b-form>
    
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login']),
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.credentials.username = ''
        this.credentials.password = ''
      }
    },
  }
</script>

<style></style>
