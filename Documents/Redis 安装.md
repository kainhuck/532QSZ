# Redis 安装

### 1.下载

```
wget http://download.redis.io/releases/redis-5.0.5.tar.gz
```

### 2.解压

```
tar -zxvf redis-5.0.5.tar.gz
```

### 3.进入解压目录

```
cd redis-5.0.5 
```

### 4.编译

```
make
```

### 5.安装/指定安装目录

```
sudo make PREFIX=/usr/local/redis install
```

### 6.切换到安装目录

```
cd /usr/local/redis
```

### 7.把配置文件复制到redis安装目录下

```
sudo cp /home/huck/Documents/redis-5.0.5/redis.conf ./
```

### 8.修改redis配置文件

```
sudo vim redis.conf
```

将*daemonize no*改为 *daemonize yes*,(后台运行redis)

将 *logfile ""* 改为 *logfile "/usr/local/redis/redis.log"*(日志文件路径,自定义) 

设置密码登录

取消 ***requirepass*** 前面的注释后面为登录密码

登录时加上 *-a password*

9. 启动redis

*redis-server redis.conf*

```
/usr/local/redis/bin/redis-server /usr/local/redis/redis.conf
```

查看是否启动成功*ps -aux | grep redis*

10. 连接redis服务

*连接命令 -h 主机ip -p 端口*

如果是本地连接,直接输入连接命令即可

```
/usr/local/redis/bin/redis-cli
```

11. 正常关闭redis服务

```
/usr/local/redis/bin/redis-cli shutdown
```

------

## 为了方便启动可以做如下操作

1. 方便启动客户端

   将`/usr/local/redis/bin/redis-cli`链接到`/usr/local/bin`目录下

   ```
   sudo ln /usr/local/redis/bin/redis-cli /usr/local/bin
   ```

2. 方便启动服务端

   在`/usr/local/bin`下编写脚本`redis_run.sh`用以启动redis服务

   ```
   cd /usr/local/bin
   ```

   ```
   sudo echo -e '#!/bin/bash\n`sudo /usr/local/redis/bin/redis-server /usr/local/redis/redis.conf`' > redis_run.sh
   ```

   ```
   sudo chmod +x redis_run.sh
   ```

   以后启动redis服务时,可在任意目录下输入命令`redis_run.sh`

   启动客户端时可在任意目录下输入`redis-cli`