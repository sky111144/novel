<template>
  <div class="section">
    <h4 class="section-title">
      {{ title }}
    </h4>
  </div>
</template>

<script>
export default {
  name: 'titles',
  props: ['title']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.section {
  padding: 0.35rem 0.25rem 0 0.25rem;
}
.section-title {
  font-size: 16px;
  padding: 0.15rem 0.2rem;
  border-left: 3px solid #49f;
}
</style>
