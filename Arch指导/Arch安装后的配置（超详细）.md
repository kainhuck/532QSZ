# Arch安装后的配置（超详细）

## 1. 添加`archlinuxcn`源

在 `/etc/pacman.conf` 文件末尾添加以下两行：

```
[archlinuxcn]
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch
```

然后安装 GPG key

```
sudo pacman -Syu
sudo pacman -S archlinuxcn-keyring
```

## 2. 配置aur

安装yay

```
sudo pacman -S yay
```

修改`aururl`

```
yay --aururl "https://aur.tuna.tsinghua.edu.cn" --save
```



## 3. 更换`shell`为`zsh`

```
chsh -s /bin/zsh
```

重启即可生效

## 4. 安装`oh-my-zsh`及插件

先确保git，wget, curl已经安装

```
sudo pacman -S git wget curl
```

安装ohmyzsh

```
sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
```

安装历史记录插件和语法检查插件

```
cd ~/.oh-my-zsh/plugins
git clone git://github.com/zsh-users/zsh-autosuggestions.git
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
```

下载好后在`～/.zshrc`文件中加入上述插件

找到`plugins=(git)`，改为如下（sudo插件无须下载，效果为连按两次`esc`键给命令加上`sudo`）

```
plugins=(
	git
	sudo
	zsh-syntax-highlighting
	zsh-autosuggestions
)
```

使插件生效

```
source ~/.zshrc
```



## 5. 安装输入法

安装fcitx

```
sudo pacman -S fcitx-im
sudo pacman -S fcitx-cofigtool
```

在家目录下创建`.xprofile`文件并写入以下内容

```
export XIM=fcitx
export XIM_PROGRAM=fcitx
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
```

然后安装喜欢的输入法，这里推荐实用讯飞输入法（搜狗输入法有bug可能用不了）

讯飞输入法需要去aur里安装

```
yay -S iflyime
```

重启查看`fcitx 配置`是否已经添加了讯飞输入法



## 6. 配置开发环境

### python

下载pip

```
sudo pacman -S python-pip
```

设置pip源

```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```



### golang

1. 安装go

   ```
   sudo pacman -S go
   ```

2. 选择一个go工作目录

   我这里以`～/Documents/go`为例

   在`～/Documents/go`下新建三个文件夹分别为`src`,`bin`,`pkg`

3. 配置环境变量（注意改为你自己的工作目录,`GOROOT=/usr/lib/go`和我一样，这是安装目录）

   编辑`～/.xprofile`

   ```
   export GOROOT=/usr/lib/go
   export GOPATH=~/Documents/go		# 这两行你需要 
   export GOBIN=~/Documents/go/bin		# 修改为自己的
   export PATH=$PATH:$GOROOT/bin:$GOBIN
   ```

   然后

   ```
   source .xprofile
   ```

4. 配置GOPROXY

   ```
   go env -w GOPROXY=https://goproxy.io,direct
   ```

   

### java

查看当前系统中已经存在的jdk有哪些

```
archlinux-java status
```

选中其中一个为默认jdk

```
sudo archlinux-java set `上面列表中列出的名字其中一个`
```

安装最新版jdk

```
sudo pacman -S jdk
```

安装jdk8

```
sudo pacman -S jdk8-openjdk
```



### nodejs

安装

```
sudo pacman -S nodejs npm
```

npm使用淘宝镜像

```
npm config set registry https://registry.npm.taobao.org
```

安装vue-cli

```
npm install -g @vue/cli
```



### docker

安装docker

```
sudo pacman -Syu docker
```

免sudo执行docker

```
sudo gpasswd -a ${USER} docker
```

配置docker国内镜像

在`/etc/docker`目录下新建`daemon.json`文件,写入下面内容(网易镜像)

```json
{
	"registry-mirrors": ["http://hub-mirror.c.163.com"]
}
```

重启docker生效

```
sudo systemctl restart docker
```



### mysql

1. 安装Maria DB

```
sudo pacman -S mariadb
```

2. 配置目录

```
sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
```

3. 启动Maria DB

```
sudo systemctl start mysqld
```

4. 为root用户设置一个新密码

```
sudo mysqladmin -u root password '123456'
```

至此已经可以进入数据库了，命令`mysql -u root -p`

5. root用用户开启远程访问

   先进入数据库

   1. 选中mysql数据库

    ```
    use mysql;
    ```

6. 更改root的访问权限

   可以先查看当前权限信息（不是必须）

     `select user,authentication_string,host from user;`

   123456 为你设置的root用户密码

   ```
    GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456';
   ```

   3. 刷新数据

    ```
    flush privileges;
    ```

7. 将mysql设为开机自启

