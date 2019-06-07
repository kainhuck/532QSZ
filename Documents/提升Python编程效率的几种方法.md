## 前言

我们知道Python这门语言在运行速度上已经败给了许多别的语言(比如C, C++, Java, Golang....).但从一个开发者的角度来看Python是我最喜欢的语言,很大一部分原因在于其语法简单(其实是我比较懒),还有很多很sao的操作,可以大大提高我们的敲代码的效率.我们通常叫这种sao操作为`pythonic`.

Python的sao操作很多,这里先介绍几种,以后慢慢更.



## 1.交换两个变量

传统写法:

```python
temp = a
a = b
b = temp
```

pythonic:

```Python
a, b = b, a
```

## 2.枚举enument

设想一个场景,有一个列表`["老胡", "老王", "老李", "老赵"]`,现在要求你创建一个字典,其中字典的每一项key为列表的元素,value为对应元素的下标,该怎么做?这并不是枚举的最佳使用场景,这里只是一个例子,告诉你们枚举其实很好用.

传统写法:

```python 
alist = ["老胡", "老王", "老李", "老赵"]

aDict = {}

for i in range(len(alist)):
    aDict[alist[i]] = i
```

pythonic:

```python 
alist = ["老胡", "老王", "老李", "老赵"]

aDict = {}

for index, item in enumerate(alist):
    aDict[item] = index
```

## 3.推导式

Python中的推导式分为三种`列表推导式`,`字典推导式`,`集合推导式`,由于集合推导式和列表推导式神似这里就不在过多演示.

### 列表推导式

设想一个场景,要求你把1-100间的所有偶数放到列表evenList中

传统写法:

```Python
evenList = []

for i in range(0, 101):
   if i % 2 == 0:
       evenList.append(i)
```

pythonic:

```python 
evenList = [i for i in range(0,101) if i % 2 == 0]
```

只用一行代码是不是很爽呢.

给出列表推导式的规范:

```
variable = [out_exp for out_exp in input_list if 某个条件成立]
```

### 字典推导式

设想一个场景,这里要求你把一个字典里所有的key和value位置交换

传统写法:

```pytohn 
ADict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

BDict = {}

for key, value in ADict.items():
    BDict[value] = key
```

pythonic:

```python
ADict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

BDict = {value: key for key, value in ADict.items()}
```

*熟练使用推导式可以让你的代码变得十分的简短!*

## 4.lambda表达式

这无疑是一个非常重要的语法,然而很多新手却不喜欢使用...

所谓lambda表达式就是匿名函数,我们为什么要使用匿名函数呢?有些时候我们想要使用一个函数但是整个程序中只需要使用这一次,这时候使用lambda表达式无疑最方便了

设想一个场景,有一个列表里面存放着一对对的元组,现在要按元组的第二个元素对该列表进行排序

传统方法:

```Python
aList = [(2, 3), (1, 2), (4, 5), (7, 4)]


def sortKey(x):
    return x[1]


aList.sort(key=sortKey)		# 注意不要写成aList = aList.sort(key=sortKey),它没有返回值

print(aList)
```

out:

```
[(1, 2), (2, 3), (7, 4), (4, 5)]
```

pythonic:

```python
aList = [(2, 3), (1, 2), (4, 5), (7, 4)]

aList.sort(key=lambda x: x[1])
```

out:

```
[(1, 2), (2, 3), (7, 4), (4, 5)]
```

给出规范:

```
lambda 参数:操作(参数)
```

注意后面的`操作(参数)`是要返回的

举个例子:

```python
add = lambda x, y: x + y
# 等价于下面的函数
def add(x, y):
    return x + y
```

## 5.装饰器

装饰器是Python非常非常非常重要的知识点,这里只做应用举例,以后我会出一期详细的讲解装饰器

设想一个场景,公司有好多的部门(函数)在同时运作,现在要求你在不改变运行代码的条件下,给每个部门新加一个功能

源代码:

```Python
def partA():
    print("----do A job----")

def partB():
    print("----do B job----")

def partC():
    print("----do C job----")

if __name__ == '__main__':
    partA()
    partB()
    partC()
```

out:

```
----do A job----
----do B job----
----do C job----
```



传统方法:

```Python
def partA():
    print("----do A job----")
    print("****do extra job****")

def partB():
    print("----do B job----")
    print("****do extra job****")

def partC():
    print("----do C job----")
    print("****do extra job****")

if __name__ == '__main__':
    partA()
    partB()
    partC()
```

out:

