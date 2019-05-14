# 给Arch安装Gnome桌面美化及常用软件配置

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



## 二.安装桌面

### 1.安装基本桌面

```
# pacman -S xorg
# pacman -S gnome
```

### 2.开启登录管理器

这里使用gdm

```
# systemctl enable gdm
```



## 三.安装第三方应用

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



## 四.配置中文环境

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

```
# vim /etc/locale.conf
加入
LANG=zh_CN.UTF-8
```



下载中文字体

```
# pacman -S wqy-zenhei
```



## 五.重启

```
# reboot
```

注意再次进入时选择GNOME on Xorg



## 六.更改pacman.conf

### 1.编辑pacman.conf文件

1.在 /etc/pacman.conf 文件末尾添加：

```
[archlinuxcn]
Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch
```

### 2.打开32位仓库

将下面的文字注释去掉

```
[multilib]
Include = /etc/pacman.d/mirrorlist
```

### 3.刷新

```
# sudo pacman -Syy
```

### 4.安装密钥包

```
# sudo pacman -S archlinuxcn-keyring
```



## 七.安装中文输入法

### 1.安装命令

```
# pacman -S fcitx-im
# pacman -S fcitx-sogoupinyin
# pacman -S fcitx-configtool
```

之后打开fcitx-configtool选择搜狗输入法即可

### 2.编辑xprofile文件

```
# vim ~/.xprofile

写入
export XIM=fcitx
export XIM_PROGRAM=fcitx
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx"
```

### 3.重启

```
# reboot
```



## 八.安装网易云音乐

```
# sudo pacman -S netease-cloud-music
```





## 九.美化zsh

### 1.安装git

```
# sudo pacman -S git
```

### 2.安装ohmyzsh

```
# sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

### 3.编辑ohmyzsh

```
# vim .zshrc
修改ZSH_THEME为你喜欢的
在plugins里面添加上sudo
```

### 4.生效.zshrc

```
# source .zshrc
```

### 5.右键打开tilix

```
# sudo pacman -S python-nautilus
```



## 十.AUR

```
# pacman -S yay yaourt
```



## 十一.gnome主题美化

### 1.安装gnome-tweaks

```
# pacman -S gnome-tweaks
```

### 2.安装主题和图标

先打开User themes App menu

```
# yay flat-remix
# yay vimix
# pacman -S papirus-icon-theme
```

### 3.安装docky

```
# pacman -S docky
# pacman -S gconf-editor
```

取消docky图标

取消gconf-editor --> apps --> docky-2 --> Docky --> items --> Dockyitem --> show

### 4.两个美化网站

```
extensions.gnome.org
gnome-look.org
```

