import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import User from './views/User.vue'
import Comment from './views/Comment.vue'
import MyComment from './views/MyComment.vue'
import Message from './views/Message.vue'
import MyMessage from './views/UserMessage.vue'
import Reader from './views/Reader.vue'
import Shelf from './views/Shelf.vue'
import Novel from './views/Novel.vue'
import Charpt from './views/Charpt.vue'
import Search from './views/Search.vue'
import Login from './views/Login.vue'
import Register from './views/Register.vue'
import ChangePassword from './views/ChangePassword.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/user',
      name: 'User',
      component: User
    },
    {
      path: '/user/:userId',
      name: 'Reader',
      component: Reader
    },
    {
      path: '/message/:userId',
      name: 'Message',
      component: Message
    },
    {
      path: '/comment/:novelId',
      name: 'Comment',
      component: Comment
    },
    {
      path: '/user/comment',
      name: 'MyComment',
      component: MyComment
    },
    {
      path: '/user/message',
      name: 'MyMessage',
      component: MyMessage
    },
    {
      path: '/shelf',
      name: 'Shelf',
      component: Shelf
    },
    {
      path: '/search',
      name: 'Search',
      component: Search
    },
    {
      path: '/novel/:novelId',
      name: 'Novel',
      component: Novel
    },
    {
      path: '/novel/:novelId/:charptId',
      name: 'Charpt',
      component: Charpt
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/changePassword',
      name: 'ChangePassword',
      component: ChangePassword
    }
  ]
})
