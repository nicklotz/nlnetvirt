# Lab: Networking in Docker

## A. Prerequisites
### Install Docker (if not already)
Docker has a convenient installation script if you're on a *nix-based system. If you're on Windows, [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/) is recommended.
1. In a terminal, download the Docker install script.

```
curl -fsSL https://get.docker.com -o get-docker.sh
```

2. Run the Docker install script.  
sh get-docker.sh

3. Set permissions so you can run Docker without sudo.

```
sudo groupadd docker
sudo usermod -aG docker $USER
```

4. For the permissions to take effect, logout and back in and/or open a new user shell.

5. Test the Docker installation.

```
docker run hello-world
```

Let your instructor know if you get a permissions error and/or are unable to run Docker without sudo.

## B. Create and use a Docker network

1. Create a custom bridge network. These are isolated on a single host.

```
docker network create --driver bridge mybridgenet
```

2. Create two NGINX containeres on the **mybridgenet** network.

```
docker run -dit --name nginx1 --network mybridgenet nginx
docker run -dit --name nginx2 --network mybridgenet nginx
```

3. Inspect the new network with containers attached.

```
docker network inspect mybridgenet
```

4. Save the IP addresses of both containers.

```
NGINX1_IP=`docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' nginx1`
NGINX2_IP=`docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' nginx2`
echo "IP address of nginx1 is $NGINX1_IP"
echo "IP address of nginx2 is $NGINX2_IP"
```

5. Test connectivity between the two containers.

```
docker exec nginx1 curl http://$NGINX2_IP
docker exec nginx2 curl http://$NGINX1_IP
```

6. Create a container **not** yet connected to your custom network.

```
docker run -dit --name nginx3 nginx
```

7. Connect the new container to your existing custom network.

```
docker network connect mybridgenet nginx3
```

8. Save the IP address of the third container.

```
NGINX3_IP=`docker inspect nginx3 -f '{{.NetworkSettings.Networks.mybridgenet.IPAddress}}'`
echo $NGINX3_IP
```

9. Test connectivity to nginx3 from another container.

```
docker exec nginx1 curl http://$NGINX3_IP
```

10. Disconnect nginx3 from your custom network.

```
docker network disconnect mybridgenet nginx3 
```

11. Try communicating with nginx3 again. Does it work?

```
docker exec nginx1 curl http://$NGINX3_IP
```

12. The connection attempt should hang. Type **CTRL-C** to kill the connection attempt.

12. Clean up the resources you've created so far.

```
docker container stop nginx1 nginx2 nginx3
docker container rm nginx1 nginx2 nginx3
docker network rm mybridgenet
```










 
