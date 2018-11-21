<template>
  <div class="section">
    <h4 class="section-title">
      {{ title }}
    </h4>
  </div>
</template>

<script>
export default {
  name: 'title',
  props: ['title']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.section {
  padding: 0.5rem 0.5rem 0 0.5rem;
}
.section-title {
  font-size: 16px;
  padding: 0.15rem 0.2rem;
  border-left: 3px solid #49f;
}
</style>
