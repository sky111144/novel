<template>
  <div class="section">
    <ul class="types">
      <li class="type" v-for="type in types">
        <router-link class="type-content" :to="{ name: '', params: {} }">
          <span class="type-icon" :class="type.icon"></span>
          {{ type.name }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'navbar',
  data () {
    return {
      types: [
        {
          name: '书库',
          icon: 'glyphicon glyphicon-th-large'
        },
        {
          name: '分类',
          icon: 'glyphicon glyphicon-th-list'
        },
        {
          name: '排行',
          icon: 'glyphicon glyphicon-align-justify'
        },
        {
          name: '足迹',
          icon: 'glyphicon glyphicon-bookmark'
        },
        {
          name: '签到',
          icon: 'glyphicon glyphicon-leaf'
        }
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .types{
    display: flex;
    justify-content: space-between;
    padding: 0.25rem 0;
    margin-bottom: 0.5rem;
  }
  .type {
    height: 1.55rem;
    width: 1.55rem;
  }
  .type:hover{
    background-color: #ededed;
  }
  .type-content{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 1.55rem;
    width: 1.55rem;
  }
  .type-icon {
    margin-bottom: 0.35rem;
  }
</style>
