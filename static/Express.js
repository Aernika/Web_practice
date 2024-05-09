const express = require('express');
const csrf = require('csurf');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

const csrfProtection = csrf({ cookie: true });

app.use(bodyParser.urlencoded({ extended: true }));
app.use(csrfProtection);

app.use((req, res, next) => {
    res.locals.csrfToken = req.csrfToken();
    next();
});

app.post('/4/result/', (req, res) => {
    // Получаем данные из формы
    const formData = req.body;

    // Отправляем ответ с данными
    res.send(`<h1>Результат</h1>
              <p>Ваше имя: ${formData.name}</p>
              <p>Ваш email: ${formData.email}</p>
              <!-- Другие данные формы -->
              `);
});

app.listen(port, () => {
    console.log(`Сервер запущен на http://localhost:${port}`);
});