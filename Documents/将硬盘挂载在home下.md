## 将硬盘挂载在/home下

### 1. 分区

```
# fdisk /dev/sdb
# partprobe
```

### 2. 格式化

```
# mkfs.ext4 /dev/sdb1
```

### 3. 挂载

```
# mkdir /mnt/home
# mount /dev/sdb1 /mnt/home
# cp -a /home/* /mnt/home
# rm -rf /home/*
# umount /dev/sdb1
```

### 4. 开机自动挂载

```
# vim /etc/fstab
加入
/dev/sdb1    /home    ext4    defaults   1 2
```



### 5.

````
# mount -a
# df -h:
````

