// Custom imports
const { pool } = require('../db')

const getAllClients = async () => {
    const res = await pool.query()
}

module.exports = {
    getAllClients
}