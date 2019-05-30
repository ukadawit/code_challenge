<template>
  <div class="container">
    <table>
    
      <tr>
        <th>Cube location</th>
        <th><button @click="refreshLocation" class="btn">Refresh location</button></th>
      </tr>
      <tr>
        <td>X cordinate</td>
        <td>{{didReturn ? cubeLocation.x: 'Loading...'}}</td>
      </tr>
      <tr>
        <td>Y cordinate</td>
        <td>{{didReturn ? cubeLocation.y: 'Loading...'}}</td>
      </tr>
      <tr>
        <td>Z cordinate</td>
        <td>{{didReturn ? cubeLocation.z: 'Loading...'}}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import apiService from "../services/apiService";
export default {
  data: function() {
    return {
      cubeLocation: [],
      errorMessage: '',
      didReturn: false
    };
  },
  beforeCreate: function() {
    apiService
      .getCubeLocation()
      .then(resp => {
          console.log(resp.data),
          this.errorMessage = '';
        this.cubeLocation = resp.data;
      })
      .catch(err => {});
  },
  methods: {
      refreshLocation: function(){
           apiService
      .getCubeLocation()
      .then(resp => {
          console.log(resp.data)
          this.errorMessage = ''
          this.didReturn = true
        this.cubeLocation = resp.data;
      })
      .catch(err => {
          this.errorMessage = "Error while getting data"
          console.log(err)
      });
      }
  }
};
</script>

<style>
</style>
