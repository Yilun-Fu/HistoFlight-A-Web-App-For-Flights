<template>
  <v-content>
    <div class="staticHero">
      <v-img src="../assets/image/comments.jpg" height="400">
        <v-row align="end" class="lightbox white--text pa-2 fill-height">
          <v-col>
            <v-container>
              <div class="headline">Post Your Comments</div>
            </v-container>
          </v-col>
        </v-row>
      </v-img>
    </div>

    <div class="block">
      <v-container>
        <validation-observer ref="observer" v-slot="{ invalid }">
          <form @submit.prevent="submit">
            <validation-provider v-slot="{ errors }" name="Name" rules="required|max:10">
              <v-text-field v-model="name" :counter="10" :error-messages="errors" label="Name" required></v-text-field>

            </validation-provider>
            <validation-provider v-slot="{ errors }" name="email" rules="required|email">
              <v-text-field v-model="email" :error-messages="errors" label="E-mail" required></v-text-field>
            </validation-provider>
            <validation-provider v-slot="{ errors }" name="select" rules="required">
              <v-select v-model="select" :items="items" :error-messages="errors" label="Select" data-vv-name="select"
                required></v-select>



              <v-textarea counter label="Comment" :rules="rules" :value="value" name="Comment"
                v-model="comments"></v-textarea>

            </validation-provider>
            <validation-provider v-slot="{ errors }" rules="required" name="checkbox">
              <v-checkbox v-model="checkbox" :error-messages="errors" value="1"
                label="I agree with the Terms of Service and Privacy Policy" type="checkbox" required></v-checkbox>
            </validation-provider>

            <v-btn class="mr-4" type="submit" :disabled="invalid">
              submit
            </v-btn>
            <v-btn @click="clear">
              clear
            </v-btn>
          </form>
        </validation-observer>

      </v-container>
    </div>




  </v-content>
</template>

<script>

import { required, digits, email, max, regex } from 'vee-validate/dist/rules'
import { extend, ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'
import axios from "axios"
setInteractionMode('eager')

extend('digits', {
  ...digits,
  message: '{_field_} needs to be {length} digits. ({_value_})',
})

extend('required', {
  ...required,
  message: '{_field_} can not be empty',
})

extend('max', {
  ...max,
  message: '{_field_} may not be greater than {length} characters',
})

extend('regex', {
  ...regex,
  message: '{_field_} {_value_} does not match {regex}',
})

extend('email', {
  ...email,
  message: 'Email must be valid',
})

export default {
  name: 'Comment_post',
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  data: () => ({
    name: '',
    email: '',
    select: null,
    airlineMap: [],
    items: [],
    comments: '',
    checkbox: null,
  }),
  created() {
    this.initialize()
  },
  methods: {
    getData: function () {
      axios.get('/api/airlines').then(resp => {
        this.airlineMap = resp.data;
        this.items = this.airlineMap.map((airline) => {
          return airline.airline_name
        })
      });
    },

    get_user() {
      axios.get('/auth/user', {
        headers: {
          "x-access-tokens": sessionStorage.token
        }
      }).then(response => {
        console.log("response", response.data.message)
        if (response.data.message === 'token is expired'
          || response.data.message === 'token is invalid') {
          sessionStorage.removeItem('token')
          this.$router.push('/login')
        }
        console.log("response ", response)
        this.name = response.data.user_name;
        this.email = response.data.email
      })
    },

    initialize() {
      // console.log("Initialize")
      this.getData()
      this.get_user()
    },
    submit() {
      if (this.$refs.observer.validate()) {
        let IATA = this.airlineMap.filter((airline) => {
          return airline.airline_name === this.select
        })[0].IATA
        let body = {
          text: this.comments,
          user_name: this.name,
          airline: IATA
        }
        // console.log(body)
        axios.post('/api/comment', body, {
          headers: {
            "x-access-tokens": sessionStorage.token
          }
        })
          .then(response => {
            console.log(response);
            this.$router.go()
          })
      }
    },

    clear() {
      this.name = ''
      this.email = ''
      this.select = null
      this.comments = ''
      this.checkbox = null
      this.$refs.observer.reset()
    },
  },
}
</script>
