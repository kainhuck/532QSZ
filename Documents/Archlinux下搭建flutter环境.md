# Archlinux下搭建flutter环境

说多了都是泪

## 1. 安装JDK

**注意一定一定要安装jdk8!!!**

**注意一定一定要安装jdk8!!!**

**注意一定一定要安装jdk8!!!**

```
sudo pacman -S jdk8-openjdk
```

如果安装了多个jdk使用以下命令切换

```
sudo archlinux-java set java-8-openjdk
```



## 2. 安装Dart

这一步是否是必须的我也不太确定，但是装上没坏处

```
sudo pacman -S dart
```



## 3. 安装flutter SDK

### 1. 下载地址

地址 https://mirrors.tuna.tsinghua.edu.cn/flutter/flutter_infra/releases/stable/linux/flutter_linux_v1.12.13%2Bhotfix.8-stable.tar.xz

### 2. 将其解压到home下的目录（为了防止出现权限问题）

我使用的目录是`～/Documents/development`

```
cd ～/Documents/development
tar xvf flutter_linux_v1.12.13+hotfix.8-stable.tar.xz
```

### 3. 配置环境变量

在`.xprofile`中写入如下内容，注意修改为你自己的路径

```
export PUB_HOSTED_URL=https://pub.flutter-io.cn
export FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn
export PATH=/home/kain/Documents/development/flutter/bin:$PATH
```

然后

```
source .xprofile
```

或者重启

## 4. 安装android SDK

```
sudo pacman -S android-sdk android-sdk-build-tools android-sdk-platform-tools android-platform gradle
```

**配置android环境变量**

在.xprofile中写入

```
export ANDROID_HOME='/opt/android-sdk'
export PATH=$ANDROID_HOME/tools:$PATH
export PATH=$ANDROID_HOME/platform-tools:$PATH
```

赋予android-sdk目录权限

```
sudo chomd -R 777 /opt/android-sdk
```

然后

```
source .xprofile
```

或者重启

## 5. 安装android-studio

