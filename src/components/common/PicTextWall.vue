<template>
  <div class="section">
    <ul class="picwall-wrapper">
      <li v-for="books in pictextwall.picwall">
        <ul class="picwall">
          <li class="picwall-item" v-for="book in books">
            <router-link :to="{ name: 'Novel', params: { novelId: book.id } }">
              <div class="book-img" :style="'background-image: url(' + book.img + ')'"></div>
              <div class="book-name">
                {{ book.name }}
              </div>
            </router-link>
          </li>
        </ul>
      </li>
    </ul>
    <div class="textList-wrapper">
      <p class="textList-item text-overflow" v-for="(item, index) in pictextwall.list">
        <router-link :to="{ name: 'Novel', params: { novelId: item.id } }">
          <i class="rank-icon">
            {{ index + 3 }}
          </i>
          <span>
            {{ item.intro }}
          </span>
        </router-link>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Picwall',
  props: ['pictextwall']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.picwall {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}
.picwall-item {
  padding: 0.25rem 0;
}
.book-img {
  height: 3rem;
  width: 2.3rem;
  background-size: cover;
}
.book-name {
  line-height: 1rem;
  height: 1rem;
  width: 2.3rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  text-align: center;
}
.textList-wrapper{
  padding-bottom: 0.5rem;
}
.rank-icon{
  display: inline-block;
  line-height: 0.65rem;
  height: 0.65rem;
  width: 0.65rem;
  margin-right: 0.15rem;
  text-align: center;
  color: #fff;
  border-radius: 4px;
  background: #d2d2d2;
}
.textList-item:first-child{
  border-top: 1px solid #ededed;
}
.textList-item{
  color: #929292;
  padding: 0.15rem 0;
  font-size: 14px;
  border-bottom: 1px solid #ededed;
}
</style>
