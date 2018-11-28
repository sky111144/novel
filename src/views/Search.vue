<template>
  <div class="wrapper">
    <Top title="搜索"></Top>
    <form>
      <input class="search" type="text" v-model="query">
    </form>
    <Result :books="books"></Result>
    <Bottom></Bottom>
  </div>
</template>

<script>
import Top from '../components/Header.vue'
import Bottom from '../components/Footer.vue'
import Result from '../components/Result.vue'

export default {
  name: 'Search',
  data () {
    return {
      query: '',
      books: []
    }
  },
  components: { Top, Bottom, Result },
  watch: {
    query () {
      if (this.query.replace(/^\s+|\s+$/gm, '').length > 0) {
        const api = `${this.target}/search?query=${this.query}`
        this.$http.get(api).then((res) => {
          this.books = res.data
        })
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
form{
  display: flex;
  justify-content: center;
}
.search{
  height: 1rem;
  width: 93%;
  border: none;
  margin: 0.25rem 0.05rem;
  padding: 0 0.25rem;
  outline: none;
}
</style>
