const express = require('express')
const router = express.Router()
const { pool } = require('../../db')

/* GET all clients */
router.get('/all', async (req, res) => {
  try {
      const poolRes = await pool.query('select distinct clientname from demo')
      res.send(poolRes.rows)
  } catch (error) {
      console.log(error.stack)
      res.status(500).send({
          error: error.stack
      })
  }
})

module.exports = router
