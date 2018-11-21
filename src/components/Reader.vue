<template>
  <div class="wrapper">
    <Top :title="username"></Top>
    <div class="section reader-info-wraper">
      <div class="reader-img" :style="`background-image: url(${readerImg})`"></div>
      <div class="reader-info">
        <div class="">
          昵称：{{ username }}
        </div>
        <div class="">
          等级：1级
        </div>
        <div class="">
          阅龄：1年
        </div>
      </div>
    </div>
    <div class="section">
      <div class="bookInfo-btns">
        <div class="bookInfo-btn active">
          动态
        </div>
        <div class="bookInfo-btn" @click="gotoSendMessage">
          私信
        </div>
        <div class="bookInfo-btn">
          关注
        </div>
        <div class="bookInfo-btn">
          粉丝
        </div>
      </div>
    </div>
    <div class="section reader-comment">

    </div>
    <div class="reader-selection">

    </div>
    <Bottom></Bottom>
  </div>
</template>

<script>
import Top from './common/Header'
import Bottom from './common/Footer'
export default {
  name: 'Reader',
  components: {
    Top: Top,
    Bottom: Bottom
  },
  data () {
    return {
      readerImg: 'http://m.shenqiwang.cn/styles/images/default/default-user.jpg',
      userId: this.$route.params.userId,
      username: null,
      password: null
    }
  },
  methods: {
    gotoSendMessage () {
      let userId = this.userId
      this.$router.push({name: 'Message', params: { userId: userId }})
    }
  },
  mounted () {
    this.$http.get(`${this.target}/user/${this.$route.params.userId}`)
    .then((res) => {
      this.username = res.data.data.username
    })
    .catch((err) => {
      console.log(err)
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .reader-info-wraper {
    display: flex;
    flex-direction: row;
    color: #929292;
    padding: 0.5rem 0.35rem;
  }
  .reader-img {
    height: 2rem;
    width: 2rem;
    border-radius: 50%;
    margin: 0 0.5rem;
    background-size: cover;
  }
  .reader-info {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
  }
  .bookInfo-btns {
    display: flex;
    justify-content: space-around;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #ededed;
  }
  .bookInfo-btn.active {
    color: #fff;
    background-color: #49f;
  }
  .bookInfo-btn {
    text-align: center;
    line-height: 0.9rem;
    height: 0.9rem;
    width: 2rem;
    border: 1px solid #ededed;
    border-radius: 5px;
    font-size: 12px;
  }

</style>
