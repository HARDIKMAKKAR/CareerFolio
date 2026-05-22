const express = require('express');
require('dotenv').config();

const cors = require('cors');

const db = require('./database/db');

const authRoutes = require('./routes/auth-routes');
const fileRoutes = require('./routes/file-routes');
const extractRoutes = require('./routes/extract-route');
const skillRoutes = require('./routes/skill-routes');

const app = express();

db();

app.use(cors({
    origin: '*',
    methods: ['GET', 'POST', 'PUT', 'DELETE'],
    credentials: true
}));

app.use(express.json());

app.get('/', (req, res) => {
    res.send('CareerFolio Backend Running');
});

app.use('/api/auth', authRoutes);
app.use('/api/files', fileRoutes);
app.use('/api/extract', extractRoutes);
app.use('/api/skills', skillRoutes);

const PORT = process.env.PORT || 5000;

app.listen(PORT, '0.0.0.0', () => {
    console.log(`Server running on port ${PORT}`);
});