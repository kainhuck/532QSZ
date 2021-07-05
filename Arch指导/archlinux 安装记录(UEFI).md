## archlinux 安装记录(UEFI)

### 1. 更新系统时间

```
timedatectl set-ntp true
```

### 2. 磁盘分区

分区表 gpt

| 类型       | 大小 | 挂载点        | 格式化    |
| ---------- | ---- | ------------- | --------- |
| EFI        | 1G   | /mnt/boot/EFI | mkfs.vfat |
| swap       | 4G   | -             | mkswap    |
| filesystem | 剩余 | /mnt          | mkfs.ext4 |

挂载分区并打开swap分区

### 3. 安装系统及必要软件

```
pacstrap /mnt base base-devel linux linux-firmware vim openssh dhcpcd networkmanager grub efibootmgr intel-ucode xf86-input-synaptics ttf-dejavu wqy-microhei fish alsa-utils pulseaudio pulseaudio-alsa xorg gdm gnome gnome-extra git wget curl
```

### 4. 生成fstab

```
genfstab -U /mnt >> /mnt/etc/fstab
```

### 5. chroot

```
arch-chroot /mnt
```

### 6. 设置时区

```
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

```
hwclock --systohc
```

### 7. 本地化

```
vim /etc/locale.gen
```

```
locale-gen
```

```
echo "LANG=zh_CN.UTF-8" > /etc/locale.conf
```

### 8. Host

```
echo "arch" > /etc/hostname
```

```
/etc/hosts
--------------------
127.0.0.1	localhost
::1		localhost
```

### 9. 设置各种软件开机自启

```
systemctl enable dhcpcd
systemctl enable NetworkManager
systemctl enable gdm
systemctl enable sshd
```

### 10. 密码&用户

设置root密码

```
passwd
```

新建普通用户

```
useradd -m -G wheel -s /bin/fish kain
```

新用户密码

```
passwd kain
```

新用户权限

```
vim /etc/sudoers
```

### 11. grub

```
grub-install --target=x86_64-efi --efi-directory=/boot/EFI --bootloader-id=GRUB
```

```
grub-mkconfig -o /boot/grub/grub.cfg
```

### 12. 结束

```
exit
```

```
umount -R /mnt
```

```
poweroff
```



