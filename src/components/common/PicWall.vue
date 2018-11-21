<template>
  <div class="section">
    <ul class="picwall-wrapper">
      <li v-for="books in picwall">
        <ul class="picwall">
          <li class="picwall-item" v-for="book in books">
            <router-link :to="{ name: 'Novel', params: { novelId: book.id} }">
              <div class="book-img" :style="'background-image: url(' + book.img + ')'"></div>
              <div class="book-name">
                {{ book.name }}
              </div>
            </router-link>
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Picwall',
  props: ['picwall']
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
    justify-content: space-around;
  }
  .picwall-item {
    padding: 0.15rem 0;
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
    font-size: 14px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    text-align: center;
  }
</style>
