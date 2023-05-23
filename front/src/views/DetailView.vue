<template>
  <div>
    <img v-if="movie && movie.poster_path" :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" alt="image">
    <h2>{{ movie?.title }}</h2>
    <p>{{ movie?.overview }}</p>
    <!-- 리뷰 표시 -->
    
    <div v-for="review in reviews" :key="review.id">
      <p>{{ review.user }}</p> 
      <p>{{ review.content }}</p>
      <!-- <div class="inline" v-if="review.user === this.userpk"> -->
        <button @click.prevent="updateReview(review)" class="btn btn-secondary" style="font-size: 0.5rem;">수정</button>
        <button @click.prevent="deleteReview(review), reviewExist=false" class="btn btn-danger"  style="font-size: 0.5rem;">삭제</button>
      <!-- </div> -->
    </div>

    <!-- 리뷰 작성 폼 -->
    <form>        
      <h3>
        <input type="text" v-model="review_content" placeholder="리뷰 작성">
        <button @click.prevent="reviewCreate" class="btn btn-primary">제출</button>
        </h3>
    </form>
    
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'DetailView',
  components:{

  },
  data() {
    return {
      movie: null,
      userName: '',
      userpk: null,
      reviews: [],
      movieId: null,
      token:null,
      review_content : '',
    };
  },
  created() {
    this.movieId = this.$route.params.id;
    this.fetchMovieData()
    this.currentUser()
    this.getReviews()
  },
  methods: {
    // 영화정보 가져오기
    fetchMovieData() {
      // URL에서 movieId를 가져옵니다.
      // 영화 데이터를 가져오는 API 요청을 보내고 데이터를 설정합니다.
      axios.get(`http://127.0.0.1:8000/api/v1/movies/${this.movieId}/`)
        .then(response => {
          this.movie = response.data;
          console.log(this.movie)
        })
        .catch(error => {
          console.error(error);
        });
    },
    // 현재 유저 정보 가져오기 (username)
    currentUser() {
      const token = this.$store.state.token
      axios.get('http://127.0.0.1:8000/accounts/user/', {
      headers: {
        Authorization: `Token ${token}`
      }
    })
      .then(response => {
        this.userpk = response.data.pk;
        this.userName = response.data.username   
        // 리뷰 작성, 수정, 삭제 요청에 사용자 정보를 전달합니다.
      })
      .catch(error => {
        console.error(error);
      });
    },
    getReviews() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/movies/reviews/${this.movieId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.reviews = res.data
        console.log(this.reviews)
        // console.log(this.userId, this.reviews, this.reviews.user)
        this.reviews.forEach(element=>{            
            if (this.userId == element.user) {
              this.reviewExist = true
            }
          })          
          
        })
        .catch((err) => {
          console.log(err)
        })
      },
    reviewCreate () {
      const reviewItem = {
        content: this.review_content,
      }
      if (reviewItem) {
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/api/v1/movies/${this.movieId}/reviews/`,
          data: reviewItem,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
          .then(() => {
            this.review_content = ''
            this.getReviews()
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
    updateReview (review) {
      const reviewItem = {
        content: this.review_content
      }
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/api/v1/reviews/${review.id}/`,
        data: reviewItem,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
        })
        .then((res) => {
          console.log(res)
          this.review_content = ''
          this.getReviews();
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteReview (review) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/api/v1/reviews/${review.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.getReviews();
      })
      .catch((err) => {
        console.log(err)
      })
    },
  
    
  }
  };
</script>

<style>
/* 스타일 지정 */
</style>