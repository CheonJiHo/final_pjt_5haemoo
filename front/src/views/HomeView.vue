<template>
  <div class="home">
  <section class="d-flex justify-content-center">
    <h1 class="text-start"> 나를 웃게 하는건 <br> "영화" 입니다</h1>
    
    <div class="container card1 ">
      <div class="row height:300px">
        <div class="col-lg-3">

        </div>
      </div>
    </div>
  </section>
  </div>

</template>

<script>
export default {

}
</script>

<style>
body{
  
  background-color: black;
}

section{
  height: 100vh;
  background: url(@/assets/sunflower.png);
}
section:before{
  content: '';
  background: linear-gradient(to top, black, transparent);
  position: absolute;
  left:0;
  height: 100%;
  width: 100%;
}
h1{
  width: 70%;
  color: whitesmoke;
  font-size: 5em;
  position: absolute;
  top:700px;
  left:50px;
  font-family: sans-serif;
}
.card1{
  width: 70%;
  color: whitesmoke;
  font-size: 5em;
  position: absolute;
  top:1000px;
  
  font-family: sans-serif;
}
.home{
  height:2000px;
}

</style>