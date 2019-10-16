const express = require('express')
const router = express.Router()
const { pool } = require('../../db')

/* POST scores of a client (demo game) */
router.post('/demo-game', async (req, res) => {
  try {
      const poolRes = await pool.query('select tappedkey, timestamp from demo where clientname = $1', [req.name])
      res.send(poolRes.rows)
  } catch (error) {
      console.log(error.stack)
      res.status(500).send({
          error: error.stack
      })
  }
})

/* POST add scores in demo game for a given client */
router.post('/add-demo-scores', async (req, res) => {
  try {
    let qString = 'insert into demo (clientname, tappedkey, timestamp) values '
    const qParams = []
    req.scores.forEach(score => {
      qParams.push(score.clientname)
      qString += '($' + qParams.length
      qParams.push(score.tappedkey)
      qString += ',$' + qParams.length
      qParams.push(score.timestamp)
      qString += ',$' + qParams.length + '), '
    })
    await pool.query(qString.substring(0, qString.length-2))
    res.send('success')
} catch (error) {
    console.log(error.stack)
    res.status(500).send({
        error: error.stack
    })
}
})

module.exports = router
