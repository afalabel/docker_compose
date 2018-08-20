# Example take from :
https://www.howtoforge.com/tutorial/docker-guide-dockerizing-python-django-application/
and
https://tutorial.djangogirls.org/it/django_start_project/

With some minor modifications
mkdir test_web
cd test_web
mkdir project/ config/

# Django Example
mkdir django_test/
cd  django_test/
django-admin startproject mysite

mysite
    ├── mysite
    │  
    └── manage.py

# Copy all the directory structure to the docker compose project folder
cp -r * ~/docker_cache_studies/test_web/project/.
