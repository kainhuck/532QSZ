# Arch常见问题及解决方案

## 1.网络链接不上

具体表现为ping不同百度

*解决办法:*

```
# systemctl enable dhcpcd
# systemctl restart dhcpcd
```



## 2.无法开启ssh

解决方法:

```
# pacman -S openssh
# systemctl enable sshd
# systemctl start sshd
```



## 3.字体问题

```
# yay lib32-freetype2-infinality-ultimate
# fc-cache -vf
```



## 4.没有ifcofig命令

```
# pacman -S net-tools
```



## 5.KDE桌面无法打开wine应用

```
# pacman -S gnome-settings-daemon

/etc/xdg/autostart --> org.gnome.settingsdaemon.xsettings.desktop 复制到 ~/.config/autostart

设置->开机和关机->自动启动
```



## 6.QQ/TIM/WeChat图标显示为wine图标

```
# xprop WM_CLASS
点击对应的窗口
更改desktop文件里的StartupWMClass属性
```

