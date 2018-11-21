<template>
  <div class="charpt" @click="changeVisiablity">
    <SectionHeader :title="charpt.name" v-show="isShow"></SectionHeader>
    <div class="section charptName-wrapper">
      <div class="charpt-name">
        {{ charpt.name }}
      </div>
    </div>
    <div class="section charpt-content" :style="{minHeight: charptContentHeight}" v-html="charpt.content">
    </div>
    <div class="btn-wrapper">
      <div class="page">
        <router-link class="page-btn" :to="{ name: 'Charpt', params: { novelId: novelId, charptId: charpt.id-1 } }">
          上一章
        </router-link>
        <router-link class="page-btn" :to="{ name: 'Charpt', params: { novelId: novelId, charptId: charpt.id+1 } }">
          下一章
        </router-link>
      </div>
      <div class="charpt-navbar">
        <div class="navbar-item">
          <router-link :to="{ name: 'Home', params: {} }">
            <span class="glyphicon glyphicon-home navbar-item-icon"></span>
            <p class="navbar-item-text">首页</p>
          </router-link>
        </div>
        <div class="navbar-item">
          <router-link :to="{ name: '', params: {} }">
            <span class="glyphicon glyphicon-book navbar-item-icon"></span>
            <p class="navbar-item-text">最近阅读</p>
          </router-link>
        </div>
        <div class="navbar-item">
          <router-link :to="{ name: '', params: {} }">
            <span class="glyphicon glyphicon-yen navbar-item-icon"></span>
            <p class="navbar-item-text">充值</p>
          </router-link>
        </div>
      </div>
    </div>
    <div class="call-navbar" v-show="isShow">
      <div class="callNavbar-top flexbox-justify-around">
        <router-link class="callNavbar-item prev" :to="{ name: 'Charpt', params: { charptId: charpt.id-1 } }">
          上一章
        </router-link>
        <router-link class="callNavbar-item next" :to="{ name: 'Charpt', params: { charptId: charpt.id+1 } }">
          下一章
        </router-link>
      </div>
      <div class="callNavbar-bottom">
        <router-link class="callNavbar-item" :to="{ name: '', params: { } }">
          <div class="callNavbar-item-inner">
            <span class="glyphicon glyphicon-wrench"></span>
            <p class="callNavbar-btnText">
              设置
            </p>
          </div>
        </router-link>
        <router-link class="callNavbar-item" :to="{ name: '', params: { } }">
          <div class="callNavbar-item-inner">
            <span class="glyphicon glyphicon-comment"></span>
            <p class="callNavbar-btnText">
              评论
            </p>
          </div>
        </router-link>
        <router-link class="callNavbar-item" :to="{ name: 'Novel', params: { novelId: novelId } }">
          <div class="callNavbar-item-inner">
            <span class="glyphicon glyphicon-list"></span>
            <p class="callNavbar-btnText">
              目录
            </p>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import SectionHeader from './common/Header'
export default {
  name: 'Charpt',
  data () {
    return {
      charpt: {},
      novelId: this.$route.params.novelId,
      windowHeight: window.innerHeight + 'px',
      charptContentHeight: '0px',
      isShow: false
    }
  },
  components: {
    SectionHeader: SectionHeader
  },
  mounted () {
    let vm = this
    vm.charptContentHeight = (window.innerHeight - document.getElementsByClassName('charpt-name')[0].offsetHeight - document.getElementsByClassName('btn-wrapper')[0].offsetHeight) + 'px'
    console.log(vm.charptContentHeight)
    let api = this.target + '/novel/' + vm.novelId + '/' + vm.$route.params.charptId
    vm.$http.get(api)
    .then((res) => {
      vm.charpt = res.data
    })
    .catch((error) => {
      console.log(error)
    })
  },
  methods: {
    changeVisiablity () {
      this.isShow = !this.isShow
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.section {
  position: relative;
  background-color: #e8e5df;
}
.call-navbar {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #000;
  opacity: 0.83;
}
.callNavbar-item {
  display: inline-block;
  width: 33%;
  text-align: center;
  color: #fff;
}
.callNavbar-item-inner {
  display: flex;
  flex-direction: column;
}
.callNavbar-bottom{
  display: flex;
  flex-direction: row;
  align-items: center;
  height: 2rem;
}
.callNavbar-btnText{
  margin-top: 0.25rem;
  font-size: 14px;
}
.callNavbar-item-inner > span {
  font-size: 14px;
}
.prev, .next{
  font-size: 14px;
  line-height: 1.5rem;
  height: 1.5rem;
}
.charpt{
  padding: 0 0.25rem;
  background-color: #e8e5df;
}
.charpt-name{
  line-height: 2rem;
  height: 2rem;
  text-align: center;
  font-size: 20px;
  font-weight: bold;
  color: #8e5435;
}
.charpt-content{
  color: #262626;
  font-size: 14px;
}
.page{
  display: flex;
  justify-content: space-around;
  font-size: 14px;
  height: 1.5rem;
}
.page-btn {
  color: #333;
}
.charpt-navbar {
  display: flex;
  justify-content: space-around;
  text-align: center;
  padding-bottom: 1rem;
}
.navbar-item {
  display: flex;
  flex-direction: column;
  justify-content: center;
  font-size: 14px;
}
.navbar-item-icon {
  color: #333;
}
.navbar-item-text {
  margin-top: 0.15rem;
  color: #333;
}
</style>
