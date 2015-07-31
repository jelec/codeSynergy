// Use express block
var express = require('express');
var app = express();

// File structure
require('./config')(app);
require('./models')(app);

// Allow them to activate
var config = app.get('config');

// Block : Include important headers headers
app.use(function (req, res, next) {
	res.header('Access-Control-Allow-Credentials', true);
	res.header('Access-Control-Allow-Origin', req.headers.origin);
	res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
	res.header('Access-Control-Allow-Headers', 'X-Requested-With, X-HTTP-Method-Override, Content-Type, Accept');

	if ('OPTIONS' === req.method) {
		res.status(200).end();
	} else {
		next();
	}
});

// Use Body parser 
var bodyParser = require('body-parser');

// Block : Allow express to use bodyParser
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
	extended: true
}));

// Block : Allow for hosting of static files
app.use(express.static(__dirname + '/@path')); // Included path
app.get('/@command', function (req, res) { //
	res.sendFile(__dirname + '/@path/@dir.html');
});

// Block : Global Set of routing
var router = express.Router();
app.set('router', router);
app.use(router);

// Block : Server Start 
// Imports ports and etc
var http = require('http');

http.createServer(app)
	.listen(config.PORT, function () {
		console.log('app start on port ' + config.PORT);
	});