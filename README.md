# api_final
### Описание проекта:

API проекта Yatube(v1) предназначено для создания постов и написания комментариев к ним.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры:

Получаем список всех постов или создаём новый пост:

```
api/v1/posts/ (GET, POST)
```
Пример запроса:
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Пример ответа API:

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

Получаем, редактируем или удаляем пост по id:

```
api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE)
```

Получаем список всех групп:

```
api/v1/groups/ (GET)
```

Получаем информацию о группе по id:

```
api/v1/groups/{group_id}/ (GET)
```

Получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать:

```
api/v1/posts/{post_id}/comments/ (GET, POST)
```

Получаем, редактируем или удаляем комментарий по id у поста с id=post_id:

```
api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE)
```

Получаем все подписки пользователя, сделавшего запрос или создаем новую:

```
api/v1/groups/ (GET)
```

### Использованные технологии:

Django REST framework:

```
https://www.django-rest-framework.org/
```

Pillow:

```
https://pillow.readthedocs.io/en/stable/
```

PyJWT:

```
https://pyjwt.readthedocs.io/en/stable/
```

Requests:

```
https://requests.readthedocs.io/en/latest/
```
