## 列表雷区

```Python
>>> lists = [[]] * 3
>>> lists
 [[], [], []]
>>> lists[0].append(3)
>>> lists
 [[3], [3], [3]]
```


具体的原因在于 [[]] 是一个包含了一个空列表的单元素列表,所以 [[]] * 3 结果中的三个元素都是对这一个空列表的引用。修改 lists 中的任何一个元素实际上都是对这一个空列表的修改。你可以用以下方式创建以不同列表为元素的列表:

```python
>>> lists = [[] for i in range(3)]
>>> lists[0].append(3)
>>> lists[1].append(5)
>>> lists[2].append(7)
>>> lists
[[3], [5], [7]]
```

## 深拷贝和浅拷贝

简单理解:浅拷贝为同一个对象,深拷贝为不同对象

列表拷贝

a = b[:]	# 深拷贝

a = list(b)	# 深拷贝

```python
实例
#!/usr/bin/python
# -*-coding:utf-8 -*-
 
import copy
a = [1, 2, 3, 4, ['a', 'b']] #原始对象
 
b = a                       #赋值，传对象的引用
c = copy.copy(a)            #对象拷贝，浅拷贝
d = copy.deepcopy(a)        #对象拷贝，深拷贝
 
a.append(5)                 #修改对象a
a[4].append('c')            #修改对象a中的['a', 'b']数组对象
 
print( 'a = ', a )
print( 'b = ', b )
print( 'c = ', c )
print( 'd = ', d )
以上实例执行输出结果为：

('a = ', [1, 2, 3, 4, ['a', 'b', 'c'], 5])
('b = ', [1, 2, 3, 4, ['a', 'b', 'c'], 5])
('c = ', [1, 2, 3, 4, ['a', 'b', 'c']])
('d = ', [1, 2, 3, 4, ['a', 'b']])

```



字典拷贝

```python
In [38]: a = {1:[1,2]}                                                                        

In [39]: b = a.copy()                                                                         

In [40]: c = a.copy()                                                                         

In [41]: b[1].append(3)                                                                       

In [42]: a,b,c                                                                                
Out[42]: ({1: [1, 2, 3]}, {1: [1, 2, 3]}, {1: [1, 2, 3]})

In [43]: b[1].append('b')                                                                     

In [44]: a,b,c                                                                                
Out[44]: ({1: [1, 2, 3, 'b']}, {1: [1, 2, 3, 'b']}, {1: [1, 2, 3, 'b']})
    
--------------------------------------------------------------------------------------------    
In [46]: a = {1: [1,2,3]}                                                                     

In [47]: b = copy.deepcopy(a)                                                                 

In [48]: a[1].append('a')                                                                     

In [49]: a,b                                                                                  
Out[49]: ({1: [1, 2, 3, 'a']}, {1: [1, 2, 3]})


```

## 可迭代对象不等同于迭代器

```python
my_string = "Yasoob"
next(my_string)
# Output: Traceback (most recent call last):
#      File "<stdin>", line 1, in <module>
#    TypeError: str object is not an iterator
```

好吧，这不是我们预期的。这个异常说那个`str`对象不是一个迭代器。对，就是这样！它是一个可迭代对象，而不是一个迭代器。这意味着它支持迭代，但我们不能直接对其进行迭代操作。那我们怎样才能对它实施迭代呢？是时候学习下另一个内置函数，`iter`。它将根据一个可迭代对象返回一个迭代器对象。这里是我们如何使用它：

```python
my_string = "Yasoob"
my_iter = iter(my_string)
next(my_iter)
# Output: 'Y'
```

## 元组条件表达式会把条件都执行

```Python
condition = True
print(2 if condition else 1/0)
#输出: 2

print((1/0, 2)[condition])
#输出ZeroDivisionError异常
```

## 函数复制的误区

```Python
In [40]: def f1(): 
    ...:     print("hello world") 
    ...:                                                                                                                                             

In [41]: f2 = f1                                                                                                                                     

In [42]: f2()                                                                                                                                        
hello world

In [43]: del f1                                                                                                                                      

In [44]:                                                                                                                                             

In [44]: f2()                                                                                                                                        
hello world

In [45]: f1()                                                                                                                                        
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-45-b27bf7c7aafe> in <module>
----> 1 f1()

NameError: name 'f1' is not defined


```

## 装饰器输出名字不正确

```Python
# def MyFirstDecorator(func):
#     def wrapTheFunction():
#         print("我装饰前面")
#         func()
#         print("我装饰后面")
#     return wrapTheFunction
#
# @MyFirstDecorator
# def needDecoration():
#     print("我需要装饰")
#
# needDecoration()
# 等价于执行了下面两句：
# tempFun = MyFirstDecorator(needDecoration)
# tempFun()

# 如果我们运行如下代码会存在一个问题：
# print(needDecoration.__name__)  # wrapTheFunction

# 这里的函数被warpTheFunction替代了。它重写了我们函数的名字和注释文档(docstring)。幸运的是Python提供给我们一个简单的函数来解决这个问题，那就是functools.wraps。

# from functools import wraps
#
# def a_new_decorator(a_func):
#     @wraps(a_func)
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
#         a_func()
#         print("I am doing some boring work after executing a_func()")
#     return wrapTheFunction
#
# @a_new_decorator
# def a_function_requiring_decoration():
#     """Hey yo! Decorate me!"""
#     print("I am the function which needs some decoration to "
#           "remove my foul smell")
#
# print(a_function_requiring_decoration.__name__)
# # Output: a_function_requiring_decoration
```

## 装饰器内部函数使用return与不使用的区别

```Python
from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)	# ----------!!这里的return!!-------------
    return with_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x


result = addition_func(4)
print(result)	# 8,有return
						# None, 没return
```

被装饰的函数其实就是装饰器里返回的函数

如不加return上面的例子等价与

```Python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        # return func(*args, **kwargs)
        8
    return with_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x


result = addition_func(4)
print(result)	# None, 原因未将计算机结果8return
# Output: addition_func was called
```

## 打印排序列表

```Python
a = [3, 12, 4]
# print(a.sort())	# 输出None
a.sort()
print(a)	# 输出[3, 4, 12]
```

## 生成式

```Python
In [52]: def gg(): 
    ...:     for i in range(3): 
    ...:         yield i 
    ...:                                                                                          

In [53]: g = gg()                                                                                 

In [54]: next(g)                                                                                  
Out[54]: 0

In [55]: next(g)                                                                                  
Out[55]: 1

In [56]: next(g)                                                                                  
Out[56]: 2

In [57]: def ff(): 
    ...:     for i in range(3): 
    ...:         yield i 
    ...:                                                                                          

In [58]: next(ff())                                                                               
Out[58]: 0

In [59]: next(ff())                                                                               
Out[59]: 0

In [60]: next(ff())                                                                                                                                  
Out[60]: 0
```

