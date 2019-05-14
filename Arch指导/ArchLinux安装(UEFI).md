

# ArchLinux安装(UEFI)

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
>
> 更改root账户密码(这还不是系统的root)
>
> ```
> # passwd
> ```
>
> 在另外的电脑上连接
>
> ```
> # ssh root@[ip地址]
> 例如:
> ssh root@192.168.1.1
> ```

## 二.更新系统时钟

ArchLinux安装(UEFI)1.设置

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
# parted /dev/sda
-->mktable -->gpt -->quit

如:
root@archiso ~ # parted /dev/sda 
GNU Parted 3.2
Using /dev/sda
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) mktable                                                          
New disk label type? gpt
(parted) quit                                                             
Information: You may need to update /etc/fstab.

root@archiso ~ # 
```

EFI 给 500M

swap 给 6G (一般为内存的两倍,如果你的内存够大可少给,如6G)

根目录和家目录分剩下的

cfdisk用法不清楚的可百度(这里不在介绍)

```
# cfdisk /dev/sda
```



### 3.格式化分区

将EFI分区格式化为vfat

根目录和家目录格式化为ext4

*请注意自己的对应的目录是那块区域*

可用`fdisk -l`查看分区情况

```
# mkfs.vfat /dev/sda1
# mkfs.ext4 /dev/sda3
# mkfs.ext4 /dev/sda4
# mkswap -f /dev/sda2
```

### 4.打开swap分区

*请注意自己的swap分区是哪块*

```
# swapon /dev/sda2
```

### 5.挂载分区

先挂载根目录

```
# mount /dev/sda3 /mnt 
# mkdir /mnt/home
# mount /dev/sda4 /mnt/home
# mkdir /mnt/boot
# mkdir /mnt/boot/EFI
# mount /dev/sda1 /mnt/boot/EFI
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
# pacman -S grub efibootmgr
# grub-install --target=x86_64-efi --efi-directory=/boot/EFI --bootloader-id=grub
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

