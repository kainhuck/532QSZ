# docker学习笔记

## 一.安装

sudo pacman -S docker

## 二.镜像

### 1.获取镜像

sudo docker pull 镜像名[:标签名]

### 2.查看镜像信息

sudo docker images

### 3.给镜像添加标签

sudo docker tag 镜像名:标签名 新名字:新标签名

### 4.搜寻镜像

sudo docker search 镜像名

### 5.删除镜像

sudo docker rmi 镜像名标签名

sudo docker rmi 镜像ID

*注:无法删除已经创建容器的镜像*

sudo docker rmi -f 镜像名或ID		# 强制删除,不推荐,应先删除容器

### 6.创建镜像

#### ①.基于已有镜像的容器创建

命令格式为:

**docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]**

> 主要选项
>
> -a,	--author=""		# 作者信息
>
> -m,	--message=""	# 提交信息
>
> -p,	--pause=ture	# 提交时暂停容器运行

例:

```
 kain@archlinux ~$ sudo docker commit -a "kain huck" -m "first build a image" e4f60aee5987 my_image
```

#### ②.基于本地模板导入

也可以直接从一个操作系统模板文件导入一个镜像.推荐使用OpenVZ提供的模板来创建.地址为:

http://openvz.org/Download/templates/precreated

假如下载了一个ubuntu-14.04的模板压缩包后,可以使用一下命令导入:

sudo cat ubuntu-14.04-x86_64-minimal.tar.gz | docker import - ubuntu:14.04

### 7.存出和载入镜像

#### ①.存出镜像

sudo docker save -o 镜像名.tar 镜像名

#### ②.载入镜像

sudo docker load --input 镜像名.tar

或

sudo docker load < 镜像名.tar

### 8.上传镜像

默认上传到DockerHub官方仓库(需要登录),格式为:

docker push NAME[":TAG"]

用户在DockerHub网站注册后,即可上传自制镜像.例如用户user上传本地的test:latest镜像,可以先添加新的标签user/test:latest,然后用docker push命令上传镜像:

sudo docker tag test:latest user/test:latest

sudo docker push user/test:latest

第一次使用时,会提示输入登录信息或进行注册

## 三.容器

### 1.新建容器

使用docker create命令新建容器,命令格式为:

**docker create [OPTIONS] IMAGE [COMMAND] [ARG...]**

例如:

**sudo docker create -it ubuntu:latest**

使用docker create命令新建的容器处于停止状态,

### 2.启动容器

使用docker start来启动已经创建的容器

**sudo docker start CONTAINER**

### 3.新建并启动容器

使用docker run命令,例如:

sudo docker run ubuntu /bin/echo 'hello world'

> 后台的操作包括
>
> 1.检查本地是否存在指定的镜像,不存在就从公有仓库下载
>
> 2.利用镜像创建并启动一个容器
>
> 3.分配一个系统文件,并在只读镜像层外面挂载一层可读写层
>
> 4.从宿主主机配置的网桥接口中桥接一个虚拟接口到容器中去
>
> 5.从地址池配置一个IP地址给容器
>
> 6.执行用户指定的应用程序
>
> 7.执行完毕后容器被终止

启动一个bash终端

sudo docker run -t -i ubuntu:14.04 /bin/bash

> -t	# 分配一个伪终端
>
> -i	# 标准输入保持打开
>
> 用exit退出后docker进入终止状态

### 4.守护态运行

通过 **-d** 参数来实现,例如:

sudo docker run -d ubuntu /bin/sh -c "while true; do echo hello world; sleep 1; done"

利用 **sudo docker ps** 查看运行的容器

利用 **sudo docker ps -a** 查看所有的容器

获取容器输出信息

sudo docker logs CONTAINER

### 5.终止容器

命令格式为:

**docker stop [-t|--time [=10]]**

此外,当docker容器中指定的容器终结后,容器也自动终止.使用**exit**或**Ctrl+d**来退出终端时,容器也立即终止.

例如(ce5为容器id):

**sudo docker stop ce5**

使用如下命令查看所有终止状态的容器:

**sudo docker ps -a -q**

### 6.进入容器

#### ①.attach命令

**sudo docker attach CONTAINER**

*注:所有窗口同步显示 ,存在阻塞风险*

#### ②.exec命令

**docker exec [OPTIONS] CONTAINER COMMAND [ARG...]**

#### ③.nsenter工具

检查是否已经存在该工具,不存在则安装(以archLinux为例):

**sudo pacman -S nsenter**

找到容器的PID

**PID=$(docker inspect --format "{{ .State.Pid }}" \<container>)**

利用该PID连接容器

**nsenter --target $PID --mount --uts --ipc --net --pid**

### 7.删除容器

