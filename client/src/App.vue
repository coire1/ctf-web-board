<template>
  <div id="app">
    <header class="header">
      <div class="logo-wrapper">
        <img src="./assets/logo.jpg" class="logo" />
        <h1>MiniCTF<br />Haqlab</h1>
      </div>
      <div id="nav">
        <router-link to="/">Rank</router-link>
        <router-link to="/challenges">Challenges</router-link>
      </div>
    </header>
    <div class="view-wrapper">
      <router-view/>
    </div>
  </div>
</template>


<style lang="scss">
@import "./assets/fonts/font.css";

* {
  box-sizing: border-box;
}
html,
body {
  background: #000;
  margin: 0;
  color: white;
}
header {
  width: 100%;
  float: left;
  height: 100px;
  display: flex;
  justify-content: space-around;
  .logo-wrapper {
    width: 50%;
    .logo {
      float: left;
      height: 100px;
      margin-right: 40px;
    }
    h1 {
      float: left;
      width: calc(100% - 140px);
    }
  }
  #nav {
    width: 50%;
    display: flex;
    justify-content: flex-end;
    a,
    a:visited {
      padding: 20px;
      color: #fff;
      &:hover {
        color: #424040;
      }
    }
  }
}
.view-wrapper {
  width: 100%;
  float: left;
}
#app {
  max-width: 1440px;
  width: 100%;
  margin: 0px auto;
  padding: 0 30px;
  font-family: "Press Start 2P", cursive;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
