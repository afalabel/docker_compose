docker pull nginx
docker run --name nginx-template-base -p 8080:80 -e TERM=xterm -d nginx
docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
05ac592e7dea        nginx               "nginx -g 'daemon of…"   19 seconds ago      Up 17 seconds       0.0.0.0:8080->80/tcp     nginx-template-base

docker exec -it 05ac592e7dea bash

#Da dentro in CONTAINER
apt-get update
apt-get install vim

#Create the storage folder with some subfolders and file

#Edit /etc/nginx/conf.d/default.conf
#Add to the configuration file
location /storage {
    autoindex on;
}


#Exit the CONTAINER
docker commit  05ac592e7dea  nginx-template

docker container stop 05ac592e7dea

docker run --name nginx-dev -p 8080:80 -e TERM=xterm -d nginx-template
