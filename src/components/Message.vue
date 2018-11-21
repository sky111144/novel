<template>
  <div class="comment-wrapper">
    <span class="glyphicon glyphicon-remove remove" @click.stop.prevent="remove"></span>
    <ul class="section comment-list">
      <li class="comment-item" v-for="comment in messages">
        <div class="comment-top">
          <img class="comment-img" src="http://img.shenqiwang.cn/2017/08/29/9d1451503990881.jpg_60x60" alt="">
          <div class="comment-text">
            <div class="comment-username">
              {{ senderName }}
            </div>
            <div class="comment-time">
              {{ comment.time }}
            </div>
          </div>
        </div>
        <div class="comment-bottom">
          @{{ comment.receiverName }}：{{ comment.message }}
        </div>
      </li>
    </ul>
    <div class="input-group comment">
      <input class="form-control" type="text" v-model="comment">
      <span class="input-group-addon" @click="sendComment">发送</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Comment',
  data () {
    return {
      senderName: this.getCookie('username'),
      comment: '',
      messages: []
    }
  },
  methods: {
    getComment () {
      let api = `${this.target}/message/${this.$route.params.userId}`
      console.log(api)
      this.$http.get(api)
      .then((res) => {
        this.messages = res.data.data
        console.log(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    sendComment () {
      let api = `${this.target}/message/${this.$route.params.userId}`
      console.log(api)
      this.$http.post(api, {
        message: this.comment
      })
      .then((res) => {
        let data = res.data
        if (data.status === 'success') {
          this.getComment()
        }
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    remove () {
      this.$router.go(-1)
    }
  },
  mounted () {
    this.getComment()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  .comment-wrapper {
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    background-color: #ededed;
    z-index: 1001;
    overflow: scroll;
  }
  .comment-list {
    width: 100%;
  }
  .comment-item {
    padding: 0.25rem 0;
    border-bottom:  1px solid #ededed;
  }
  .comment-top {
    display: flex;
    flex-direction: row;
  }
  .comment-img {
    height: 1.25rem;
    width: 1.25rem;
    border-radius: 50%;
  }
  .comment-username {
    padding-top: 0.1rem;
    margin-left: 0.25rem;
  }
  .comment-time {
    color: #929292;
    padding: 0.1rem 0;
    margin-left: 0.25rem;
  }
  .comment-bottom {
    padding: 0.2rem 0.15rem;
    font-size: 14px;
  }
  .remove {
    position: absolute;
    top: 0.5rem;
    right: 0.5rem;
    text-align: center;
    line-height: 0.75rem;
    height: 0.75rem;
    width: 0.75rem;
    border-radius: 50%;
    color: #ededed;
    background-color: #000;
    opacity: 0.75;
  }
  .comment {
    position: fixed;
    bottom: 0.5rem;
    left: 0;
    right: 0;
    margin: 0 auto;
    width: 9.5rem;
  }
</style>
