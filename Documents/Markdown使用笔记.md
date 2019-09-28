# Markdown使用笔记

## 介绍

*Markdown*是一种标记语言,通过Markdown可以排版我们的文章使其更加具有逻辑性,看着更美观.我们在GitHub中经常看见一个名为README.md就是一个Markdown文件.Markdown使用方便 ,学习简单,学会使用Markdown可以大大提高我们的办公效率.

-------------------

## 常用语法

| 语法名称 | 格式                       | 快捷键   |
| -------- | -------------------------- | -------- |
| 斜体     | \*内容*                    | Ctrl + I |
| 加粗     | \**内容**                  | Ctrl + B |
| 链接     | \[name](http://)           | Ctrl + K |
| 分割线   | \--- (注: **-** 不少于3个) |          |
| 脚注     | a\[^2]    效果:  a[^2]     |          |
| 转义     | \\                         |          |



-------------



## 其他语法



## 1.标题

共六级标题,从大到小排序为

- #

- ##

- ###

- ####

- #####

- ######

  注: **#** 和标题文本之间隔一个空格

  如: \### 这是一三级个标题

  效果: 

  ### 这是一三级个标题

  

## 2.内嵌代码

### 使用两个 **`** 来嵌入一行代码

> 如: \` import requests `
>
> 效果: ` import requests`

### 使用两个 **```** 来嵌入一块代码

>**例子**
>
>\```
>
>#!/usr/bin/python3
>
>\#-\*- coding: utf-8 -*-
>
>import requests
>url = "https://www.baidu.com"
>r = requests.get(url)
>status = r.status_code
>if status == 200:
>    r.encoding = r.apparent_encoding
>    print(r.text)
>else:
>    print("Error")
>
>\```

>**效果**
>
>```python
>#!/usr/bin/python3
># -*- coding: utf-8 -*-
>import requests
>url = "https://www.baidu.com"
>r = requests.get(url)
>status = r.status_code
>if status == 200:
>    r.encoding = r.apparent_encoding
>    print(r.text)
>else:
>    print("Error")
>```



## 3.引用

### 格式: \> 引用内容

> 引用内容

### 也可以使用多层嵌套,格式为:

\> 一级 

\>> 二级

\>>> 三级

### 效果:

> 一级
>
> > 二级
> >
> > > 三级



## 4.表格插入

### 格式为:

\| 标题一 | 标题二 | 标题三 |

\| --------- | --------- | --------- |

\| 内容一 | 内容二 | 内容三 |

\| 内容四 | 内容五 | 内容六 |

### 效果

| 标题一 | 标题二 | 标题三 |
| ------ | ------ | ------ |
| 内容一 | 内容二 | 内容三 |
| 内容四 | 内容五 | 内容六 |



## 5.列表

### 无序列表

**格式**

*****  或 **\-**  ;注意和后面文字的空格

#### 例子

> \* test text
>
> \* text text
>
> \- hello markdown

#### 效果

> * test text
> * text text
> * hello markdown



### 有序列表

**格式**

第一句以阿拉伯数字加上 '**.** ' 号组成

#### 例子

>1\. hello Markdown
>
>2\. hello Mark
>
>3\. hello Down

#### 效果

>1. hello Markdown
>2. hello Mark
>3. hello Down



## 6.图片嵌入

### 格式

> !\[这里是图片未加载成功时显示的文字](这里是图片的链接)

*注意和链接比较(前面多了一个 **!** )*

### 例子

> 以博客园的logo为例
>
> !\[图片加载失败](https://www.cnblogs.com//images/logo_small.gif)		
>
> 后面也可以是本地的图片地址(这是一张[deepin](https://www.deepin.org/)系统的默认壁纸,但是网页上会显示失败)
>
> !\[图片加载失败](/home/kain/Pictures/desktop.jpg)
>
> > 效果如下
> >
> > ![图片加载失败](https://www.cnblogs.com//images/logo_small.gif)
> >
> > ![图片加载失败](/home/kain/Pictures/desktop.jpg)



## 注:

### 1. 我这里只是简单的罗列了一些*Markdown*的常用用法,并不全面

### 2. 大家可以选择合适的*Markdown*编辑器来加快排版的效率(推荐使用Typora)

