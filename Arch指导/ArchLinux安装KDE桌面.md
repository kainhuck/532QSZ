# ArchLinux安装KDE桌面

## 一.链接网络

### 1.有线

```
# dhcpcd
```

### 2.无线

```
# wifi-menu
```

### 3.检查

```
# ping www.baidu.com
```



## 二.安装X服务

```
# pacman -S xorg
```



## 三.安装触摸板驱动

```
# pacman -S xf86-input-synaptics
```



## 四.安装中文字体包

```
# pacman -S ttf-dejavu wqy-microhei
```



## 五.创建普通用户

kain 为自己用户名

```
# useradd -m -G wheel -s /bin/bash kain
# passwd kain
# vim /etc/suders
```



## 六.安装桌面

```
# pacman -S plasma kde-applications
```



## 七.安装图形登录界面

### 1.安装sddm

```
# pacman -S sddm sddm-kcm
```

### 2.开启sddm服务

```
# systemctl enable sddm
```



## 八.安装网络工具

### 1.安装

```
# pacman -S networkmanager net-tools
```

### 2.启动

```
# systemctl enable NetworkManager
# systemctl enable dhcpcd
```



## 九.安装声音软件包

```
# pacman -S alsa-utils pulseaudio pulseaudio-alsa
```



## 十.安装KDE中文语言包

```
# pacman -S kde-l10n-zh_cn
```



## 十一.安装中文输入法

取消zh_CN.UTF-8的注释并刷新

```
# vim /etc/locale.gen
# locale-gen
```

```
# pacman -S fcitx fcitx-rime fcitx-im kcm-fcitx
# vim /home/<username>/.xprofile

export LANG=zh_CN.UTF-8
export LC_ALL=zh_CN.UTF-8
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
```



