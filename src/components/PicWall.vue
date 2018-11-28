<template>
  <div class="section">
    <ul class="picwall-wrapper">
      <li v-for="(books, bsId) in picwall" :key="bsId">
        <ul class="picwall">
          <li class="picwall-item" v-for="(book, bId) in books" :key="bId" @click="gotoBook(book)">
              <div class="book-img" :style="'background-image: url(' + book.img + ')'"></div>
              <div class="book-name">
                {{ book.name }}
              </div>
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Picwall',
  props: ['picwall'],
  methods: {
    gotoBook (book) {
      this.$router.push({ name: 'Novel', params: { novelId: book.id } })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .picwall-wrapper {
    padding: 0.25rem 0;
    margin-bottom: 0.5rem;
  }
  .picwall {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }
  .picwall-item {
    padding: 0.15rem 0;
    width: 30%;
  }
  .book-img {
    height: 2.8rem;
    width: 100%;
    background-size: cover;
  }
  .book-name {
    line-height: 1rem;
    height: 1rem;
    width: 100%;
    font-size: 14px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    text-align: center;
  }
</style>
