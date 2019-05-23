# Python3学习教程

## 〇.说在前头

### 0.这是Python3的自编教程

> 下文中的Python默认代表Python3
>
> Python2到2020年停止维护,推荐大家学习Python3

### 1.下载Python

> Windows
>
> https://www.python.org/downloads/windows/
>
> Linux/macOS
>
> 一般系统自带,可用对应的包管理工具进行下载

### 2.Python的语法

> 不同于类C语言,Python使用冒号":"加缩进(四个空格或一个Tab,不能混用)划分代码块,而不是括号加花括号

### 3.Python中的注释

>Python使用  # 进行单行注释,使用三个单引号或双引号进行多行注释
>
>```Python
>a = 0 # 这里是注释
>
>'''
>这里
>都是
>注释
>'''
>```
>
>

## 一.基础知识

### 0.变量

> Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
>
> 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
>
> 变量赋值(示例)
>
> ```python
> a = 0
> a = b = 0
> a, b = 0, 1
> ```

### 1.数字数据类型

>int、float、bool、complex（复数）
>
>常用操作符
>
>```
>+  
>- 
>*  
>/(普通除法,带小数)  
>%(取余)  
>**(幂运算)   
>//(地板除,不带小数)
>--------------------------------------------------------
><
><=
>>
>>=
>==
>!=
>-------------------------------------------------------
>and
>or
>not
>```
>
>类型转换
>
>```
>类型名(变量名)
>```
>
>一些函数
>
>```
>type(变量名)	查看变量类型
>isinstance(变量名, 类型名)	判断变量是否为该类型
>random模块
>```

### 2.列表,元组和字符串类型

> 列表(list):
>
> ```
> Python中使用一对方括号表示列表类型,
> 列表中可以存放任意数量的任何类型元素,
> ```
>
> 创建一个列表:
>
> ```python
> a = []
> a = list()	# 通过list()函数创立
> a = [1, 3]	# 创建一个非空的列表
> ```
>
> 列表的操作函数
>
> ```Python
> append(a)	# 末尾添加一个元素
> extend(b)	# 末尾添加多个元素,b必须是一个列表
> insert(index, a)	# 向指定位置添加一个元素
> 
> listName[index]		# 通过索引值获取列表中元素
> 
> remove(a)	# 从列表中删除a元素
> pop()	# 可带参(弹出指定位置元素)也可不带参(弹出末尾元素)
> 
> index(a, start, stop)	# 在区间内查找a元素的位置,后两个参数省略则在全不区间查找
> reverse()	# 翻转列表
> sort(reverse=False)	# 默认从小到大排序
> count(a)	# 统计a出现的次数
> ```
>
> ```Python
> len(list)	# 取长度
> max(list)	# 取最大值
> min(list) 	# 取最小值
> sum(list)	# 取和
> sorted(list)
> reversed(list)
> zip()
> ```
>
> 列表切片
>
> ```Python
> # 使用:进行列表切片
> listName[start:end:step]
> # start : 开始位置,默认为0
> # end : 结束位置,默认为最后
> # step : 步长,默认为1,不常用
> # 注意,列表切片为左闭右开(除非end为空),列表切片不改变原来的列表
> ```
>
> 列表拼接
>
> ```
> 使用加号拼接
> ```
>
> -----------------------------------------------------------------------------
>
> 元组(tuple):
>
> ```
> 同列表
> ```
>
> 字符串(str):
>
> ```
> python 中没有字符,一对单引号或者双引号代表字符串
> ```
>
> ```
>同列表
> ```
> 
> 此外,字符串还有的常用操作
>
> ```
>"*".join(string)	# 拼接
> string.split(sep = "")  # 拆分
> string.format()		# 格式化  "{0}, {1}".format("hello", "world") 或则使用
> ```

### 3.字典和集合类型

> dict()
>
> ```
> 字典创建
> 字典访问
> 字典修改
> 字典迭代,添加
> 
> 一些函数: keys()  values()  items()  get()
> ```
>
> 
>
> set()
>
> ```
> 集合的特点: 唯一性
> 创建
> 迭代
> 一些函数: add()  remove()
> ```
>
> 

### 4.分支循环

> for
>
> while
>
> break
>
> continue
>
> **range()函数**

> if  else  elif
>
> 断言:  assert  后面为假时抛出异常
>
> 

### 5.函数

> def 申明函数
>
> 函数参数
>
> 函数返回值
>
> pass关键字
>
> 函数文档
>
> **help()函数**
>
> 变量作用域   global关键字
>
> 递归

### 6.类和对象

> class创建类
>
> 属性和方法
>
> **self**关键字
>
> **\__init__** 函数
>
> 公有和私有
>
> 继承
>
> super函数
>
> 多重继承

### 7.文件操作

> open函数
>
> 打开问价的两种方法
>
> readline()函数
>
> read()函数
>
> 迭代文件对象,
>
> write()函数

### 8.异常处理

> try   except   finally
>
> 捕获多个异常
>
> raise语句
>
> 自定义异常

### 9.模块

