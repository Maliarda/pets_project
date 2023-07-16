# pets_project
Тестовое задание для Python (Django) разработчика от компании Anyera Digital &amp; Design

## Как запустить проект:

 _Если у вас не установлены Docker и Docker-compose необходимо воспользоваться официальной [инструкцией](https://docs.docker.com/engine/install/)._

### Клонировать репозиторий и перейти в нем в папку infra в командной строке:

```
git clone https://github.com/Maliarda/pets_project.git
```
```
cd pets_project/infra
```
### Создать .env файл в директории infra, в котором должны содержаться следующие переменные:
> DB_ENGINE=django.db.backends.postgresql - указываем, что работаем с postgresql

> DB_NAME=postgres - имя базы данных

> POSTGRES_USER=postgres - логин для подключения к базе данных

>POSTGRES_PASSWORD=postgres - пароль для подключения к БД (установите свой)

>DB_HOST=db - название сервиса (контейнера)

> DB_PORT=5432 - порт для подключения к БД

### Создать .env файл в директории pets_project для SECRET_KEY
Для генерации нового значения можно использовать команду (из контейнера web, 
либо иного окружения с установленным python и Django)

```
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### Собрать образ при помощи docker-compose

```
docker-compose up -d --build
```

### Применить миграции:
```
docker-compose exec web python manage.py migrate
```
### Собрать статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```

### Создать суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```