命令格式为:

**docker rm [OPTIONS] CONTAINER [CONTAINER...]**

> -f, --force=false	# 强行终止并删除一个运行中的容器
>
> -l, --link=false	# 删除容器的连接,但保留容器
>
> -v, --volumes=false	# 删除容器挂载的数据卷

### 8.导入和导出容器

#### ①.导出容器

命令格式为:

**docker export [OPTIONS] CONTAINER**

例如,将ce5542...容器导出到test.tar文件:

**sudo docker export ce5 > test.tar**

#### ②.导入文件

命令格式为:

**docker import [OPTIONS] file|URL|- [REPOSITORY[:TAG]]**

例如:

**cat test.tar | sudo docker import - test/ubuntu:v1.0**

## 四.仓库

### 1.Docker Hub

这是docker官方维护的公共仓库,网址为:

https://hub.docker.com

#### ①.登录

通过**docker login**命令来输入用户名,密码和邮箱来完成注册和登录.注册成功后,本地用户目录的**.dockercfg**中将保存用户的认证信息

#### ②.基本操作

**docker search**	# 查找镜像(无需登录)

**docker pull**	# 下载镜像(无需登录)

**docker push**	# 上传镜像(需登录)

#### ③.自动创建

步骤如下:

1. 创建并登录Docker Hub,以及目标网站;* 在目标网站中链接账户到Docker Hub.

2. 在Docker Hub中配置一个自动创建.
3. 选取一个目标网站中的项目(需要含Dockerfile)和分支.
4. 指定Dockerfile的位置,并提交创建

### 2.Docker Pool(已废弃)

Docker Pool是国内的Docker技术社区,提供镜像下载,网址为:

http://dockerpool.com

#### ①.查看镜像

访问*http://www.dockerpool.com/downloads*,即可查看

#### ②.下载镜像

在镜像前添加服务器具体的地址 dl.dockerpool.com:5000

例如,下载一个ubuntu仓库的12.04镜像:

**sudo docker pull dl.dockerpool.com:5000/ubuntu:12.04**

### 3.创建和使用私有仓库

**sudo docker run -d -p 5000:5000 registry**

这将自动下载并启动一个registry容器,创建本地的私有仓库服务

默认将仓库创建在容器的/tmp/registry目录下,可使用-v参数更改为本地路径,如:

sudo docker run -d -p 5000:5000 -v /opt/data/registry:/tmp/registry registry

### 4.管理私有仓库镜像

假设搭建私有仓库的地址为*10.0.2.2:5000*

查看已有镜像

**sudo docker images**

给镜像贴标签

**sudo docker tag ubuntu:14.04 10.0.2.2:5000/test**

上传镜像

**sudo docker push 10.0.2.2:5000/test**

用curl查看仓库10.0.2.2:5000中的镜像

**curl http://10.0.2.2:5000/()/search**

从另一台可访问10.0.2.2:5000的电脑上下载该镜像

**sudo docker pull 10.0.2.2:5000/test**

## 五.数据管理

### 1.数据卷

数据卷是一种可供容器使用的特殊目录,它绕过文件系统,具有以下特性:

1. 数据卷可以在容器之间共享和重用
2. 对数据卷的修改会立马生效
3. 对数据卷的更新不会影响镜像
4. 卷会一直存在,直到没有容器使用

#### ①.在容器内创建一个数据卷

在执行**docker run**命令是加上 **-v** 参数创建数据卷(可以创建多个),例如

使用training/webapp镜像创建一个web容器,并创建一个数据卷挂载到容器的/webapp目录:

**sudo docker run -d -P --name web -v /webapp training/webapp python app.py**

*-P 是允许外部访问容器需要暴露的端口*

#### ③.挂载一个主机目录作为数据卷

挂载一主机的/src/webapp目录到容器的/opt/webapp目录

**sudo docker run -d -P --name web -v /src/webapp:/opt/webapp training/webapp python app.py**

*注意:必须为绝对路径,默认权限为读写(rw)*

设置为只读(ro):

**sudo docker run -d -P --name web -v /src/webapp:/opt/webapp:ro training/webapp python app.py**

#### ④.挂载一个本地主机文件作为数据卷

**sudo docker run --rm -it -v ~/.bash_history:/.bash_history ubuntu /bin/bash**

*注:--rm标记会使容器使用完后立即删除,不能和-d同时使用*

### 2.数据卷容器


用于容器之间共享数据

1. 创建数据卷容器dbdata,并在其中创建一个数据卷挂载到/dbdata:

   **sudo docker run -it -v /dbdata --name dbdata ubuntu**

2. 在其他容器中使用--volumes-from来挂载dbdata容器中的数据卷(db为容器名)

   **sudo docker run -it --volumes-from dbdata --name db ubuntu**

