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

