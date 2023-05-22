<template>
  <div class="home">
  <section class="d-flex justify-content-center">
    <h1 class="text-start main"> 나를 웃게 하는건 <br> "영화" 입니다</h1>
    
     <header class="masthead">
            <div class="container px-4 px-lg-5 h-100">
                <div class="row gx-4 gx-lg-5 h-100 align-items-center justify-content-center text-center">
                    <div class="col-lg-8 align-self-end">
                        <h1 class="text-white font-weight-bold">오태식의 해바라기 영화에 오신걸 환영합니다</h1>
                        <hr class="divider" />
                    </div>
                
                <div class="container">
            <div class="row gx-4 gx-lg-5 h-100 align-items-center justify-content-center text-center">
              <div class="col-md-6 cardImg">
                <img src="@/assets/comeback.png" alt="오태식이 돌아왔구나" class="img-fluid">
            </div>
            <div class="col-md-6">
              <h2>오태식이 돌아왔구나...</h2>
              <br>
              <h4>오태식의 해바라기 영화는 언제나 봐도 즐겁습니다</h4>
            </div>
          </div>
        </div>
                </div>
            </div>
        </header>
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
.main{
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
header{
  width: 70%;
  color: whitesmoke;
  font-size: 5em;
  position: absolute;
  top:1100px;
  
  font-family: sans-serif;
}
.cardImg{
  margin-bottom: 20px;
}
</style>