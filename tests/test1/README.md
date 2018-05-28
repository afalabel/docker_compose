docker build -t pythonflask .

docker image ls

#Map port 80 on the container to port 4000 on the host machine
docker run -p 4000:80 pythonflask

CTRL+C to stop

#Run  in detached mode
docker run -d -p 4000:80 pythonflask
docker container ls
docker container stop <container id>


docker tag pythonflask/custom afalabel/first

docker login

docker push afalabel/first
