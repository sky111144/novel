<template>
  <div class="wrapper">
    <Top title="书架"></Top>
    <Result :books="books"></Result>
    <Bottom></Bottom>
  </div>
</template>

<script>
import Top from './common/Header'
import Bottom from './common/Footer'
import Result from './common/Result'
export default {
  name: 'Shelf',
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
  mounted () {
    let api = this.target + '/shelf'
    this.$http.get(api)
    .then((res) => {
      this.books = res.data.data
      console.log(this.books)
    }).catch((error) => {
      console.log(error)
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
