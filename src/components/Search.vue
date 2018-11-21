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
import Top from './common/Header'
import Bottom from './common/Footer'
import Result from './common/Result'
export default {
  name: 'Search',
  data () {
    return {
      query: '',
      books: []
    }
  },
  components: {
    Top: Top,
    Bottom: Bottom,
    Result: Result
  },
  watch: {
    query () {
      if (this.query.replace(/^\s+|\s+$/gm, '').length > 0) {
        let api = this.target + '/search?query=' + this.query
        this.$http.get(api).then((res) => {
          this.books = res.data
          console.log(this.books)
        }).catch((error) => {
          console.log(error)
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
  width: 90%;
  border: none;
  margin: 0.25rem 0.5rem;
  padding: 0 0.25rem;
  outline: none;
}
</style>
