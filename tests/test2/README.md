#--advertise-addr : use the ip of the host interface
docker swarm init --advertise-addr 131.154.5.31
docker stack deploy -c docker-compose.yml getstartedlab

docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE                       PORTS
n2v2nf01plr2        getstartedlab_web   replicated          5/5                 afalabel/first:latest   *:4000->80/tcp

curl -4 http://localhost:4000
<h3>Hello World!</h3><b>Hostname:</b> cffa2844dd94<br/><b>Visits:</b> <i>cannot connect to Redis, counter disabled</i>
curl -4 http://localhost:4000
<h3>Hello World!</h3><b>Hostname:</b> cc057bf90fdb<br/><b>Visits:</b> <i>cannot connect to Redis, counter disabled</i>
curl -4 http://localhost:4000
<h3>Hello World!</h3><b>Hostname:</b> a401f9363ac4<br/><b>Visits:</b> <i>cannot connect to Redis, counter disabled</i>
curl -4 http://localhost:4000
<h3>Hello World!</h3><b>Hostname:</b> 2b6d28400bfa<br/><b>Visits:</b> <i>cannot connect to Redis, counter disabled</i>


docker stack rm getstartedlab
docker swarm leave --force
