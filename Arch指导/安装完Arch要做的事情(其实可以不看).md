# 安装完Arch要做的事情

## 一.创建普通用户

### 1.安装zsh

个人比较喜欢的一个shell,你们可以和我不同

```
# pacman -S zsh
```

### 2.创建用户

kain是我创建用户的名字

```
# useradd -m -G wheel -s /bin/zsh kain
```

### 3.为新用户设置密码

```
# passwd kain
```

### 4.赋予新用户sudo权限

将/etc/sudoers中`# %wheel ALL=(ALL) ALL`前面的`#`去掉

```
# vim /etc/sudoers
```



## 二.安装第三方应用

### 1.火狐浏览器

```
# pacman -S firefox
```

### 2.安装Tilix

这是一个第三方终端,推荐装上

自带终端太难看了,二来可能自带的终端无法使用

```
# pacman -S tilix
```



## 三.配置中文环境

在/etc/locale.gen中取消掉`zh_CN.UTF-8`前面的注释

然后

```
# locale-gen
```

```
# vim ~.xprofile

写入
export LANG=zh_CN.UTF-8
export LANG=zh_CN:en_US
export LC_CTYPE=en_US.UTF-8
```

下一步可不做

```
# vim /etc/locale.conf
加入
LANG=zh_CN.UTF-8
```

下载中文字体

```
# pacman -S wqy-zenhei
```

## 四.安装QQ

```
# yay deepin.com
```

