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
docker network create --driver bridge my-bridge-network
```

2. Create two NGINX containeres on the **my-bridge-net** network.

```
docker run -dit --name nginx1 --network my-bridge-network nginx
docker run -dit --name nginx2 --network my-bridge-network nginx
```

3. Inspect the new network with containers attached.

```
docker network inspect my-bridge-network
```

4. Test connectivity between the two containers.

```
docker exec nginx1 ping -c 4 nginx2
```

5. Create a container **not** yet connected to your custom network.

```
docker run -dit --name nginx3 nginx
```

6. Connect the new container to your existing custom network.

```
docker network connect my-bridge-network nginx3
```

7. Disconnect the container from your custom network.

```
docker network disconnect my-bridge-network nginx3 
```

8. Clean up the resources you've created so far.

```
docker container stop nginx1 nginx2 nginx3
docker container rm nginx1 nginx2 nginx3
docker network rm my-bridge-network
```










 
