FROM nginx_voms

USER root

RUN mkdir -p /etc/nginx/conf
RUN mkdir -p /etc/nginx/conf.d
RUN mkdir -p /etc/nginx/logs

COPY ./.docker/nginx/nginx.conf /etc/nginx/conf/nginx.conf
COPY ./.docker/nginx/app.conf /etc/nginx/conf.d/app.conf


CMD /home/build/local/openresty/nginx/sbin/nginx -p /etc/nginx
