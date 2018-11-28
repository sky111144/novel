<template>
  <div class="tips">
    {{ message }}
  </div>
</template>

<script>
export default {
  name: 'Tips',
  props: ['message']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .tips {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;
    text-align: center;
    width: 2rem;
    line-height: 2rem;
    height: 2rem;
    border-radius: 7px;
    background-color: #ededed;
  }
</style>
