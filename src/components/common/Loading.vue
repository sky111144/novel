<template>
  <div class="loading">
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
  </div>
</template>

<script>
export default {
  name: 'Loading'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.loading{
    width: 4.5rem;
    height: 0.65rem;
    margin: 0.25rem auto 1.75rem auto;
}
.loading span{
    display: inline-block;
    width: 0.65rem;
    height: 100%;
    margin-right: 0.15rem;
    border-radius: 50%;
    background: #49f;
    -webkit-animation: load 1.04s ease infinite;
}
.loading span:last-child{
    margin-right: 0;
}
@-webkit-keyframes load{
    0%{
        opacity: 1;
    }
    100%{
        opacity: 0;
    }
}
.loading span:nth-child(1){
    -webkit-animation-delay:0.13s;
}
.loading span:nth-child(2){
    -webkit-animation-delay:0.26s;
}
.loading span:nth-child(3){
    -webkit-animation-delay:0.39s;
}
.loading span:nth-child(4){
    -webkit-animation-delay:0.52s;
}
.loading span:nth-child(5){
    -webkit-animation-delay:0.65s;
}
</style>
