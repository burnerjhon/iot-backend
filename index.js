const express = require('express')
var bodyParser = require('body-parser')
const cors = require('cors')
const app = express()
app.use(cors())
app.use(express.bodyParser());
app.use(bodyParser.urlencoded({ extended: true }))
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Authorization, X-API-KEY, Origin, X-Requested-With, Content-Type, Accept, Access-Control-Allow-Request-Method');
    res.header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE');
    res.header('Allow', 'GET, POST, OPTIONS, PUT, DELETE');
    next();
});
app.use(express.json())
app.post('/', (req, res) => {
  let data = req.body
  console.log(data)
  console.log("hola")
  res.send('Hello World!')
})
const PORT = process.env.PORT || 3000
app.listen(PORT, () => console.log('Example app listening on port 3000!'))
