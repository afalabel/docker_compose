##https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-centos-7

## CentOS 7: Docker, Nginx, and flask

This will build the necessary services (nginx and flask) to serve php files.

The project directory will mount to ```/opt/app```.

```docker-compose build```
```docker-compose up -d```

#N.B.
#nginx e flask sono su due container diversi.
