import Vue from 'vue';
import Router from 'vue-router';
import Home from '../components/Home';
import CubeLocation from '../components/CubeLocation';
import ConsumeApi from '../components/ConsumeApi';
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '', 
      component: Home
    },
    {
      path: '/', 
      component: Home,
      name: 'home'
    },
    {
      path: '/cubeLocation', 
      component: CubeLocation,
      name: 'cubeLocation'
    },
    {
      path: '/consumeApi', 
      component: ConsumeApi,
      name: 'consumeApi'
    },
    {
      path: '*',
      redirect: '/'
    }
    
  ],
  mode: 'history'
})
