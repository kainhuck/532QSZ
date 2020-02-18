# CentOS搭建v2ray

## 1. **安装wget**

```shel
yum -y install wget
```



## 2. **下载脚本**

```shell
wget https://install.direct/go.sh
```



## 3. **安装unzip**

```shell
yum install -y zip unzip  
```



## 4. **执行安装**

```shell
bash go.sh
```



## 5. **启动v2ray**

```bash
systemctl start v2ray
systemctl enable v2ray
```



## 6. **查看配置**

```shell
cat /etc/v2ray/config.json
```



## 7. 注意

确保你的服务器对应的端口开放



## 8. linux下的v2ray图形界面客户端

```
yay -S qv2ray
pacman -S v2ray
```

