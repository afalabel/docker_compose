##https://github.com/iamawwsome/docker-nginx-php-fpm-7
## CentOS 7: Docker, Nginx, and php-fpm

This will build the necessary services (nginx and php-fpm) to serve php files.

The project directory will mount to ```/opt/app```.

```docker-compose build```
```docker-compose up -d```

#N.B.
#nginx e php sono su due contained diversi. Questo funziona grazie a questa riga di configurazione
#in app.conf
#    fastcgi_pass php-fpm:9000;
# notare che php-fpm è l'hostname del container come è stato definito nel docker-compose.yml
<!-- php-fpm: <------- Questo è l'hostname
  build:
    context: .
    dockerfile: .docker/php-fpm/Dockerfile
  expose:
    - "9000"
  volumes:
    - ${PWD}/html:/usr/share/nginx/html
  stdin_open: true
  tty: true -->
