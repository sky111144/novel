import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import User from '@/components/User'
import Comment from '@/components/Comment'
import MyComment from '@/components/MyComment'
import Message from '@/components/Message'
import MyMessage from '@/components/UserMessage'
import Reader from '@/components/Reader'
import Shelf from '@/components/Shelf'
import Novel from '@/components/Novel'
import Charpt from '@/components/Charpt'
import Search from '@/components/Search'
import Login from '@/components/Login'
import Register from '@/components/Register'
import ChangePassword from '@/components/ChangePassword'

Vue.use(Router)

export default new Router({
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
