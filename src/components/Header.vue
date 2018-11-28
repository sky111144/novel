<template>
  <div>
    <header class="blue">
      <h1 class="title">
        {{ title }}
      </h1>
      <a href="/search">
        <span class="search glyphicon glyphicon-search"></span>
      </a>
    </header>
  </div>
</template>

<script>
export default {
  name: 'top',
  props: ['title']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
header{
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000
}
.title{
  text-align: center;
  line-height: 1.2rem;
  height: 1.2rem;
  font-size: 16px;
  font-weight: 300;
  color: #fff;
}
.search{
  position: absolute;
  right: 0.75rem;

  line-height: 1.2rem;
  height: 1.2rem;

  font-size: 16px;
  color: #fff;
}
.padding{
  height: 1.2rem;
}
</style>
