// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
Vue.prototype.$http = axios
Vue.prototype.$http.defaults.withCredentials = true
// Vue.prototype.target = 'http://localhost:8000'
Vue.prototype.target = '//193.112.57.247'
Vue.prototype.getCookie = (name) => {
  let v = window.document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)')
  return v ? v[2] : null
}
Vue.prototype.setCookie = (name, value, days) => {
  let d = new Date()
  d.setTime(d.getTime() + 24 * 60 * 60 * 1000 * days)
  window.document.cookie = name + '=' + value + ';path=/;expires=' + d.toGMTString()
}
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
