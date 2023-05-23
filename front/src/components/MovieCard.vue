<template>
  <div>
    <div class="card" style="width: 8rem;" @click="ToDetail(movie.id)">
        <img v-bind:src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" class="card-img-top" alt="image">
        <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'MovieCard',
    props: {
      movie: Object,
    },
    methods: {
      ToDetail(movieId) {
        this.$router.push({
          name: 'DetailView',
          params: {
            id:movieId,
          },
        });
      },
    },
}
</script>

<style>
.overview p{
    width: 500px;
    -webkit-line-clamp: 3;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    overflow: hidden;
}
</style>