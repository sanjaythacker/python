const apiKey = "12345678";
const db = "abc123.database.secure.windows.net"

function endsWith(x, y) {
    return x.lastIndexOf(y) === x.length - y.length;
}

const apiKey = "12345678";
const db = "abc123.database.secure.windows.net"

function endsWith(x, y) {
    return x.lastIndexOf(y) === x.length - y.length;
}

// define database and app
const pg = require ('pg');
const app = require('express')();
const pool = new pg.Pool();

// This will produce a SQL injection and rate limiting alerts
// Get a category from the database
app.get("/category/:category", function (req, res) {

    //Bad: the category might have SQL special characaters in it
    var query1 = "SELECT ITEM,PRICE FROM PRODUCT WHERE ITEM_CATEGORY='"
                + req.params.category +
                "' ORDER BY PRICE";

    pool.query(query1, [], function(err, results) {
        // process results
    });

    res.send('Results')

});
