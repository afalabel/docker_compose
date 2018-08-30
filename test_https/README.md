# Example take from :
https://github.com/Integralist/Docker-Examples/tree/master/Nginx-ClientCertAccess/docker-nginxand

docker build -t my-nginx .

docker run --name nginx-container \
  -v $(pwd)/html:/usr/share/nginx/html:ro \
  -v $(pwd)/certs:/etc/nginx/certs/ \
  -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro \
  -P -d my-nginx
