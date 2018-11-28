<template>
  <div class="wrapper">
    <Top title="注册"></Top>
    <div class="section user-form">
      <input type="text" class="user-input" placeholder="请输入用户名" v-model="username">
      <input type="text" class="user-input" placeholder="请输入邮箱" v-model="email">
      <input type="password" class="user-input" placeholder="请输入密码" v-model="password">
      <input type="password" class="user-input" placeholder="请重复密码" v-model="repeat">
      <input type="button" class="user-btn" value="立即注册" @click="register">
    </div>
    <Bottom></Bottom>
  </div>
</template>

<script>
import Top from '../components/Header.vue'
import Bottom from '../components/Footer.vue'

export default {
  name: 'Register',
  data () {
    return {
      username: null,
      password: null,
      email: null,
      repeat: null
    }
  },
  components: { Top, Bottom },
  methods: {
    register () {
      if (this.password !== this.repeat) {
        return null
      }
      const api = `${this.target}/register`
      this.$http.post(api, {
        username: this.username,
        password: this.password,
        email: this.email
      }).then((res) => {
        if (res.data.status === 'success') {
          this.$router.push({ name: 'Login' })
        }
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
