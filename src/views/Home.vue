<template>
  <div class="wrapper">
    <Top title="未来中文网"></Top>
    <div class="home">
      <Swiper></Swiper>
      <Navbar></Navbar>
      <SectionTitle title="主编强推"></SectionTitle>
      <Result :books="books.slice(0,5)"></Result>
      <SectionTitle title="精品推荐"></SectionTitle>
      <PicWall :picwall="picwall"></PicWall>
      <SectionTitle title="火热新书"></SectionTitle>
      <PicTextWall :pictextwall="pictextwall"></PicTextWall>
    </div>
    <Bottom></Bottom>
  </div>
</template>

<script>
import Top from '../components/Header'
import Bottom from '../components/Footer'
import Result from '../components/Result'
import Swiper from '../components/Swiper'
import Navbar from '../components/Navbar'
import PicWall from '../components/PicWall'
import PicTextWall from '../components/PicTextWall'
import SectionTitle from '../components/SectionTitle'
export default {
  name: 'Home',
  components: { Top, Bottom, Result, Swiper, Navbar, PicWall, PicTextWall, SectionTitle },
  data () {
    return {
      books: [],
      picwall: [],
      pictextwall: {}
    }
  },
  mounted () {
    const api = `${this.target}/novel/list/100`
    this.$http.get(api).then((res) => {
      this.books = res.data.data
      this.picwall = [
        this.books.slice(10, 13),
        this.books.slice(14, 17)
      ]
      this.pictextwall = {
        picwall: [this.books.slice(7, 10)],
        list: this.books.slice(0, 7)
      }
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.wrapper {
  margin: 1.2rem 0;
  background-color: #ededed;
}
.home{
  width: 100%;
}
</style>