```
----do A job----
****do extra job****
----do B job----
****do extra job****
----do C job----
****do extra job****
```

pythonic:

```python
def doExtraJob(func):
    def wrap():
        func()
        print("****do extra job****")
    return wrap

@doExtraJob
def partA():
    print("----do A job----")

@doExtraJob
def partB():
    print("----do B job----")

@doExtraJob
def partC():
    print("----do C job----")

if __name__ == '__main__':
    partA()
    partB()
    partC()
```

out:

```
----do A job----
****do extra job****
----do B job----
****do extra job****
----do C job----
****do extra job****
```

对比两种方法,使用装饰器的效果就是可以让一个函数再不改变内部代码的情况下增加新的功能.

## 6.神奇的else语句

大部分人只知道else语句和if语句一起使用,但是你们知道吗else语句也可以和`for`语句,`while`语句,`try`语句一起使用

设想一个场景,你在对一个内部数据未知的列表进行循环时(不论是`for`还是`while`),你设置了一个遇到偶数就break的语句,倘若数组里不含偶数就输出`奇数列表`字样.

传统方法:

```python 
aList = [1, 3, 5, 7, 9]

flag = True
for i in aList:
    if i % 2 == 0:
        flag = False
        break

if flag:
    print("奇数列表")
```

pythonic:

```python 
aList = [1, 3, 5, 7, 9]

for i in aList:
    if i % 2 == 0:
        flag = False
        break
else:
    print("奇数列表")
```

注意,循环中(`for`或`while`)的else语句会在循环正常退出时(即不是由于break语句退出时)触发

对与`try,else`语句,else语句会在没有异常时被触发,也许你们会有疑问,没有异常直接在try语句里不是解决了吗,但是try语句里的操作会被捕获,有些时候我们并不想这样.

看个例子:

```Python
try:
    assert True
except:
    print("出错了")
else:
    print("没有错")
```

out:

```python 
没有错
```

`assert`为断言当其后面的语句为假是会报出异常,这和`try`语句一起使用有时候会非常的方便.



## 7.map函数

map函数会将一个函数映射到一个列表的所有元素上去.这和lambda表达式配合简直完美.

设想一个场景,一个列表里有1-10十个数,现要求你将这个列表里的每一个数的平方存入另一个列表,这并不难

传统方法:

```Python
aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

bList = []
for i in aList:
    bList.append(i**2)
```

pythonic:

```python 
aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

bList = list(map(lambda x:x**2, aList))
```

*千万注意map函数返回的不是列表是个`map对象`,需要类型转换*

## 8.filter函数

没错从函数的名字就可以看出`filter`函数的功能是过滤,`filter`可以过滤一个列表的元素并返回所有符合要求的元素组成的`filter对象`,和`map`类似注意类型转换.

设想一个场景,有一个列表,里面存放着一些未知的数字,现在要求你把所有的偶数挑选出来,

传统方法:

```python 
aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

bList = []
for each in aList:
    if each % 2 == 0:
        bList.append(each)
```

pythonic:

```python 
aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

bList = list(filter(lambda x: not x % 2, aList))
```

这里使用`not`是因为偶数除2的余数为0(Python中0为False),为了让偶数时返回True,用来一个not

## 9.reduce函数

注意:和前两个函数不同,reduce函数被放到了`functools`这个模块里,使用时需要导入.

`reduce`函数会将一个列表里的所有元素都用一个函数进行运算,要求这个函数必须有两个参数.

设想一个场景,要求求一个数字列表里所有的数字的平均值.

传统方法:

```Python
aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0
for i in aList:
    sum += i

ave = sum / len(aList)
```

pythonic:

````python 
from functools import reduce

aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ave = reduce(lambda x, y: x + y, aList) / len(aList)
````

`map`,`filter`,`reduce`函数和`lambda`配合使用才是精华所在.还有千万别弄混三个函数的功能

| 函数名 | 功能                                                       | 返回值     |
| ------ | ---------------------------------------------------------- | ---------- |
| map    | 单纯的将一个函数映射到一个列表的所有元素上去               | map对象    |
| filter | 过滤一个列表的元素并返回所有符合要求的元素组成的filter对象 | filter对象 |
| reduce | 将一个列表里的所有元素都用一个函数进行运算                 | 计算结果   |

## 10.总结

Python的sao操作还有很多,这次希望这次带来的几个用法对你们有所帮助,对于刚接触的人来说很容易忘记,希望大家可以多动手敲敲代码加强记忆,看看你们之前写的代码可不可以用这些sao操作改一改,使你的代码看上去更加精简.