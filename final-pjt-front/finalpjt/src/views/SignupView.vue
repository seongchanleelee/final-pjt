<template>
  <div>
    <h1 class="mx-4">Signup</h1>

    <b-card v-if="authError" title="회원정보가 정확하지 않습니다" class="mx-4" style="max-width: 30rem;">
      <b-card-text>
        <account-error-list v-if="authError"></account-error-list>
      </b-card-text>
    </b-card>

    <!-- <account-error-list v-if="authError"></account-error-list> -->
    <b-form @submit.prevent="signup(credentials)" @reset="onReset" class="mx-4 my-2">
      <b-form-group id="username" label="Username:" label-for="username">
        <b-form-input id="username" v-model="credentials.username" type="text" placeholder="Enter Username" required></b-form-input>
      </b-form-group>
      <!-- <div>
        <label for="username">Username: </label>
        <input  v-model="credentials.username" type="text" id="username" required/>
      </div> -->
      <b-form-group id="password1" label="Password:" label-for="password1">
        <b-form-input id="password1" v-model="credentials.password1" type="password" placeholder="Enter password" required></b-form-input>
      </b-form-group>
      <!-- <div>
        <label for="password1">Password: </label>
        <input v-model="credentials.password1" type="password" id="password1" required />
      </div> -->
      <b-form-group id="password2" label="Password Confirmation: " label-for="password2">
        <b-form-input id="password2" v-model="credentials.password2" type="password" placeholder="Enter password again" required></b-form-input>
      </b-form-group>
      <!-- <div>
        <label for="password2">Password Confirmation:</label>
        <input v-model="credentials.password2" type="password" id="password2" required />
      </div> -->
      <div>
        <b-button class="mt-2" type="submit" variant="primary">Signup</b-button>
        <b-button class="mx-2 mt-2" type="reset" variant="danger">Reset</b-button>
      </div>
    </b-form>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup']),
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.credentials.username = ''
        this.credentials.password1 = ''
        this.credentials.password2 = ''
      }
    },
  }
</script>

<style></style>
