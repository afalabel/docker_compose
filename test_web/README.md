# Example take from :
https://www.howtoforge.com/tutorial/docker-guide-dockerizing-python-django-application/
and
https://tutorial.djangogirls.org/it/django_start_project/

With some minor modifications

## Create directory structure

```
mkdir test_web
cd test_web
mkdir project/ config/
```
## Django Example
```
mkdir django_test/
cd  django_test/
django-admin startproject mysite
```
```
mysite
    ├── mysite
    │  
    └── manage.py
```
### Copy all the directory structure to the docker compose project folder
```
cp -r * ~/docker_cache_studies/test_web/project/.
```

## List of the files to edit
```
vim config/requirements.txt
mkdir -p config/nginx/
vim config/nginx/django.conf
vim Dockerfile
vim docker-compose.yml
```

## Modification to django config
In settings.py
```
ALLOW_HOSTS = ['web']
```
and
```
DATABASES = {  
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'postgres',
         'USER': 'postgres',
         'HOST': 'db',
         'PORT': 5432,
     }
 }
```
and
```
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
```
## Build and run
```
docker-compose build
docker-compose up -d
```
check the running containers
```
docker-compose ps
docker-compose images
```
