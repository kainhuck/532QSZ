# 手动搭建ssr

## 1.购买服务器

```
https://www.vultr.com/
```

​		选择CentOS6 x64

## 2.链接你的服务器

```
ssh root@yourip	
```

## 3.搭建ssr

```
yum -y install wget
```

```
wget --no-check-certificate https://freed.ga/github/shadowsocksR.sh; bash shadowsocksR.sh
```

​		这里设置密码和端口，等待安装成功注意保存信息！！！！


## 4.加速

```
wget --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh
```

```
chmod +x bbr.sh
```

```
./bbr.sh
```

​		这里输入 **y** 重启服务器，稍等片刻，就OK了

