<template>
  <footer>
    <div>
      <router-link class="bar-item" :to="{ name: 'Home' }">
        <span class="glyphicon glyphicon-home"></span>
        书城
      </router-link>
    </div>
    <div class="bar-item" @click="gotoUserPage">
      <span class="glyphicon glyphicon-user"></span>
      个人
    </div>
    <Tips :message="message" v-if="message"></Tips>
  </footer>
</template>

<script>
import Tips from './Tips'
export default {
  name: 'bottom',
  data () {
    return {
      infos: [],
      message: false
    }
  },
  components: { Tips },
  methods: {
    gotoUserPage () {
      console.log(this.getCookie('username'))
      if (this.getCookie('isLogin')) {
        this.message = '已登录'
        this.$router.push({ name: 'User' })
      } else {
        this.message = '未登录'
        this.$router.push({ name: 'Login' })
      }
      setTimeout(() => {
        this.message = false
      }, 1000)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  footer{
    position: fixed;
    bottom: 0;
    left: 0;

    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;

    height: 1.2rem;
    width: 100%;
    color: #49f;

    background: #eee;
  }
  .bar-item {
    color: #49f;
  }
</style>
