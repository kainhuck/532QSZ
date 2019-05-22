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

#### ①基于已有镜像的容器创建

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

#### ②基于本地模板导入

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

使用docker create命令新建容器,例如:

sudo docker create -it ubuntu:latest

使用docker create命令新建的容器处于停止状态,

### 2.启动容器

使用docker start来启动已经创建的容器

sudo docker start CONTAINER

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





 