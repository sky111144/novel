<template>
  <div class="section">
    <div class="bookInfo-wrapper">
      <div class="book-img" :style="'background-image: url(' + info.img + ')'"></div>
      <div class="book-info">
        <div class="book-name">
          {{ info.name }}
        </div>
        <div class="bookInfo-item">
          作者：{{ info.author }}
        </div>
        <div class="bookInfo-item">
          章节：
          <span class="glyphicon glyphicon-fire lastUpdate"></span>
          {{ info.lastUpdate.name }}
        </div>
        <div class="bookInfo-item">
          类型：暂无
        </div>
      </div>
    </div>
    <div class="bookInfo-btns">
      <router-link class="bookInfo-btn active" :to="{ name: '', params: {} }">
        开始阅读
      </router-link>
      <router-link class="bookInfo-btn" :to="{ name: 'Comment', params: { novelId : novelId } }">
        评价
      </router-link>
      <router-link class="bookInfo-btn" :to="{ name: '', params: {} }">
        投票
      </router-link>
      <a class="bookInfo-btn" @click="collectNovel">
        加入书架
      </a>
    </div>
    <div class="bookInfo-intro">
      {{ info.intro === '' ? '暂无简介' : `简介：${info.intro}` }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'BookInfo',
  props: ['info'],
  data () {
    return {
      novelId: this.$route.params.novelId
    }
  },
  methods: {
    collectNovel () {
      let api = this.target + '/collect/' + this.novelId
      this.$http.get(api).then((res) => {
        if (res.data.status === 'success') {
          console.log(res.data.msg)
        } else {
          console.log(res.data.msg)
        }
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .bookInfo-wrapper {
    display: flex;
    flex-direction: row;
    padding: 0.25rem 0;
  }
  .book-img {
    height: 3rem;
    width: 2.3rem;
    margin-right: 0.5rem;
    background-size: cover;
  }
  .book-name {
    font-size: 14px;
    width: 2rem;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .bookInfo-item{
    margin: 0.2rem 0;
    font-size: 12px;
    color: #929292;
  }
  .lastUpdate {
    color: red;
  }
  .bookInfo-btns {
    display: flex;
    justify-content: space-between;
    padding-bottom: 0.25rem;
    border-bottom: 1px solid #ededed;
  }
  .bookInfo-btn.active {
    color: #fff;
    background-color: #49f;
  }
  .bookInfo-btn {
    text-align: center;
    line-height: 0.8rem;
    height: 0.8rem;
    width: 23%;
    border: 1px solid #ededed;
    border-radius: 5px;
    font-size: 12px;
  }
  .bookInfo-intro {
    padding: 0.25rem 0.15rem;
    border-bottom: 1px solid #ededed;
    color: #939393;
  }
</style>
