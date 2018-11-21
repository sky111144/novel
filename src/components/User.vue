<template>
  <div class="wrapper">
    <Top title="个人中心"></Top>
    <div class="section userinfo-wrapper">
      <div class="user-info">
        <div class="userinfo-top">
          <div class="user-img" :style="'background-image:url(' + userImg + ')'"></div>
          <div class="user-data">
            <dl>
              <dt>阅读币/个</dt>
              <dd>5</dd>
            </dl>
            <em></em>
            <dl>
              <dt>推荐票</dt>
              <dd>3</dd>
            </dl>
            <em></em>
            <dl>
              <dt>藏书</dt>
              <dd>0</dd>
            </dl>
          </div>
        </div>
        <div class="userinfo-bottom">
        </div>
      </div>
    </div>
    <div class="section">
      <ul class="user-service">
        <li class="service-item" v-for="service in services">
          <router-link :to="{ name: service.route, params: {} }">
            <span :class="service.icon"></span>
            <span>
              {{ service.name }}
            </span>
          </router-link>
        </li>
      </ul>
    </div>
    <div class="section logout-wrapper">
      <div class="logout" @click="logout">退出登录</div>
    </div>
    <Bottom></Bottom>
  </div>
</template>

<script>
import Top from './common/Header'
import Bottom from './common/Footer'
export default {
  name: 'User',
  data () {
    return {
      userImg: 'http://m.shenqiwang.cn/styles/images/default/default-user.jpg',
      services: [
        {
          name: '我的书架',
          icon: 'glyphicon glyphicon-book',
          route: 'Shelf'
        },
        {
          name: '我的评论',
          icon: 'glyphicon glyphicon-comment',
          route: 'MyComment'
        },
        // {
        //   name: '我的关注',
        //   icon: 'glyphicon glyphicon-list',
        //   route: 'ChangePassword'
        // },
        {
          name: '我的消息',
          icon: 'glyphicon glyphicon-envelope',
          route: 'MyMessage'
        },
        {
          name: '修改密码',
          icon: 'glyphicon glyphicon-lock',
          route: 'ChangePassword'
        }
      ]
    }
  },
  components: {
    Top: Top,
    Bottom: Bottom
  },
  methods: {
    logout () {
      let api = this.target + '/logout'
      this.$http.post(api)
      .then((res) => {
        if (res.data.status === 'success') {
          this.setCookie('username', null, 0)
          this.setCookie('userId', null, 0)
          this.setCookie('isLogin', null, 0)
          this.$router.push({ name: 'Home' })
        }
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .userinfo-wrapper {
    background-color: #999;
  }
  .user-info {
    padding: 1rem 0;
  }
  .userinfo-top {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
  }
  .user-img {
    height: 2rem;
    width: 2rem;
    border-radius: 50%;
    background-size: cover;
    background-repeat: no-repeat;
  }
  .user-data {
    display: flex;
    flex-direction: row;
    align-items: center;
    height: 2.5rem;
    text-align: center;
    color: #fff;
  }
  .user-data dl {
    padding: 0 0.5rem;
  }
  .user-service {
    margin-bottom: 0.5rem;
  }
  .service-item {
    font-size: 14px;
    line-height: 1.25rem;
    height: 1.25rem;
    border-bottom: 1px solid #ededed;
    margin-bottom: 0.05rem;
  }
  .service-item:last-child {
    border-bottom: none;
  }
  .logout-wrapper {
    padding-top: 0.5rem;
    padding-bottom: 1.5rem;
  }
  .logout {
    line-height: 1.25rem;
    height: 1.25rem;
    text-align: center;
    border-radius: 3px;
    color: #fff;
    background-color: #3498db;
  }
</style>
