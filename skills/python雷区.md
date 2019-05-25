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