3. 这样就已经实现数据共享了,注意--volumes-from可以使用多次

### 3.利用数据卷容器迁移数据

#### ①.备份

**sudo docker run --volumes-from dbdata -v $(pwd):/backup --name worker ubuntu tar cvf /backup/backup.tar /dbdata**

解释:

> 首先利用ubuntu镜像创建了一个容器worker.使用--volumes-from dbdata参数来让worker容器挂载dbdata容器的数据卷(即dbdata数据卷);使用-v $(pwd):/backup参数来挂载本地的当前目录到worker容器的/backup目录.
>
> worker容器启动后,使用了tar cvf /backup/backup.tar /dbdata命令来将/dbdata下的内容备份为容器内的/backup/backup.tar,即宿主主机当前目录下的backup.tar.

#### ②.恢复

1. 先创建一个带有数据卷的容器dbdata2:

   **sudo docker run -v /dbdata --name dbdata2 ubuntu /bin/bash**

2. 创建一个新的容器挂载dbdata2的容器,并使用untar解压备份文件到所挂载的容器卷中即可

   **sudo docker run --volumes-from dbdata2 -v $(pwd):/backup busybox tar xvf /backup/backup.tar**

## 六.网络基础配置

### 1.端口映射实现访问容器

#### ①.从外部访问容器应用

使用-P随机映射一个49000~49900的端口到容器内部

**sudo docker run -d -P training/webapp python app.py**

查看:

**sudo docker ps -l**

或者:

**sudo docker logs -f CONTAINER**

-p可以指定端口,并且可以绑定容器,格式为:

**ip:hostPort:containerPort | ip::containerPort | hostPort:containerPort**

#### ②.映射所有接口地址

hostPort:containerPort

**sudo docker run -d -p 5000:5000 -p 3000:80 training/webapp python app.py**

#### ③映射指定地址到指定端口

ip:hostPort"containerPort

**sudo docker run -d -p 127.0.0.1:5000:5000 training/webapp python app.py**

#### ④.映射指定地址到任意端口

ip::containerPort

系统自动分配:

**sudo docker run -d -p 127.0.0.1::5000 training/webapp python app.py**

指定udp端口:

**sudo docker run -d -p 127.0.0.1:5000:5000/udp training/webapp python app.py**

#### ⑤.查看映射端口配置

sudo docker port CONATINER 5000

### 2.容器互联实现容器间通信

#### ①.自定义容器命名

使用--name标记

**sudo docker run -d -P --name web training/webapp python app.py**

使用docker ps来验证设定的名字

**sudo docker ps -l**

使用docker inspect来查看容器的名字

**sudo docker inspect -f "{{ .Name }}" aed84ee21bds**

*注意:名字唯一*

#### ②.容器互联

使用--link参数

例如:

1. 创建新的数据库容器

   **sudo docker run -d --name db training/postgres**

2. 删除之前创建的web容器

   **sudo docker rm -f web**

3. 创建一个新的web容器,并将它连接到db容器

   **sudo docker run -d -P --name web --link db:db training/webapp python app.py**

--link的格式:

--link name:alias

name是要链接的容器的名称

alias是这个链接的别名

可以使用docker ps查看链接

### 3.公开连接信息的两种方式

#### ①.环境变量

env命令

**sudo docker run --rm --name web2 --link db:db training/webapp env**

前缀采用大写的连接别名

#### ②./etc/hosts文件

进入容器后

cat /etc/hosts

## 七.使用Dockerfile创建镜像

### 1.基本结构

Dockerfile分为四个部分

1. 基础镜像信息
2. 维护者信息
3. 镜像操作指令
4. 容器启动时执行指令

```dockerfile
# This dockerfile uses the ubuntu image
# VERSION 2 -EDITION 1
# Author: docker_user
# Command format: Instruction [arguments / command] . .

# 第一行必须指定基础的镜像
FROM ubuntu

# 维护者信息
MAINTAINER docker_user docker_usr@email.com

# 镜像的操作指令
RUN echo "deb http://archive.ubuntu.com/ubuntu/ raring main universe" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y nginx
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf

# 容器启动时执行的命令
CMD /usr/sbin/nginx
```

### 2.指令

一般格式为

INSTRUCTION arguments

#### ①.FROM

格式为:

**FROM \<image>**

第一条指令必须为FROM,并且如果在同一个Dockerfile中创建多个镜像时,可以使用多个FROM

#### ②.MAINTAINER

格式为:

**MAINTAINER \<name>**

指定维护者信息

#### ③.RUN

格式为:

**RUN \<command>**

或

**RUN ["executable", "paraml", "param2"]**

