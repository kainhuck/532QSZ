# Docker 笔记

## 1. 给当前用户执行docker的权限

1. sudo groupadd docker
2. sudo gpasswd -a ${USER} docker
3. sudo systemctl restart docker

## 2. Linux下 `networknamespace`

1. 查看`networknamespace`

   ```shell
   sudo ip netns list
   ```

2. 创建`networknamespace`

   ```shell
   sudo ip netns add 名字
   ```

3. 删除`networknamespace`

   ```shell
   sudo ip netns delete 名字
   ```

4. 在`networknamespace`中执行命令

   ```shell
   sudo ip netns exec 名字 命令
   ```

   **查看ip信息**(blue为名字)

   ```shell
   sudo ip netns exec blue ip a
   ```

   **将设备设为up状态**(lo为设备名)

   ```shell
   sudo ip netns exec blue ip link set dev lo up
   ```

   

5. 创建一对veth peer来联通netns

   **创建一对veth peer**

   ```shell
   sudo ip link add 名字一 type veth peer name 名字二
   ```

   ```shell
   sudo ip link add blue-veth-a type veth peer name blue-veth-b
   ```

   

   **将一端放入netns**

   ```shell
   sudo ip link set 名字二 netns 网络空间名字
   ```

   ```shell
   sudo ip link set blue-veth-b netns blue
   ```

   6.给interface配置IP地址

   ```shell
   sudo ip addr add 192.168.1.1/24 dev blue-veth-a
   ```

   ```shell
   sudo ip netns exec blue ip addr add 192.168.1.2/24 dev blue-veth-b
   ```

   **记得把blue-veth-b给up**

   ```shell
   sudo ip netns exec blue ip link set dev blue-veth-b up
   ```

   **另一端（这里是本地）也要up**

   ```shell
   sudo ip link set dev blue-veth-a up
   ```

   


## 3. docker的bridge网络driver

1. 查看docker网络

   ```shell
   docker network ls
   ```

2. 查看linux bridge

   ```shell
   brctl show
   ```

3. 查看docker网络详细信息

   ```
   docker network inspect id或名字
   ```

4. 通过容器名称ping通（假设test2与test1联通）

   创建容器时加上--link参数

   ```
   docker run -d --name test2 --link test1 busybox sh -c "while true; do sleep 2000; done"
   ```

   这样在test1无法通过名字ping通test2

   *只要连接的不是默认的bridge默认已经link上了*

   

5. 创建自己的bridge

   **创建**
   
   ```
   docker network create -d bridge 名字
   ```
   
   **创建container链接到自己的bridge**
   
   加上--network
   
   ```
   docker run -d --name test2 --network my-bridge busybox sh -c "while true; do sleep 2000; done"
   ```
   
   **让已经存在的容器连接到我们的bridge**
   
   ```
   docker network connect my-bridge test1
   ```

## 4.docker端口映射

例

**将容器的80端口映射到本地的80端口**

```
docker run -d --name web -p 80:80 nginx
```

**这样直接访问本地就OK了**

```
curl 127.0.0.1
```

## 5.docker的host网络driver

host可以使容器拥有和本地同一个网络空间

例：

```、
docker run -d --name web --network host nginx
```

本地可以直接访问

```
curl 127.0.0.1
```

