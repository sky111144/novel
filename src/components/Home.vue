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
import Top from './common/Header'
import Bottom from './common/Footer'
import Result from './common/Result'
import Swiper from './common/Swiper'
import Navbar from './common/Navbar'
import PicWall from './common/PicWall'
import PicTextWall from './common/PicTextWall'
import SectionTitle from './common/SectionTitle'
export default {
  name: 'Home',
  components: {
    Top: Top,
    Bottom: Bottom,
    Result: Result,
    Swiper: Swiper,
    Navbar: Navbar,
    PicWall: PicWall,
    PicTextWall: PicTextWall,
    SectionTitle: SectionTitle
  },
  data () {
    return {
      books: [],
      picwall: [],
      pictextwall: {}
    }
  },
  mounted () {
    let api = `${this.target}/novel/list/100`
    this.$http.get(api)
    .then((res) => {
      this.books = res.data.data
      this.picwall = [
        this.books.slice(10, 13),
        this.books.slice(14, 17)
      ]
      this.pictextwall = {
        picwall: [this.books.slice(7, 10)],
        list: this.books.slice(0, 7)
      }
    }).catch((error) => {
      console.log(error)
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.wrapper {
  margin: 1.5rem 0;
  background-color: #ededed;
}
.home{
  width: 100%;
}
</style>
