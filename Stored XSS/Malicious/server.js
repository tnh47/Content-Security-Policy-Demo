const express = require('express');
const app = express();
const port = 3000;

// Cung cấp các tệp tĩnh (chẳng hạn như script.js)
app.use(express.static('public'));

// Endpoint để gửi một trang HTML với mã JavaScript
app.get('/', (req, res) => {
    res.send(`
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Inject Script Demo</title>
        </head>
        <body>
            <h1>Welcome to localhost:3000</h1>
            <script src="/inject.js"></script> <!-- Nhúng script từ localhost -->
        </body>
        </html>
    `);
});

// Chạy máy chủ trên cổng 3000
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
