<template>
  <div id="app">
    <nav class="navbar navbar-expand-md navbar-dark bg-dark sticky-top">
      <div class="container-fluid">
        <router-link :to="{name: 'home'}" class="navbar-brand"><img src="@/assets/byeongjin.jpg" alt="병진이" class="rounded" ></router-link>
        <router-link :to="{name: 'home'}" class="navbar-brand">오태식의 해바라기 무비</router-link>
  
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'SignUpView' }"  >SignUpPage</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'LogInView' }" >LogInPage</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'MoviesView' }"  >Movies</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'RandomView' }"  >Random</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    
    <router-view class="p-0"/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: black;
  ;
}

nav {
  padding: 30px;
  background-color: #2c3e50;
}

nav a {
  font-weight: bold;
  color: whitesmoke;
}

nav a.active {
  color: #42b983;
}

nav img {
  width: 40px;
  height: 40px;
  border-radius: 70%;
  margin-right: 10px;
}

</style>
