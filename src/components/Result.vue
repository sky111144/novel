<template>
  <div class="section result">
    <div class="result-item" v-for="(book, bId) in books" :key="bId">
      <div class="book-img" :style="`background-image:url(${book.img})`"></div>
      <div class="book-info">
        <div class="book-item">
          <router-link class="book-name" :to="{ name: 'Novel', params: { novelId: book.id } }">
            {{ book.name }}
          </router-link>
          <a class="book-author" href="#">
            {{ book.author }}
          </a>
        </div>
        <div class="book-item book-intro">
          {{ book.intro }}
        </div>
        <div class="book-item">
          <ul class="book-tags">
            <li class="book-tag">
              <a class="book-tag-content" href="#">
                {{ '暂未分类' }}
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Result',
  props: ['books']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.section.result{
  margin-bottom: 0.5rem;
}
.result-item{
  display: flex;
  flex-direction: row;
  padding: 0.25rem 0;
  border-bottom: 1px solid #ededed;
  background-color: #fff;
}
.book-img{
  height: 3rem;
  width: 2.3rem;
  margin-right: 0.35rem;
  background-size: cover;
}
.book-item{
  margin-bottom: 0.25rem;
}
.book-intro{
  height: 1.25rem;
  width: 3.5rem;
  white-space: wrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.book-name{
  color: #000;
  font-size: 14px;
}
.book-author{
  font-size: 12px;
}
.book-tags{
  margin: 0;
  padding-left: 0;
}
.book-tag{
  display: inline-block;
}
.book-tag-content{
  display: inline-block;
  line-height: 0.75rem;
  height: 0.75rem;
  padding: 0 0.25rem;
  border-radius: 4px;
  color: #fff;
  font-size: 12px;
  background-color: #49f;
}
</style>
