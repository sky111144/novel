import Vue from 'vue'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false
Vue.config.productionTip = false
Vue.prototype.$http = axios
Vue.prototype.$http.defaults.withCredentials = true
Vue.prototype.target = 'http://localhost:8000'
Vue.prototype.getCookie = (name) => {
  const v = window.document.cookie.match(`(^|;) ?${name}=([^;]*)(;|$)`)
  return v ? v[2] : null
}
Vue.prototype.setCookie = (name, value, days) => {
  const d = new Date()
  d.setTime(d.getTime() + 24 * 60 * 60 * 1000 * days)
  window.document.cookie = `${name}=${value};path=/;expires=${d.toGMTString()}`
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
