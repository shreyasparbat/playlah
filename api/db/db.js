// Imports
const pg = require('pg')
const moment = require('moment')

// Parse dates as moment objects
pg.types.setTypeParser(1082, val => moment.utc(val))

// Connect to postgres
const Pool = pg.Pool
const pool = new Pool({
    user: process.env.DB_USER,
    host: process.env.DB_HOST,
    database: process.env.DB_NAME,
    password: process.env.DB_PASSWORD,
    port: process.env.DB_PORT,
})

// Export connection pool
module.exports = {
    pool
}