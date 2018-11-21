<template>
  <div class="wrapper">
    <Top title="登录"></Top>
    <div class="section user-form">
      <input type="text" class="user-input" placeholder="请输入帐号" v-model="username">
      <input type="password" class="user-input" placeholder="请输入密码" v-model="password">
      <input type="button" class="user-btn" value="立即登录" @click="login">
    </div>
    <div class="section register">
      <router-link :to="{ name: 'Register', params: {} }">
        注册
      </router-link>
      <router-link :to="{ name: '', params: {} }">
        忘记密码？
      </router-link>
    </div>
    <Bottom></Bottom>
  </div>
</template>

<script>
import Top from './common/Header'
import Bottom from './common/Footer'
export default {
  name: 'Login',
  data () {
    return {
      username: null,
      password: null
    }
  },
  components: {
    Top: Top,
    Bottom: Bottom
  },
  methods: {
    login () {
      let api = this.target + '/login'
      this.$http.post(api, { username: this.username, password: this.password })
      .then((res) => {
        if (res.data.status === 'success') {
          this.$router.push({ name: 'User' })
        } else {
          console.log(res.data.msg)
        }
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.register {
  display: flex;
  justify-content: space-between;
}
</style>
