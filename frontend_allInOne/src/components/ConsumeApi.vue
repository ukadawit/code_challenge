<template>
    <div>
        <div class="row">
            <h4>List of exchanges from coin api</h4>
        </div>
        <div class="row">
            <table>
                <tr>
                    <th>Exchange Id</th>
                    <th>Web site</th>
                    <th>Name</th>
                </tr>

                <tr v-for="(exchange, i) in listOfExchanges" :key="i">
                    <td>
                        {{exchange.exchange_id}}
                    </td>
                    <td>
                        {{exchange.website}}
                    </td>
                    <td>
                        {{exchange.name}}
                    </td>
                </tr>
            </table>
        </div>

        <div class="row" v-if="!didReturn">
            Loading...
        </div>

    </div>
</template>

<script>

import apiService from '../services/apiService';

export default {

    data: function(){
        return {
            listOfExchanges: [],
            didReturn: false
        }
    },
    beforeCreate: function(){
        apiService.getExchanges()
            .then(
                resp => {
                    // console.log(resp.data)
                    this.didReturn = true;
                    this.listOfExchanges = resp.data;
                }
            )
            .catch(
                err => {
                    this.didReturn = false;
                }
            )
    }

}
</script>

<style>

</style>
