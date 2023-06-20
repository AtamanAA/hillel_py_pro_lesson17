# University

## Web applications with CRUD operation.
### Use Django, PostgreSQL, Herroku Pipiline, AWS S3

https://ataman-university-app.herokuapp.com

## Розгортаня проекту локально (команди для Windows)

1. Склонувати репозиторій
    ```bash    
    git clone https://github.com/AtamanAA/hillel_py_pro_lesson17.git
    ```
2. Запустити [PostgreSQL](https://www.postgresql.org) (переконатися що [Docker Desktop](https://www.docker.com/products/docker-desktop/) запущений )
    ```bash
    docker run --rm --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5400:5432 -v vol_1:/var/lib/postgresql/data postgres
    ```
3. Встановити venv та активувати його
    ```bash
    python -m venv venv
   .\venv\Scripts\activate    
    ```
4. Інсталювати сторонні пакети у venv
    ```bash
    python -m pip install -r requirements.txt    
    ```
5. Перейти до осноної дерикторії проекту
    ```bash
    cd hillel_py_pro_lesson17    
    ```
6. Виконати запуск основного web-серверу
    ```bash
    python manage.py runserver   
    ```
7. В браузері перейти на домашню сторінку
    http://127.0.0.1:8000/blog/<publication_id>