> 包的概念
>
> 安装一个第三方库
>
> import 导入一个模块
>
> 自定义一个模块
>
> \__init__.py文件
>
> \__name__ == "\__main__"

## 二.Python进阶

## 三.数据库操作

## 四.多线程

## 五.爬虫

### 0.准备工作

***安装所需的第三方库***

`pip install requests`

`pip install bs4`

`pip install lxml`

***URL的理解***

> URL全名为统一资源定位符
>
> 也就是常说的网址

***选择一款合适的浏览器***

> 这里推荐谷歌浏览器和火狐浏览器
>
> 掌握浏览器开发者工具的简单操作

***爬虫一般分为三大步骤***

1. 请求网址
2. 解析网址
3. 保存数据

### 1.请求网址

***利用requests模块对网页发起请求***

***常用方法有***

1. requests.get(url, params=None, **kwargs)	# 用get方法发送请求
2. requests.post(url, data=None, json=None, **kwargs)    # 用post方法发送请求
3. 其他不常用的方法有options,head,put,patch,delete

***简单的例子****

```Python
import requests

r = requests.get("https://www.baidu.com")	# 对百度发起get请求

print(r.status_code)	# 打印状态码
```

***携带请求参数***

```python
import requests

url = "http://www.csgmooc.com/spocv3api//user/login"

data = {
    "number": "20173312000**",
    "password": "20173312000**",
    "schoolNum": "1MzrWz0lTc**"
}

r = requests.post(url, data=data)	# 参数以字典的格式传给data形参

print(r.text)
```

### 2.解析网页

***常用的类库为lxml, BeautifulSoup, re(正则)***

以获取豆瓣电影正在热映的电影名为例,url='https://movie.douban.com/cinema/nowplaying/beijing/'

***网页分析***

***部分网页源码***

```html
<ul class="lists">
                    <li
                        id="3878007"
                        class="list-item"
                        data-title="海王"
                        data-score="8.2"
                        data-star="40"
                        data-release="2018"
                        data-duration="143分钟"
                        data-region="美国 澳大利亚"
                        data-director="温子仁"
                        data-actors="杰森·莫玛 / 艾梅柏·希尔德 / 威廉·达福"
                        data-category="nowplaying"
                        data-enough="True"
                        data-showed="True"
                        data-votecount="105013"
                        data-subject="3878007"
                    >
                        
```

分析可知我们要的电影名称信息在li标签的data-title属性里

下面开始写代码

***爬虫源码展示***

```python
import requests
from lxml import etree              # 导入库
from bs4 import BeautifulSoup
import re

import time

# 定义爬虫类
class Spider():
    def __init__(self):
        self.url = 'https://movie.douban.com/cinema/nowplaying/beijing/'

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        r = requests.get(self.url,headers=self.headers)
        r.encoding = r.apparent_encoding
        self.html = r.text

    def lxml_find(self):
        '''用lxml解析'''
        start = time.time()						# 三种方式速度对比
        selector = etree.HTML(self.html)        # 转换为lxml解析的对象
        titles = selector.xpath('//li[@class="list-item"]/@data-title')    # 这里返回的是一个列表
        for each in titles:
            title = each.strip()        # 去掉字符左右的空格
            print(title)
        end = time.time()
        print('lxml耗时', end-start)

    def BeautifulSoup_find(self):
        '''用BeautifulSoup解析'''
        start = time.time()
        soup = BeautifulSoup(self.html, 'lxml')   # 转换为BeautifulSoup的解析对象()里第二个参数为解析方式
        titles = soup.find_all('li', class_='list-item')
        for each in titles:
            title = each['data-title']
            print(title)
        end = time.time()
        print('BeautifulSoup耗时', end-start)

    def re_find(self):
        '''用re解析'''
        start = time.time()
        titles = re.findall('data-title="(.+)"',self.html)
        for each in titles:
            print(each)
        end = time.time()
        print('re耗时', end-start)

if __name__ == '__main__':
    spider = Spider()
    spider.lxml_find()
    spider.BeautifulSoup_find()
    spider.re_find()
```

***输出结果***

