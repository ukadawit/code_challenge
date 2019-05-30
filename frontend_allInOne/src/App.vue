<template>
  <div id="app" class="container">
   <h4>My code challange test</h4>
    <hr>
    <app-header></app-header>
    <hr>
    <router-view/>
  </div>
</template>

<script>
import Header from './components/shared/Header';
export default {
  name: 'App',
  components: {
    'app-header': Header
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
