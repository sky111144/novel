<template>
  <div class="wrapper">
    <Top title="修改密码"></Top>
    <div class="section user-form">
      <input type="password" class="user-input" placeholder="用户名" v-model="username">
      <input type="password" class="user-input" placeholder="请输入旧密码" v-model="oldPassword">
      <input type="password" class="user-input" placeholder="请输入新密码" v-model="newPassword">
      <input type="password" class="user-input" placeholder="请重复新密码" v-model="repeat">
      <input type="button" class="user-btn" value="立即修改" @click="changePassword">
    </div>
    <Bottom></Bottom>
  </div>
</template>

<script>
import Top from '../components/Header'
import Bottom from '../components/Footer'
export default {
  name: 'ChangePassword',
  data () {
    return {
      username: null,
      oldPassword: null,
      newPassword: null,
      repeat: null
    }
  },
  components: { Top, Bottom },
  methods: {
    changePassword () {
      if (this.newPassword !== this.repeat) {
        return null
      }
      let api = this.target + '/changePassword'
      this.$http.post(api, {
        username: this.username,
        oldPassword: this.oldPassword,
        newPassword: this.newPassword
      }).then((res) => {
        console.log(res.data.msg)
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
