<template>
  <div id="app">
    <nav>
      <div class="nav-links">
      <router-link v-if="!isLogin" :to="{ name: 'SignUpView' }">SignUpPage | </router-link> 
      <router-link v-if="!isLogin" :to="{ name: 'LogInView' }">LogInPage | </router-link> 
      <router-link :to="{ name: 'MoviesView' }">Movies</router-link> |
      <router-link :to="{ name: 'RandomView' }">Random</router-link>
      </div>
      <div class="logout-btn">
        <button v-if="isLogin" @click="logout">Logout</button>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
 
  computed: {
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }, 
  },
  created() {

  },
  methods: {
    logout() {
      this.$store.dispatch('logout');
    }
  },
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
nav img {
  width: 30px;
  height: 50px;

}
.logout-btn button:hover {
  text-decoration: underline;
}
</style>