```
  sudo systmctl enable mysql
```

### 其他环境

可以选择通过`docker`来安装

## 7. 安装常用软件

### 1. 聊天类

- qq(wine)

  ```
  yay -S deepin.com.qq.im
  ```

  或者qq(linux)，这个不推荐，太难用了(但是是官方的)

  ```
  sudo pacman -S qq-linux
  ```

  或者tim

  ```
  yay -S deepin.com.qq.office
  ```

  或者qq轻聊版

  ```
  yay -S deepin.com.qq.im.light
  ```

- 微信

  ```
  yay -S deepin.com.wechat2
  ```

- telegram

  ```
  sudo pacman -S telegram-desktop
  ```

- deepin qq和微信在`kde`桌面下可能遇到打不开的问题,解决方法如下

  安装如下程序

  ```
  sudo pacman -S gnome-settings-daemon
  ```

  执行以下操作

  ```
  sudo cp /etc/xdg/autostart/org.gnome.SettingsDaemon.XSettings.desktop ~/.config/autostart
  ```

  后打开设置，找到`开机和关机`中的`自动启动`，将`GNOME Settings Daemon's xsettings plugin`设置为已启用，注意要先点击右下角的`高级`按钮，在弹出框中选中`只在Plasma中自动启用`，确定即可

### 2. 办公类

- WPS

  ```
  sudo pacman -S wps-office ttf-wps-fonts
  ```

- typora

  ```
  sudo pacman -S typora
  ```

- mindmaster（亿图思维导图）

  ```
  yay -S yay mindmaster-cn
  ```



### 3. 开发类

- vscode

  ```
  sudo pacman -S code
  ```

- postman

  ```
  sudo pacman -S postman-bin
  ```

- eclipse（java）

  ```
  sudo pacman -S eclipse-java 
  ```

- pycharm

  专业版

  ```
  sudo pacman -S pycharm-professional
  ```

  社区版

  ```
  sudo pacman -S pycharm-community-edition 
  ```

- IDEA

  专业版

  ```
  sudo pacman -S intellij-idea-ultimate-edition
  ```

  社区版

  ```
  sudo pacman -S intellij-idea-community-edition
  ```

  

### 4. 娱乐类

- 网易云音乐

  官方版

  ```
  sudo pacman -S netease-cloud-music
  ```

  非dde桌面下可能遇到无法输入中文的问题，需要做以下修改

  1. 安装`qcef`

  ```
  $ yay -S qcef
  ```

  1. 修改`/opt/netease/netease-cloud-music/netease-cloud-music.bash`文件为以下内容

  ```
  #!/bin/sh
  HERE="$(dirname "$(readlink -f "${0}")")"
  export XDG_CURRENT_DESKTOP=DDE 
  exec "${HERE}"/netease-cloud-music $@
  ```

  民间大神版

  ```
  sudo pacman -S electron-netease-cloud-music
  ```

- qq音乐（wine）

  ```
  yay -S deepin.com.qq.qqmusic
  ```

  

### 5. 实用工具类

- 谷歌浏览器

  ```
  sudo pacman -S google-chrome
  ```

- 火狐浏览器

  ```
  sudo pacman -S firefox
  ```

- virtual box

  ```
  sudo pacman -S virtualbox
  ```

  选择`virtualbox-host-modules-arch`模块

  ```
  sudo pacman -S linux-headers
  ```

  将当前用户加入`vboxusers`组

  ```
  sudo gpasswd -a $USER vboxusers
  ```

  其他可选相关项

  注意如果遇到让你选择类型，记得选和第一步一样的类型

  ```
  sudo pacman -S virtualbox-guest-dkms
  sudo pacman -S virtualbox-guest-iso
  sudo pacman -S virtualbox-guest-utils
  yay -S virtualbox-ext-oracle
  ```

  重启

- 百度网盘

  ```
  sudo pacman -S baidunetdisk-bin
  ```

  

### 6. 不可描述类

- qv2ray

  ```
  sudo pacman -S qv2ray
  ```



## 8. 美化grub启动界面

1. 去商店下载主题包

   [gnome-look](https://www.gnome-look.org/)

   [kde-look](https://store.kde.org/)

   访问有点慢。。。

2. 解压下载好的主题

   ```
   sudo tar -xf 主题包名
   ```

3. 复制到grub主题目录

   ```
   sudo cp -r 主题包名 /boot/grub/themes/  
   ```

4. 修改文件添加主题

   ```
   sudo vim /etc/default/grub
   ```

   找到`#GRUB_THEME=`去掉注释，该为对应的主题名称，就像这样

   ```
   GRUB_THEME="/usr/share/grub/themes/主题包名/theme.txt"
   ```

  
