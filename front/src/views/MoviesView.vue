<template>
  <div>
    <div class="container d-flex">
        <div class="row justify-content-center">
          <MovieCard
            class="mb-5 col-xs-12 col-md-6 col-lg-4 col-xl-3"
            v-for="movie in movies"
            :key="movie.id" 
            :movie="movie"
            @click="openModal(movie)"
          />
        </div>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'

export default {
    name:'MoviesView',
    components:{
        MovieCard,
    },
    // created(){
    //   this.$store.dispatch('getCard')
    // },
    computed:{
      movies(){
        return this.$store.state.Movies
      },
      sortedMovies(){
        console.log(this.movies)
        return this.$store.getters.sortedMovies
      },

      //
      isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
      },
    },
    created() {
    this.getCard()
    },
    methods: {
      getCard() {
        if (this.isLogin) {
          this.$store.dispatch('getCard')
        } else {
          alert('로그인이 필요한 페이지입니다...')
          this.$router.push({ name: 'LogInView' })
        }
        // 로그인이 되어 있으면 getArticles action 실행
        // 로그인 X라면 login 페이지로 이동
      }
    }   
  }

</script>

<style>

</style>
