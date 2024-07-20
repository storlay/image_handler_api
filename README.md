<h1 align="center">API:Сервис обработки изображений 🎇</h1>

<div align="center">

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Pillow](https://img.shields.io/badge/pillow-11557C?style=for-the-badge&logo=python&logoColor=white)](https://python-pillow.org/)
[![Docker](https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Gunicorn](https://img.shields.io/badge/gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)](https://gunicorn.org/)
[![Poetry](https://img.shields.io/badge/poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)](https://python-poetry.org/)


</div>
<br>

## Основные возможности:
1. **Изменение качества**
2. **Настройка ширины/высоты**
3. **Добавление собственного водяного знака**
4. **Настройка прозрачности/расположения водяного знака**
5. **Аутентификация по API ключу**

<br>

## Установка и запуск

1. Склонируйте репозиторий:

```
git clone https://github.com/storlay/image_handler_api.git
```

2. Создайте и заполните файл `.env`

```
API_KEY=
```

3. Запустите проект с помощью Docker Compose:

```
docker compose -f infra/docker-compose.yml up --build 
```

4. API будет доступно по адресу http://127.0.0.1:8000

<br>

## Использование

- **Документация API** доступна по адресам:
    - http://127.0.0.1:8000/docs (Swagger)
    - http://127.0.0.1:8000/redoc (Redoc)

- Для доступа к API нужно ввести `API_KEY` в разделе **Authorize** (Swagger) или передать его в **Headers** запроса по ключу **access_token**