# 手动搭建ssr

## 1.购买服务器

```
https://www.vultr.com/
```

​		选择**CentOS6**或者**CentOS7**

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

## 4.加速(Cent6)

bbr加速

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

## 4.加速(Cent7)

速锐加速

```shell
wget --no-check-certificate -O rskernel.sh https://raw.githubusercontent.com/hombo125/doubi/master/rskernel.sh && bash rskernel.sh
```

这里会自动重启,然后执行下面

```shell
yum install net-tools -y && wget --no-check-certificate -O appex.sh https://raw.githubusercontent.com/0oVicero0/serverSpeeder_Install/master/appex.sh && bash appex.sh install
```

一路回车

# **OK**

