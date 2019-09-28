## Docker 总结

## 1. 说在前头(Docker命令的格式)

docker中的对象分为4个(就目前我所学到的)

1. 镜像  image
2. 容器  container
3. 网络  network
4. 数据卷 volume

docker 对不同对象的操作格式为

docker (对象类型) (命令) [参数] (对象名)

比如,删除一个名为mysql的容器

`docker container rm mysql`

这些命令有:

| 命令    | 功能         |
| ------- | ------------ |
| rm      | 删除         |
| inspect | 查看详细信息 |
| start   | 启动容器     |
| stop    | 关闭容器     |
| create  | 创建         |
| ls      | 列出         |
|         |              |



## 2.容器

### 创建容器

创建并运行一个容器的命令为

`docker run --name [名字] -d 镜像名:标签 一些要执行的命令`

如果不加执行命令,容器会执行dockerfile里指定的命令(如果存在)

比如:

`docker run --name mysql -d mysql:5.7`

这里基于mysql 5.7创建了一个容器并取名为mysql,并且使其后台运行(-d)

镜像名后不跟标签默认为latest

--------------

将`run`改成`create`则为创建容器不运行

用`start`命令启动容器

用`stop`命令停止容器

-----

列举一些参数

| 参数名    | 功能                                      | 列举                       |
| --------- | ----------------------------------------- | -------------------------- |
| --name    | 给容器取名字                              | --name mysql               |
| -d        | 后台运行容器                              | -d                         |
| -e        | 指定环境变量                              | -e MYSQL_ROOT_PASSWORD=123 |
| -v        | 设置数据卷                                | -v mysql:/var/lib/mysql    |
| --network | 这是网络(默认bridge)                      | --network host             |
| -p        | 映射端口                                  | -p 80:80                   |
| -P        | 映射所有开放端口到本地(随机)              | -P                         |
| --link    | 连接到某个已存在的容器,方便使用容器名访问 | --link mysql               |

----

### 进入容器

常用命令为

`docker exec -it 容器名 /bin/bash`

`exec`为执行命令的命令

`-it`就是 `-i`和`-t` ,`-i`表示标准输入保持打开,`-t`表示分配一个伪终端

这里执行的命令为`/bin/bash`,一般的容器都带有`bash`,有些则用`sh`

### 查看容器详细信息

`docker container inspect 容器名`

## 网络

通过命令`docker network ls 可以查看`当前拥有哪些网络类型,通常有一下几种:

1. bridge 桥类型,也是默认类型,默认只能通过ip平通
2. host 主机类型,和主机共享网络,这样就不必使用端口映射
3. none   不指定任何网卡,只有lo

使用`bridge`的两个网络通过ip可以ping通.若使用--link来创建容器时可以通过容器名ping通,但这是单向的,例:

已存在容器a,创建容器b时指定`--link a`则在容器b使用命令`ping a`可以ping通,在a里使用命令`ping b`则不行

一种特殊情况,

可以创建一个自己的网络指定类型为`bridge`,再创建几个容器连接到自己创建的网络上,则这些容器可以通过名字互相ping通.例:

`docker network create -d bridge my_bridge`

注:这里的`-d`为指定网络的类型



## 数据卷

数据卷一般用于数据持久化,下面以dockerhub官方的mysql镜像为例,

查看mysql的dockerfile可以看到`VOLUME /var/lib/mysql`这一行,说明mysql将数据存储在容器中的`/var/lib/mysql`目录下,并自动挂载到一个主机的目录可以`inspect`容器或者volume(启动一个mysql容器会产生一个volume,可以用docker volume ls查看)就可以看到详细的目录.但是自动生成的volume名字十分冗长,

**修改volume的名字**

`docker run --name mysql1 -d -v mysql_v_name:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=1 mysql`

上面的命令是常见的启动mysql容器的命令,其中`-v mysql_v_name:/var/lib/mysql`命令指定了本地的挂载点`:`前面就是本地的目录,后面就是容器里的目录(可以通过dockerfile查看),相当于重命名

通过inspect可知道全路径为:`"/var/lib/docker/volumes/mysql_v_name/_data"`

**这样的优点**

创建第二个容器

`docker run --name mysql2 -d -v mysql_v_name:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=1 mysql`

注意这里的`-v`后面指定的名字是前一个容器的挂载点,这样一来,前一个容器删除后,第二个容器可以接着使用第一个容器的数据.

**共享主机的文件夹**

注意一个原则,我们尽量不要在容器里面操作,应当在外面通过命令来操控容器,通常情况下,容器是不带vim或其他文本编辑工具的,所以一种有效的的办法是通过主机和容器共享一个文件夹,这样一来就可以在主机里通过vim等工具来编写代码.

`docker run --name test -d -v /home/kainhuck/Documents/PyCode:/temp/PyCode python:3.7`

这里创建一个Python3.7的容器,并将本地文件夹`/home/kainhuck/Documents/PyCode`关联到容器里的`/temp/PyCode`目录.

这种方式关联的文件相当于同一个文件,操作均为同步,里面修改,外面也会修改.