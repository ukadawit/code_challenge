// Nodejs script that fetches list of assets from coin api and responds the list 

// https module for requiring from coin api
var https = require('https');

// http module to listen for client request
var http = require('http');

// server that will listen for client request
// it first waits for client to request and queries coin api
// once it gets the response from coin api, it returns to client

var server = http.createServer((function (req, resp) {

    // request to coin api
    var request = https.request({
        "method": "GET",
        "hostname": "rest.coinapi.io",
        "path": "/v1/assets",
        "headers": { 'X-CoinAPI-Key': '73034021-0EBC-493D-8A00-E0F138111F41' }
    },

        function (listOfAssets) {
            // send the result to client once it has got
            listOfAssets.on('data', function (result) {
                resp.writeHead(200, { 'Content-Type': 'application/json' })
                resp.end(result);
            });
        }
    );

    request.end();

   

}));

server.listen(4000, function () {
    console.log('Server started listening on port 4000...')
});
