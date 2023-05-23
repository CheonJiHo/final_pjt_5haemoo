<template>
  <div>
    <h2>Random View</h2>

    <!-- 장르 선택 -->
    <select v-model="selectedGenre">
      <option option value="">전체</option>
      <option v-for="genre in genres" :key="genre.id" :value="genre.id">{{ genre.name }}</option>
    </select>


    <!-- 랜덤 영화 출력 -->
    <div v-if="randomMovie" class="movie-card">
      <img v-bind:src="`https://image.tmdb.org/t/p/original${randomMovie.poster_path}`" alt="movie poster" />
      <h3>{{ randomMovie.title }}</h3>
    </div>
    <div v-else>No movie available</div>

    <!-- 랜덤 영화 가져오기 버튼 -->
    <button @click="fetchRandomMovie">랜덤 영화 추출</button>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  
  data() {
    return {
      selectedGenre: null,
    };
  },
  computed: {
    ...mapGetters(['getRandomMovie']),
    genres() {
      return this.$store.state.genres;
    },
    randomMovie() {
      return this.$store.state.randomMovie;
    },
  },
  methods: {
    fetchRandomMovie() {
      this.$store.dispatch('getRandomMovie', this.selectedGenre);
    }
  },
  created() {
    this.$store.dispatch('fetchGenres');
  },
};
</script>

<style>
.movie-card {
  width: 200px;
  margin: 10px;
}
</style>
