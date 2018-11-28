<template>
  <div class="gotoTop" @click="gotoTop">
    <span class="glyphicon glyphicon-chevron-up"></span>
  </div>
</template>

<script>
export default {
  name: 'gotoTop',
  methods: {
    gotoTop: () => {
      let timer
      let gotoTop = function () {
        let currentPosition = document.documentElement.scrollTop || document.body.scrollTop || window.pageYOffset
        currentPosition -= 10
        if (currentPosition > 0) {
          window.scrollTo(0, currentPosition)
        } else {
          window.scrollTo(0, 0)
          clearInterval(timer)
          timer = null
        }
      }
      timer = setInterval(gotoTop, 1)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .gotoTop{
    position: fixed;
    right: 0.35rem;
    bottom: 1.85rem;
    text-align: center;
    line-height: 1rem;
    height: 1rem;
    width: 1rem;
    border-radius: 50%;
    font-size: 14px;
    color: #49f;
    background: #fff;
    box-shadow: 0 0 1px 1px #888888;
  }
</style>
