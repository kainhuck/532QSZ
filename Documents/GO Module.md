# GO Module

## 1. 是什么

Go Module是Go1.11后加入的新功能，用于管理GO语言的包，类是与python的pip

## 2. 与go get的区别

go get下载的包源码存放在 `$GOPATH/src`目录中

Go Module下载的包源代码存放在 `$GOPATH/pkg/mod`文件夹中，并且带有版本号

## 3. GO MODULE附带功能goproxy

下载镜像

## 4. 使用GO MODULE

将`GO111MODULE`环境变量设置为`on`,如果你无法直接访问外网，推荐设置上`GOPROXY="https://goproxy.io,direct"`

使用命令`go env`查看有关go的环境变量



```
设置GO111MODULE=on后强制所有命令使用GO Module功能，如果要恢复删掉环境变量或者设置为auto,建议Go工程都使用Module并开启该特性
```

## 5. 创建go工程

进入工程目录（可以在任意地点）

输入`go mod init 模块名`，该命令会自动创建`go.mod`文件

模块名：一般可以`github.com/username/project_name`

## 6. go.mod文件

管理包的说明文件，常用指令如下：

1. module: 模块名称
2. require: 依赖包列表以及版本
3. exclude: 禁止依赖包列表（仅在当前模块为主模块时生效）
4. replace: 替换依赖包列表（仅在当前模块为主模块时生效）

上述命令一般IDE会自动生成，不需要手写

项目中引用一个未下载的第三方库，go module会自动去下载

## 7. go.sum文件

可以认为是临时文件，一般加入.gitignore列表

## 8. go mod其他命令

0. init               // 初始化go.mod文件

1. download 	// 下载模块到本地缓存

   ​					// 可以通过命令 go clean -cache 清除文件

2. edit              // 从工具或脚本中编辑go.mod文件

3. graph           // 打印需求模块图

4. tidy              // 添加缺失的模块以及移除无用的模块

5. verify           // 验证依赖项是否达到预期的目的

6. why             // 解释为什么需要包或模块

#### 基础使用

- 用`go get`拉取新的依赖
  - 拉取最新的版本(优先择取 tag)：`go get golang.org/x/text@latest`
  - 拉取 `master` 分支的最新 commit：`go get golang.org/x/text@master`
  - 拉取 tag 为 v0.3.2 的 commit：`go get golang.org/x/text@v0.3.2`
  - 拉取 hash 为 342b231 的 commit，最终会被转换为 v0.3.2：`go get golang.org/x/text@342b2e`
  - 用 `go get -u` 更新现有的依赖
  - 用 `go mod download` 下载 go.mod 文件中指明的所有依赖
  - 用 `go mod tidy` 整理现有的依赖
  - 用 `go mod graph` 查看现有的依赖结构
  - 用 `go mod init` 生成 go.mod 文件 (Go 1.13 中唯一一个可以生成 go.mod 文件的子命令)
- 用 `go mod edit` 编辑 go.mod 文件
- 用 `go mod vendor` 导出现有的所有依赖 (事实上 Go modules 正在淡化 Vendor 的概念)
- 用 `go mod verify` 校验一个模块是否被篡改过