const express = require('express')

const app = express()
app.use(express.json())

app.post('/', (req, res) => {
  let data = req.body
  console.log(data)
  res.send('Hello World!')
})
const PORT = process.env.PORT || 3000
app.listen(PORT, () => console.log('Example app listening on port 3000!'))