前者在shell终端中运行指令, 即/bin/sh -c;后者使用exec执行.

指定使用其他终端也可以使用第二种,例如

RUN ["/bin/bash", "-c", "echo hello"]

每条RUN指令将在当前镜像的基础上执行指定的命令,并提交为新的镜像.当命令较长时可以使用**\\**来换行.

#### ④.CMD

支持三种格式:

**CMD ["executable", "paraml", "param2"]**	使用exec执行,推荐方式

**CMD command param1 param2**	在/bin/sh中执行,提供给需要交互的应用

**CMD ["paraml", "param2"]**	提供给ENTRYPOINT的默认参数

容器启动时执行的命令,一个Dockerfile文件只能有一条CMD命令

#### ⑤.EXPOSE

格式为:

EXPOSE \<port> [\<port>. . .]

例如:

**EXPORT 22 80 8443**

告诉Docker服务端暴露的端口号,供互联系统使用.

#### ⑥.ENV

格式为:

ENV \<key> \<value>

指定一个环境变量,会被后续RUN指令使用,并在容器中运行时保持.

例如:

```dockerfile
ENV PG_MAJOR 9.3
ENV PG_VERSION 9.3.4
RUN curl -SL http://example.com/postgres-$PG_VERSION.tar.xz | tar -xJC /usr/src/postgress && ...
ENV PATH /usr/local/postgres-$PG_MAJOR/bin:$PATH
```

#### ⑦.ADD

格式为:

ADD \<src> \<dest>

该指令将复制指定的\<src>到容器中的\<dest>.其中\<src>可以是Dockerfile所在目录的一个相对路径(文件或目录);也可以是一个URL;还可以是一个tar文件(自动解压为目录)

#### ⑧.COPY

格式为:

COPY \<src> \<dest>

复制本地主机的\<src>(为Dockerfile所在目录的相对路径,文件或目录)为容器中的\<dest>.路径不存在时自动创建.

当使用本地目录为

#### ⑨.ENTRYPOINT

格式为:

ENTRYPOINT ["executable", "parama1", "param2"]

ENTRYPOINT command param1 param2 (shell中执行)

配置容器启动后执行的命令,并且不可被docker run提供的参数覆盖.

每个Dockerfikle中只能有一个ENTRYPOINT.

#### ⑩.VOLUME

格式为:

VOLUME ["/data"]

创建一个可从本地主机或其他容器挂载的挂载点,一般用来存放数据库和需要保持的数据等.

#### 11.USER

格式为:

USER daemon

指定运行容器时的用户名或UID,后续的RUN也会使用指定用户.

当服务不需要管理员权限时,可以通过该命令指定运行用户.并且可以在之前创建所需要的用户,例如:

RUN groupadd -r postgres && useradd -r -g postgres postgres

要临时获取管理员权限可以使用gous,而不推荐sudo.

#### 12.WORKDIR

格式为:

WORKDIR /path/to/workdir

为后续的RUN, CMD, ENTRYPOINT指令配置工作目录.

可以使用多个WORKDIR指令,后续命令如参数是相对路径,则会基于之前命令指定的路径.例如:

WORKDIR /a

WORKDIR b

WORKDIR c

RUN pwd

则最终路径是/a/b/c

#### 13.ONBUILD

格式为:

ONBUILD [INSTRUCTION]

配置当所创建的镜像作为其他新创建镜像的基础镜像时,所执行的操作指令.例如,Dockerfile使用如下的内容创建镜像image-A.

[...]

ONBUILD ADD . /app/src

ONBUILD RUN /usr/local/bin/python-build --dir /app/src

[...]

如果基于image-A创建新的镜像时,新的Dockerfile中使用FROM image-A指定基础镜像时,会自动执行ONBUILD指令内容,等价于在后面添加了两条指令.

```dockerfile
FROM image-A

# Automatically run the following
ADD . /app/src
RUN /usr/local/bin/python-build --dir /app/src
```

使用ONBUILD指令的镜像,推荐在标签中注明,例如ruby:1.9-onbuild

### 3.创建镜像

**docker build [OPTIONS] PATH | URL | -**

该命令将读取指定路径下(包括子目录)的Dockerfile,并将该路径下所有内容发送给Docker服务端,由服务端来创建镜像.因此一般建议放置Dockerfile的目录为空目录.

另外,可以通过.dockeringnore文件(每一行添加一条匹配模式)来让Docker忽略路径下的目录和文件.

要指定镜像的标签信息,可以通过**-t**选项.

例如,指定Dockerfile所在路径为/tmp/docker_builder/,并且希望生成镜像标签为build_repo/first_image,可以使用下面的命令:

sudo docker build -t build_repo/first_image /tmp/docker_builder/