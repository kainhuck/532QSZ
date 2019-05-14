

# ArchLinux安装(BIOS)

## 一.连接网络

### 1.连接

```
# wifi-menu
```

### 2.检查是否联通

(ctrl+c停止)

```
# ping www.baidu.com
```

### 3.远程安装

*注:连接上网络之后可以通过远程链接(同一个网络下)在另一台电脑上进行安装操作(可方便复制代码),如不想这么做请忽略这一步骤*

> 开启ssh
>
> ```
> # systemctl start ssh
> ```
>
> 查看ip地址
>
> ```
> # ip a
> ```
> 更改root账户密码(这还不是系统的root)
>
>
> ```
> # passwd
> ```
> 在另外的电脑上连接
> ```
> # ssh root@[ip地址]
> 例如:
> ssh root@192.168.1.1
> ```

## 二.更新系统时钟

### 1.设置

```
# timedatectl set-ntp true
```

### 2.检查

```
# timedatectl status
```



## 三.磁盘分区

### 1.查看当前的可用磁盘

一般都是 /dev/sda

```
# fdisk -l
```

### 2.创建新分区

```
# fdisk /dev/sda
-->n -->回车 -->回车 -->回车 -->+500m 
-->n -->回车 -->回车 -->回车 -->+6G
-->n -->回车 -->回车 -->回车 -->回车 
-->w

如:
root@archiso ~ # fdisk /dev/sda    

Welcome to fdisk (util-linux 2.33).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table.
Created a new DOS disklabel with disk identifier 0x1d29b8d3.

Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p): 
Partition number (1-4, default 1): 
First sector (2048-41943039, default 2048): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-41943039, default 41943039): +500m
 
Created a new partition 1 of type 'Linux' and of size 500 MiB.

Command (m for help): n
Partition type
   p   primary (1 primary, 0 extended, 3 free)
   e   extended (container for logical partitions)
Select (default p): 

Using default response p.
Partition number (2-4, default 2): 
First sector (1026048-41943039, default 1026048): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (1026048-41943039, default 41943039): +6G

Created a new partition 2 of type 'Linux' and of size 6 GiB.

Command (m for help): n
Partition type
   p   primary (2 primary, 0 extended, 2 free)
   e   extended (container for logical partitions)
Select (default p): 

Using default response p.
Partition number (3,4, default 3): 
First sector (13608960-41943039, default 13608960): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (13608960-41943039, default 41943039): 

Created a new partition 3 of type 'Linux' and of size 13.5 GiB.

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.

root@archiso ~ # 
```

```
# partprob
```



### 3.格式化分区

将bios分区格式化为ext2

根目录格式化为ext4

*请注意自己的对应的目录是那块区域*

```
# mkfs.ext2 /dev/sda1
# mkswap /dev/sda2
# mkfs.ext4 /dev/sda3
```

### 4.打开swap分区

请注意自己的swap分区是哪块

```
# swapon /dev/sda2
```

### 5.挂载分区

```
# mount /dev/sda3 /mnt 
# mkdir /mnt/boot
# mount /dev/sda1 /mnt/boot
```

## 四.安装系统基本包

### 1.配置源

将国内源放到第一位

```
# vim /etc/pacman.d/mirrorlist
```

### 2.刷新源

```
# pacman -Syy
```

### 3.安装基本包

```
# pacstrap /mnt base base-devel
```

### 4.生成fstab文件

```
# genfstab -U /mnt >> /mnt/etc/fstab
```



## 四.切换环境

### 1.切换

```
# arch-chroot /mnt
```

### 2.配置时区

```
# ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

### 3.硬件时间

```
# hwclock --systohc
```

### 4.安装vim

方便操作

```
# pacman -S vim
```

### 6.设置语言

将/etc/locale.gen中en_US.UTF-8的注释去掉

避免中文乱码,推荐先使用英文

```
# vim /etc/locale.gen
# locale-gen
```

### 7.配置 /etc/locale.conf文件

```
# vim /etc/locale.conf

写入
LANG=en_US.UTF-8
```

### 8.重置root密码

```
# passwd
```

### 9.安装网络相关的包

```
# pacman -S iw wpa_supplicant dialog
```

### 10.安装编码

```
# pacman -S intel-ucode
```

### 11.安装引导

```
# pacman -S grub
# grub-install /dev/sda
# grub-mkconfig -o /boot/grub/grub.cfg
```



## 五.退出当前环境

```
# exit
```



## 六.卸载新分区

```
# umount -R /mnt
```



## 七.重启

```
# reboot
```



到此安装完成

## 八.可能遇到的问题

### 1.网络链接不上

具体表现为ping不同百度

*解决办法:*

```
# systemctl enable dhcpcd
# systemctl restart dhcpcd
```

