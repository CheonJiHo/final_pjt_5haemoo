<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username"> username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      <br>
      <label>선호하는 장르 | {{ selectedGenres.length }}/3</label>
      <div class="row">
        <div v-for="genre in genres" :key="genre.id" class="col-md-3">
          <label class="checkbox-label">
            <input type="radio" :value="genre.id" v-model="selectedGenres" @change="checkGenreLimit(genre.id)">
            {{ genre.name }}
          </label>
        </div>
      </div>

      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      genres: [],              // 장르 목록
      selectedGenres: [],      // 선택한 장르 ID 배열
    }
  },
  methods: {
    signUp() {
      // console.log('signup')
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const selectedGenres = this.selectedGenres

      const payload = {
        username, password1, password2, selectedGenres
      }
      // if (this.selectedGenres.length != 3) {
      //   alert('3개의 장르를 선택해야 합니다.')
      //   return;
      // }
      
      this.$store.dispatch('signUp', payload)
    },
    fetchGenres() {
      // 장르 목록을 받아오는 API를 호출하여 genres 데이터를 설정하는 메서드
      axios.get('http://127.0.0.1:8000/api/v1/movies/genres/')
        .then(response => {
          console.log(response.data)
          this.genres = response.data;
        })
        .catch(err => {
          console.log(err)
          // 에러 처리
        }); 
    },
    // checkGenreLimit(genreId) {
    //   if (this.selectedGenres.length > 3) {
    //     const index = this.selectedGenres.indexOf(genreId);
    //     this.selectedGenres.splice(index, 1); // 이전 상태로 되돌립니다.
    //     const checkbox = event.target;

    //     checkbox.checked = false; // 체크박스의 checked 속성을 조작하여 해제합니다.
    //     alert('3개 이상의 장르를 선택할 수 없습니다.');
    //   }
    // },
  },
  mounted() {
    this.fetchGenres(); // 컴포넌트가 마운트되면 장르 목록을 가져옴
  }
  }

</script>

<style>
.checkbox-label {
  display: inline-block;
  margin-right: 10px;
}


</style>