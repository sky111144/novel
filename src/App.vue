<template>
  <div id="app">
    <router-view :key="$route.path"></router-view>
    <GotoTop></GotoTop>
  </div>
</template>

<script>
import GotoTop from './components/common/GotoTop'
export default {
  name: 'app',
  components: {
    'GotoTop': GotoTop
  }
}
</script>

<style>
#app {
  position: relative;
  overflow: hidden;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 0;
}
body, h1, h2, h3, h4, h5, ul, p, dl{
  margin: 0;
}
h1, h2, h3, h4, h5{
  color: #999;
}
ul {
  padding-left: 0;
}
li{
  list-style-type: none;
}
a, a:focus, a:hover{
  color: #999;
  text-decoration: none;
}
.blue{
  background: #3498db;
}
.section{
  padding: 0 0.35rem;
  background: #fff;
}
.text-overflow {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.flexbox-justify-around {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}
.user-form {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  margin-top: 1rem;
}
.user-input {
  display: block;
  border-top: none;
  border-left: none;
  border-right: none;
  border-bottom: 1px solid #ededed;
  padding-bottom: 0.35rem;
  margin: 0.35rem 0.25rem;
  outline: none;
}
.user-btn {
  display: block;
  height: 1.25rem;
  margin: 0.5rem 0;
  border: none;
  outline: none;
  border-radius: 4px;
  color: #fff;
  background-color: #3498db;
}
</style>
