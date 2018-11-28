<template>
  <div class="wrapper">
    <Top title="书架"></Top>
    <Result :books="books"></Result>
    <Bottom></Bottom>
  </div>
</template>

<script>
import Top from '../components/Header.vue'
import Bottom from '../components/Footer.vue'
import Result from '../components/Result.vue'

export default {
  name: 'Shelf',
  data () {
    return {
      query: '',
      books: []
    }
  },
  components: { Top, Bottom, Result },
  mounted () {
    const api = `${this.target}/shelf`
    this.$http.get(api).then((res) => {
      this.books = res.data.data
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
