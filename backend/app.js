const express = require('express')
require('dotenv').config();
const http = require('http');
const cors = require('cors');
const db = require('./database/db')
const authRoutes = require('./routes/auth-routes');
const fileRoutes = require('./routes/file-routes');
const extractRoutes = require('./routes/extract-route');
const skillRoutes = require('./routes/skill-routes');
const app = express()

db();



app.use(cors());
app.use(express.json());
app.use('/api/auth' ,  authRoutes);
app.use('/api/files' ,  fileRoutes);
app.use('/api/extract' ,  extractRoutes);
app.use('/api/skills' ,  skillRoutes);


app.listen(process.env.PORT, () => console.log("Server running on port 5000"));