```
海王
无名之辈
无敌破坏王2：大闹互联网
狗十三
惊涛飓浪
毒液：致命守护者
憨豆特工3
神奇动物：格林德沃之罪
恐龙王
老爸102岁
生活万岁
进击的男孩
摘金奇缘
亡命救赎
一百年很长吗
云上日出
谁是坏孩子
照相师
缘·梦
网络谜踪
龙猫
印度合伙人
绿毛怪格林奇
最萌警探
春天的马拉松
lxml耗时 0.007623910903930664
海王
无名之辈
无敌破坏王2：大闹互联网
狗十三
惊涛飓浪
毒液：致命守护者
憨豆特工3
神奇动物：格林德沃之罪
恐龙王
老爸102岁
生活万岁
进击的男孩
摘金奇缘
亡命救赎
一百年很长吗
超时空大冒险
天渠
爱不可及
二十岁
你好，之华
冒牌搭档
铁甲战神
克隆人
恐怖快递
中国蓝盔
阿凡提之奇缘历险
名侦探柯南：零的执行人
为迈克尔·杰克逊铸造雕像
再见仍是朋友
心迷宫
淡蓝琥珀
阿拉姜色
两个俏公主
云上日出
谁是坏孩子
照相师
缘·梦
网络谜踪
龙猫
印度合伙人
绿毛怪格林奇
最萌警探
春天的马拉松
BeautifulSoup耗时 0.061043500900268555
海王
无名之辈
无敌破坏王2：大闹互联网
狗十三
惊涛飓浪
毒液：致命守护者
憨豆特工3
神奇动物：格林德沃之罪
恐龙王
老爸102岁
生活万岁
进击的男孩
摘金奇缘
亡命救赎
一百年很长吗
超时空大冒险
天渠
爱不可及
二十岁
你好，之华
冒牌搭档
铁甲战神
克隆人
恐怖快递
中国蓝盔
阿凡提之奇缘历险
名侦探柯南：零的执行人
为迈克尔·杰克逊铸造雕像
再见仍是朋友
心迷宫
淡蓝琥珀
阿拉姜色
两个俏公主
云上日出
谁是坏孩子
照相师
缘·梦
网络谜踪
龙猫
印度合伙人
绿毛怪格林奇
最萌警探
春天的马拉松
re耗时 0.0004856586456298828
```

***代码说明***

> ### 1. lxml
>
> > lxml是通过xpath来查找
> >
> > 使用前需使用调用ertee.HTML()方法('()'内填HTML代码)生成一个可查找的对象
> >
> > 常用xpath语法如下
> >
> > **//**  两个斜杠为向下查找孙子标签
> >
> > **/**   一个斜杠为查找直接儿子标签
> >
> > **[]**  方括号内填标签属性,如查找class属性为name的a标签,格式为a[@class="name"]
> >
> > **/text()**    取出标签的内容,如查找网页中的 \<a class="name">KAINHUCK\</a> 中的KAINHUCK,格式为*//a[@class="name"]/text()*
> >
> > **/@attr**    取出标签的属性,如查找网页中的 \<a class="name">KAINHUCK\</a> 中的class属性值name,格式为*//a[@class="name"]/@class*
>
> ### 2. BeautifulSoup
>
> >使用前需先将HTML转换为课查找对象,格式为
> >
> >BeautifulSoup(html, 'lxml')  
> >
> >html 为HTML代码, 后面的参数为转换方法(其他方法有*'html.parser'* , *'html5lib'*, 推荐使用*'lxml'*)
> >
> >查找方法
> >
> >**info =** **find('a', id='kain')**   查找第一个id属性为kain的a标签,并存进info变量中(其他标签同理)
> >
> >**find_all('a', class_='name')**  查找所有class属性为name的a标签(注:*class*属性需写成*'class_'*)
> >
> >**info.p.text**  获取第一个id属性为kain的a标签下的p标签的内容(info为上面例子里的info,其他同理)
> >
> >**info.p['name']**  获取第一个id属性为kain的a标签下的p标签的name属性值(info为上面例子里的info,其他同理)
> >
> >**当代码中有很多同级标签时**
> >
> >```html
> ><p class='info-list'>
> >   <a class='name'>text1</a>
> >   <a class='name'>text2</a>
> >   <a class='name'>text3</a>
> >   <a class='name'>text4</a>
> ></p>
> >```
> >
> >示例代码如下
> >
> >```python
> >from bs4 import BeautifulSoup
> >
> >html = '''
> ><p class='info-list'>
> >   <a class='name'>text1</a>
> >   <a class='name'>text2</a>
> >   <a class='name'>text3</a>
> >   <a class='name'>text4</a>
> ></p>
> >'''
> >soup = BeautifulSoup(html, 'lxml')
> >texts = soup.find('p', class_='info-list')
> >print(texts.contents[1].text)	# 输出text1
> >print(texts.contents[2].text)	# 输出text2
> >print(texts.contents[3].text)	# 输出text3
> >print(texts.contents[4].text)	# 输出text4
> >```
> >
> >*注意:不是从0开始*
>
> ### 3. re(正则表达式)
>
> > 正则表达式内容较多,大家可以参考[这里](http://www.runoob.com/python3/python3-reg-expressions.html)

***总结***

使用lxml查找时可以在目标网页按F12调出开发者窗口然后再在按Ctrl+f查找,在查找栏里输入你的xpath语法可以检查是否能找到对应内容

可以从看例子的输出中看出三种方法的速度

> lxml耗时 0.007623910903930664
>
> BeautifulSoup耗时 0.061043500900268555
>
> re耗时 0.0004856586456298828

***对以上三种最常用的解析网页的方法做个对比***

|            | lxml | BeautifulSoup | re   |
| ---------- | ---- | ------------- | ---- |
| 语法难易度 | 简单 | 简单          | 复杂 |
| 查找速度   | 较快 | 慢            | 快   |

综上,对于网页内容的解析,这里推荐新手使用lxml方法,而对速度有要求就使用正则表达式(入门有点困难)

### 3.存储数据

### 4.反反爬虫

### 5.提升爬虫的速度

### 6.爬取动态网站

### 7.爬虫框架



## 六.网络编程

## 七.网站后端(Tornado)

