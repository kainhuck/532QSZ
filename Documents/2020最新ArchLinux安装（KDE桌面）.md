# 2020最新ArchLinux安装（KDE桌面）

许多网友反映之前的教程安装好后连不上互联网，最近我刚好又安装了一遍，总结出以下没毛病的过程

按照此教程需要你会基本的`vim`操作（或其他文本编辑工具比如`nano`），基本的`fdisk`分盘操作(或其他分盘工具)，`fdisk`的使用我在[上次教程](https://www.cnblogs.com/kainhuck/p/10620031.html)中有傻瓜式的说明

一下为个人在自己笔记本电脑安装arch全过程

## 1. 联网

```
wifi-menu
```

*检查是否联通*

```
ping www.baidu.com
```

## 2. 更新系统时钟

```
timedatectl set-ntp true
```

## 3. 磁盘分区

用下面命令检查你要安装的磁盘

```
fdisk -l
```

这里假设安装到`/dev/sda`，然后用下面命令对磁盘分区（fdisk具体使用方法可参考[我的另一篇博客](https://www.cnblogs.com/kainhuck/p/10620031.html)里面有提到）

```
fdisk /dev/sda
```

这里我给出我的方案：

| 类形     | 磁盘大小 | 磁盘序号  |
| -------- | -------- | --------- |
| boot分区 | 500m     | /dev/sda1 |
| swap分区 | 6G       | /dev/sda2 |
| 根分区   | 其余     | /dev/sda3 |

home目录我是在系统安装好后进行的，你们也可以在这一步进行

## 4. 格式化分区

将boot分区格式化为 `ext2`

```
mkfs.ext2 /dev/sda1
```

将swap分区格式化为`swap`

```
mkswap /dev/sda2
```

打开swap分区

```
swapon /dev/sda2
```

将根目录/home目录格式化为`ext4`

```
mkfs.ext4 /dev/sda3
```

## 5. 挂载分区

### 1. 先将根分区挂载到`/mnt`目录

```
mount /dev/sda3 /mnt
```

#### 2. 再在`/mnt`目录下新建`boot`目录

```
mkdir /mnt/boot
```

### 3. 最后将boot分区挂载在刚刚创建的`/mnt/boot`目录

```
mount /dev/sda1 /mnt/boot
```

## 6. 开始安装系统

### 1. 先配置软件源（推荐选择清华源）

搜索`tuna`将其粘贴到文件第一行

```
vim /etc/pacman.d/mirrorlist
```

### 2. 刷新一下

```
pacman -Syy
```

### 3. 然后开始安装系统到`/dev/sda1`也就是挂载点`/mnt`

其中必须安装的有`base` `linux` `linux-firmware`，推介也把`base-devel`安装上

```
pacstrap /mnt base linux linux-firmware base-devel
```

### 4. 安装完成之后需生成`fstab`文件

```
genfstab -U /mnt >> /mnt/etc/fastab
```

## 7. 切换环境

### 1. 切换到刚刚安装好的系统

```
arch-chroot /mnt
```

### 2. 配置时区

```
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

### 3. 设置硬件时间

```
hwclock --systohc
```

### 4. 安装vim(我习惯了使用vim编辑)

```
pacman -S vim
```

### 5. 设置语言

#### 1. 将/etc/locale.gen中`en_US.UTF-8`和`zh_CN.UTF-8`的注释去掉

```
vim /etc/locale.gen
```

#### 2. 然后生成一下

```
locale-gen
```

#### 3. 配置 /etc/locale.conf文件

在 `/etc/locale.conf`文件中写入`LANG=en_US.UTF-8`

```
echo LANG=en_US.UTF-8 >> /etc/locale.conf
```

### 6. 设置root用户密码

```
passwd
```

### 7. 安装网络相关的包

```
pacman -S iw wpa_supplicant dialog net-tools networkmanager dhcpcd
```

设置网络工具开机自启

```
systemctl enable NetworkManager
systemctl enable dhcpcd
```

### 8. 按装cpu编码

如果是`intel`cpu

```
pacman -S intel-ucode
```

如果是`amd`cpu

```
pacman -S amd-ucode
```

### 9. 安装引导

注意第二条命令是你安装系统的盘符，如果你安装在`/dev/sdb`就填`/dev/sdb`

```
pacman -S grub
grub-install /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```

### 10. 给你的系统取个名字

```
echo yourname > /etc/hostname 
```

***到此系统就安装好了，先别急着退出，接下来开始安装桌面***

## 8. 开始按装kde-plasma

### 1. 安装Xorg

```
pacman -S xorg
```

### 2. 安装触摸板驱动

```
pacman -S xf86-input-synaptics
```

### 3. 安装字体

超级喜欢`dejavu`字体

```
pacman -S ttf-dejavu wqy-microhei
```

### 4. 创建用户

将新建用户移入`wheel`组并指定shell为`bash`(以后可修改)

kain 为我设置的用户，你们可以取别的名字

```
useradd -m -G wheel -s /bin/bash kain
```

为新用户设置密码

```
passwd kain
```

为新用户添加管理员权限（可以使用sudo命令）

将文件`/etc/sudoers`中的`wheel ALL=(ALL) ALL`那一行前面的注释去掉

```
vim /etc/sudoers
```

### 5. 开始安装桌面

### 1. 安装桌面及基本应用

其中`plasma`是必须的`kde-applications`是一些常用软件包括终端和文件管理器等，还有许多小游戏（为了方便推荐安装上）

```
pacman -S plasma kde-applications
```

### 2. 激活登录窗口`sddm`

sddm已经被包含进`plasma`中，无需另外安装

```
systemctl enable sddm
```

### 3. 安装声音

```
pacman -S alsa-utils pulseaudio pulseaudio-alsa
```

### 4. 其他

解决kde中部分应用无法使用全局菜单栏的问题，需安装下面的库

```
pacman -S libdbusmenu-glib
```



到这里arch已经完全安装结束了

## 9. 退出当前环境

```
exit
```

## 10. 卸载分区

```
umount -R /mnt
```

## 11. 重启

```
reboot
```

拔掉u盘

接下去就可以对安装好的arch做一些配置，和常用软件的的安装，我下次更新

