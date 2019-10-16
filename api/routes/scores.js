const express = require('express')
const router = express.Router()
const { pool } = require('../db')

/* POST add scores in demo game for a given client */
router.post('/add-demo-scores', async (req, res) => {
  try {
    let qString = 'insert into demo (clientname, tappedkey, timestamp) values '
    const qParams = []
    req.body.scores.forEach(score => {
      qParams.push(score.clientname)
      qString += '($' + qParams.length
      qParams.push(score.tappedkey)
      qString += ',$' + qParams.length
      qParams.push(score.timestamp)
      qString += ',$' + qParams.length + '), '
    })
    await pool.query(qString.substring(0, qString.length-2), qParams)
    res.send('success')
} catch (error) {
    console.log(error.stack)
    res.status(500).send({
        error: error.stack
    })
}
})

module.exports = router
