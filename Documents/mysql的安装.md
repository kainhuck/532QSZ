# mysql的安装

***这里安装的是mariadb一个mysql的开源版本，实际使用体验没有差别***

## 1. 安装Maria DB

```
sudo pacman -S mariadb
```

## 2. 配置目录

```
sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
```

## 3. 启动Maria DB

```
sudo systemctl start mysqld
```

## 4. 为root用户设置一个新密码

```
sudo mysqladmin -u root password '12345678'
```

至此已经可以进入数据库了，命令`mysql -u root -p`

## 5. root用用户开启远程访问

先进入数据库

1. 选中mysql数据库

```
use mysql;
```

2. 更改root的访问权限

   可以先查看当前权限信息（不是必须）

   `select  user,authentication_string,host from user;`

   123456 为你设置的root用户密码

```
 GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456';
```

3. 刷新数据

```
flush privileges;
```

## 6. 将mysql设为开机自启

```
sudo systmctl enable mysqld
```

