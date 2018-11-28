<template>
  <div class="section">
    <ul class="picwall-wrapper">
      <li v-for="(books, bsId) in pictextwall.picwall" :key="bsId">
        <ul class="picwall">
          <li class="picwall-item" v-for="(book, bId) in books" :key="bId">
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
      <p class="textList-item text-overflow" v-for="(item, pId) in pictextwall.list" :key="pId">
        <router-link :to="{ name: 'Novel', params: { novelId: item.id } }">
          <i class="rank-icon">
            {{ pId + 4 }}
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
  justify-content: space-between;
}
.picwall-item {
  padding: 0.25rem 0;
  width: 30%;
}
.book-img {
  height: 2.8rem;
  width: 100%;
  background-size: cover;
}
.book-name {
  line-height: 0.8rem;
  height: 0.8rem;
  width: 100%;
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
