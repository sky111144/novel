<template>
  <div class="section">
    <ul class="swiper">
      <li class="swiper-item" :style="{left: item.cur*9.3 + 'rem', backgroundImage: 'url(' + item.image + ')' }" v-for="item in slide"></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Swiper',
  data () {
    return {
      curSlide: 0,
      slide: [
        {
          id: 0,
          cur: 0,
          image: 'https://qidian.qpic.cn/qidian_common/349573/d232bf25655f29abb0054ff1bbaf0f45/0'
        },
        {
          id: 1,
          cur: 1,
          image: 'https://qidian.qpic.cn/qidian_common/349573/95a256b6ed61c21a50993a58d69fc342/0'
        },
        {
          id: 2,
          cur: 2,
          image: 'https://qidian.qpic.cn/qidian_common/349573/27684190fa05f6baece8ed8efb5a483c/0'
        },
        {
          id: 3,
          cur: 3,
          image: 'https://qidian.qpic.cn/qidian_common/349573/6f16473018a8f30ccf876311448582ac/0'
        }
      ]
    }
  },
  methods: {
    linear: (time, begin, change, duration) => {
      return begin - change * time / duration
    },
    move: (vm, time, begin, change, duration) => {
      let timer = setInterval(() => {
        vm.slide = vm.slide.map((item, index) => {
          let dif = Math.abs(item.id - item.cur)
          if (dif <= 1) {
            return Object.assign(item, {
              cur: vm.linear(time, item.cur, change, duration)
            })
          } else {
            clearInterval(timer)
            return Object.assign(item, {
              id: item.id - 1
            })
          }
        })
        let result = vm.slide.every((item, index) => {
          let dif = Math.abs(item.id - item.cur)
          if (dif >= 1) {
            return true
          }
          return false
        })
        if (result) {
          setTimeout(() => {
            vm.curSlide++
            if (vm.curSlide < vm.slide.length - 1) {
              vm.move(vm, time, begin, change, duration)
            } else {
              vm.curSlide = 0
              vm.slide = vm.slide.map((item, index) => {
                return Object.assign(item, {
                  id: index,
                  cur: index
                })
              })
              vm.move(vm, time, begin, change, duration)
            }
          }, 3000)
        }
      }, 16)
    }
  },
  mounted () {
    this.move(this, 1000, 0, 0.02, 1000)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .section{
    display: flex;
    justify-content: center;
  }
  .swiper {
    position: relative;
    height: 4rem;
    width: 100%;
    padding-top: 0.5rem;
    overflow: hidden;
    z-index: 0
  }
  .swiper-item {
    position: absolute;
    height: 3.5rem;
    width: 100%;
    overflow: hidden;
    background-size: cover;
    background-repeat: no-repeat;
  }
</style>
