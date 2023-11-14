const express = require('express')
const cors = require('cors')
const app = express()
app.use(cors())
app.use(express.json())
app.post('/', (req, res) => {
  let data = req.body
  console.log(data)
  res.send('Hello World!')
})
const PORT = process.env.PORT || 3000
app.listen(PORT, () => console.log('Example app listening on port 3000!'))
