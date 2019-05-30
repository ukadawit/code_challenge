import axios from 'axios';

var http = axios.create({
  baseURL: 'http://localhost:12000',
  timeout: 5000,
  headers: {
    'X-Auth-Token': 'f2b6637ddf355a476918940289c0be016a4fe99e3b69c83d',
    'Content-Type': 'application/json'
  }
});


var coinHttp = axios.create({
    baseURL: 'https://rest.coinapi.io',
    timeout: 5000,
    headers: {
      'X-CoinAPI-Key': 'DEEEDF74-4B93-41B4-87E2-7E103C08FFEB',
      'Content-Type': 'application/json'
    }
  });

export default {
    getCubeLocation(){
        console.log('test');
        return http.get('');
    },
    
    getExchanges(){
      return coinHttp.get('/v1/exchanges');
    }
}