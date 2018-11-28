<template>
  <div class="wrapper">
    <Top :title="this.info.name"></Top>
    <div class="novel">
      <BookInfo :info="info"></BookInfo>
      <div class="section">
        <ul class="charpts">
          <li class="charpt" v-for="(charpt, cId) in charpts" :key="cId">
            <router-link :to="{ name: 'Charpt', params: { novelId: novelId, charptId: charpt.id } }">
              {{ charpt.name }}
            </router-link>
          </li>
        </ul>
        <Loading v-if="isShowLoading"></Loading>
      </div>
    </div>
    <Bottom></Bottom>
  </div>
</template>

<script>
import { throttle } from 'lodash'
import Top from '../components/Header.vue'
import Bottom from '../components/Footer.vue'
import BookInfo from '../components/BookInfo.vue'
import Loading from '../components/Loading.vue'
export default {
  name: 'Novel',
  data () {
    return {
      novelId: parseInt(this.$route.params.novelId),
      charpts: [],
      info: {
        id: null,
        lastUpdate: {}
      },
      curPages: [],
      pageSize: 10,
      isShowLoading: false,
      isLoad: false
    }
  },
  components: { Top, Bottom, BookInfo, Loading },
  methods: {
    requestCharpts () {
      const nextPage = this.charpts.length / this.pageSize + 1
      console.time(`请求数据：第${nextPage}页耗时`)
      console.log(`开始请求数据：第${nextPage}页`)

      // 防止重复请求书页
      if (this.curPages.indexOf(nextPage) !== -1) {
        console.log(`第${nextPage}页已经请求，不予重复请求`)
        return null
      }
      const api = `${this.target}/novel/${this.novelId}?page=${nextPage}&size=${this.pageSize}`
      this.$http.get(api).then((res) => {
        if (this.novelId === res.data.info.id) {
          // 记录已请求书页,防止重复请求
          this.curPages.push(nextPage)
          // 更新章节数据
          this.charpts = this.charpts.concat(res.data.charpts)
          // 防止小说数据丢失
          this.info = Object.assign({}, res.data.info)
          // 关闭加载动画
          this.isShowLoading = false
          // 允许请求下一页数据
          this.isLoad = false
          console.log('结束请求数据：第' + nextPage + '页', this.charpts)
          console.timeEnd('请求数据：第' + nextPage + '页耗时')
        }
      }).catch(() => {
        // 允许请求下一页数据
        this.isLoad = false
      })
    },
    pullRequest () {
      // 如果已请求书页数据，但未收到响应，则阻止此次请求
      if (this.isLoad) {
        return null
      }
      // 节流，防止对服务器产生过大载荷
      const request = throttle(() => {
        // 声明已经发出请求
        this.isLoad = true
        // 防止scroll绑定事件影响其他页面
        if (this.$route.name !== 'Novel') {
          window.removeEventListener('scroll', request)
          window.removeEventListener('scroll', this.isBottom)
          return null
        }
        // 判断是否下拉到底
        const currentPosition = document.documentElement.scrollTop || document.body.scrollTop || window.pageYOffset
        const targetPosition = document.body.clientHeight - window.innerHeight - 50
        if (currentPosition > targetPosition) {
          // 下拉加载下一页数据
          this.requestCharpts()
        }
      }, 1800)
      return request
    },
    isBottom () {
      if (this.$route.name !== 'Novel') {
        window.removeEventListener('scroll', this.isBottom)
        return null
      }

      const currentPosition = document.documentElement.scrollTop || document.body.scrollTop || window.pageYOffset
      const targetPosition = document.body.clientHeight - window.innerHeight - 50
      if (currentPosition >= targetPosition) {
        this.isShowLoading = true
        // console.log('当前位置：' + currentPosition + '  目标位置：' + targetPosition)
      }
    }
  },
  mounted () {
    const vm = this
    const request = vm.pullRequest()
    request()
    // 绑定滚动请求事件
    window.addEventListener('scroll', request)
    // 节流函数不会立刻执行请求，需要此函数判断是否显示加载动画
    window.addEventListener('scroll', vm.isBottom)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.charpt{
  padding: 0.2rem;
  border-bottom: 1px solid #ededed;
  background-color: #fff;
  font-size: 14px;
}
</style>
