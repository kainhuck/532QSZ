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
> 元组是不可变序列,通常用于储存异构数据的多项集(例如由enumerate() 内置函数所产生的二元组)。元组也被用于需要同构数据的不可变序列的情况(例如允许存储到set 或dict 的实例)。
> 
> class tuple([iterable ])
>     可以用多种方式构建元组:
>     • 使用一对圆括号来表示空元组: ()
>     • 使用一个后缀的逗号来表示单元组: a, 或 (a,)
>     • 使用以逗号分隔的多个项: a, b, c or (a, b, c)
>     • 使用内置的tuple(): tuple() 或 tuple(iterable)
> 
> 请注意决定生成元组的其实是逗号而不是圆括号。圆括号只是可选的,生成空元组或需要避免语法歧
> 义的情况除外。例如,f(a, b, c) 是在调用函数时附带三个参数,而 f((a, b, c)) 则是在调用函数
> 时附带一个三元组。
> 元组实现了所有一般 序列的操作。
> 
> 务必注意元组不可改变
> ```
>
> 字符串(str):
>
> ```
> python 中没有字符,一对单引号或者双引号代表字符串
> ```
>
> ```
> 同列表
> ```
>
> 此外,字符串还有的常用操作
>
> ```
> "*".join(string)	# 拼接
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

异常处理是一种艺术，一旦你掌握，会授予你无穷的力量。我将要向你展示我们能处理异常的一些方式。

最基本的术语里我们知道了`try/except`从句。可能触发异常产生的代码会放到`try`语句块里，而处理异常的代码会在`except`语句块里实现。这是一个简单的例子：

```Python
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
```

上面的例子里，我们仅仅在处理一个`IOError`的异常。大部分初学者还不知道的是，我们可以处理多个异常。

#### 处理多个异常

我们可以使用三种方法来处理多个异常。

第一种方法需要把所有可能发生的异常放到一个元组里。像这样：

```python
try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print("An error occurred. {}".format(e.args[-1]))
```

另外一种方式是对每个单独的异常在单独的`except`语句块中处理。我们想要多少个`except`语句块都可以。这里是个例子：

```Python
try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("An EOF error occurred.")
    raise e
except IOError as e:
    print("An error occurred.")
    raise e
```

上面这个方式中，如果异常没有被第一个`except`语句块处理，那么它也许被下一个语句块处理，或者根本不会被处理。

现在，最后一种方式会捕获**所有**异常：

```Python
try:
    file = open('test.txt', 'rb')
except Exception:
    # 打印一些异常日志，如果你想要的话
    raise
```

当你不知道你的程序会抛出什么样的异常时，上面的方式可能非常有帮助。

#### `finally`从句

我们把我们的主程序代码包裹进了`try`从句。然后我们把一些代码包裹进一个`except`从句，它会在`try`从句中的代码触发异常时执行。

在下面的例子中，我们还会使用第三个从句，那就是`finally`从句。包裹到`finally`从句中的代码不管异常是否触发都将会被执行。这可以被用来在脚本执行之后做清理工作。这里是个简单的例子：

```python
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception occurred!")

# Output: An IOError occurred. No such file or directory
# This would be printed whether or not an exception occurred!
```

#### `try/else`从句

我们常常想在没有触发异常的时候执行一些代码。这可以很轻松地通过一个`else`从句来达到。

有人也许问了：如果你只是想让一些代码在没有触发异常的情况下执行，为啥你不直接把代码放在`try`里面呢？
回答是，那样的话这段代码中的任意异常都还是会被`try`捕获，而你并不一定想要那样。

大多数人并不使用`else`从句，而且坦率地讲我自己也没有大范围使用。这里是个例子：

```python
try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # 这里的代码只会在try语句里没有触发异常时运行,
    # 但是这里的异常将 *不会* 被捕获
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print('This would be printed in every case.')

# Output: I am sure no exception is going to occur!
# This would only run if no exception occurs.
# This would be printed in every case.
```

`else`从句只会在没有异常的情况下执行，而且它会在`finally`语句之前执行。

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

*这个模块参考了这篇文章 -> <https://docs.pythontab.com/interpy/*>

### 0.`*args` 和 `**kwargs`

首先让我告诉你, 其实并不是必须写成`*args` 和`**kwargs`。 只有变量前面的 `*`(星号)才是必须的. 你也可以写成`*var` 和`**vars`. 而写成`*args` 和`**kwargs`只是一个通俗的命名约定。 那就让我们先看一下`*args`吧。

#### *args的例子

```Python
# *args用于输入不定数量的参数
def args_test(num, *args):
    print("第1个元素： " + str(num))
    for i in range(len(args)):
        print("第" + str(i+2) + "个元素： " + str(args[i]))

# args_test(123,64,12,7,99)
# 输出：
# 第1个元素： 123
# 第2个元素： 64
# 第3个元素： 12
# 第4个元素： 7
# 第5个元素： 99

--------------------------------------------------------------------------
In [1]: def f(*args): 
   ...:     print(type(args)) 
   ...:                                                                                       

In [2]: f(1,2,3,4,5,6)                                                                        
<class 'tuple'>
# 可见args为元组类型
```

#### **kwargs

```python 
# **kwargs 允许你将不定长度的键值对, 作为参数传递给一个函数。 如果你想要在一个函数里处理带名字的参数, 你应该使用**kwargs。
def kwargs_test_1(name, age, sex):
    print("name:", name)
    print("age:", age)
    print("sex:", sex)

# 普通用法
kwargs_test_1("kain", 18, "man")

# **kwargs用法
me = {
    "name": "kain",
    "age": 18,
    "sex": "man"
}
kwargs_test_1(**me)
----------------------------------------------------------------------------
In [4]: def kwargs_test_2(**kwargs): 
   ...:     # for item in kwargs: 
   ...:     #     print("{0} -> {1}".format(item, kwargs[item])) 
   ...:     for key, value in kwargs.items(): 
   ...:         print("{0} -> {1}".format(key, value)) 
   ...:                                                                                       

In [5]: kwargs_test_2(name="kain", age=18, sex="man")                                         
name -> kain
age -> 18
sex -> man

```

#### 同时具有*args和**kwargs

```Python
# 那么如果你想在函数里同时使用所有这三种参数， 顺序是这样的：
some_func(fargs, *args, **kwargs)
```

### 1.**生成器（Generators）**

#### 可迭代对象(Iterable)

Python中任意的对象，只要它定义了可以返回一个迭代器的`__iter__`方法，或者定义了可以支持下标索引的`__getitem__`方法(这些双下划线方法会在其他章节中全面解释)，那么它就是一个可迭代对象。

#### 迭代器(Iterator)

任意对象，只要定义了`next`(Python2) 或者`__next__`方法，它就是一个迭代器。

#### 迭代(Iteration)

用简单的话讲，它就是从某个地方（比如一个列表）取出一个元素的过程。当我们使用一个循环来遍历某个东西时，这个过程本身就叫迭代。

#### 生成器(Generators)

生成器也是一种迭代器，但是你只能对其迭代一次。

**这是因为它们并没有把所有的值存在内存中，而是在运行时生成值。**

通过遍历来使用它们，要么用一个“for”循环，要么将它们传递给任意可以进行迭代的函数和结构。

大多数时候生成器是以函数来实现的。然而，它们并不返回一个值，而是`yield`(暂且译作“生出”)一个值。

```python
def generator_function():
    for i in range(10):
        yield i

for item in generator_function():
    print(item)

# Output: 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
```

*生成器最佳应用场景是：你不想同一时间将所有计算出来的大量结果集分配到内存当中，特别是结果集里还包含循环。*

```PYTHON
# 生成器实现斐波那契数列
def fib(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

# for x in fib(100):
#     print(x)
```

**next()内置函数**

```python
def generator_function():
    for i in range(3):
        yield i

gen = generator_function()
print(next(gen))
# Output: 0
print(next(gen))
# Output: 1
print(next(gen))
# Output: 2
print(next(gen))
# Output: Traceback (most recent call last):
#            File "<stdin>", line 1, in <module>
#         StopIteration
```

我们可以看到，在`yield`掉所有的值后，`next()`触发了一个`StopIteration`的异常。基本上这个异常告诉我们，所有的值都已经被`yield`完了。你也许会奇怪，为什么我们在使用`for`循环时没有这个异常呢？啊哈，答案很简单。`for`循环会自动捕捉到这个异常并停止调用`next()`

**可迭代对象不等同于迭代器**

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

### 2.Map，Filter 和 Reduce

#### Map

`Map`会将一个函数映射到一个输入列表的所有元素上。这是它的规范：

**规范**

```python
map(function_to_apply, list_of_inputs)
```

大多数时候，我们要把列表中所有元素一个个地传递给一个函数，并收集输出。比方说：

```python 
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
```

`Map`可以让我们用一种简单而漂亮得多的方式来实现。就是这样：

```python
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

---------------------------------------------------------------------
In [20]: def fun(x): 
    ...:     return x*x 
    ...:                                                                                                                                             

In [21]: a = [1,2,3,4]                                                                                                                               

In [22]: b = map(fun, a)                                                                                                                             

In [23]: b                                                                                                                                           
Out[23]: <map at 0x7f7ae9822438>

In [24]: list(b)                                                                                                                                     
Out[24]: [1, 4, 9, 16]

```

大多数时候，我们使用匿名函数(lambdas)来配合`map`, 所以我在上面也是这么做的。 不仅用于一列表的输入， 我们甚至可以用于一列表的函数！

```python
def multiply(x):
        return (x*x)
def add(x):
        return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = map(lambda x: x(i), funcs)
    print(list(value))
    # 译者注：上面print时，加了list转换，是为了python2/3的兼容性
    #        在python2中map直接返回列表，但在python3中返回迭代器
    #        因此为了兼容python3, 需要list转换一下

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]
```

#### Filter

顾名思义，`filter`过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表，`符合要求`即函数映射到该元素时返回值为True. 这里是一个简短的例子：

```python
number_list = range(-5, 5)
less_than_zero = filter(lambda x: x < 0, number_list)
print(list(less_than_zero))  
# 译者注：上面print时，加了list转换，是为了python2/3的兼容性
#        在python2中filter直接返回列表，但在python3中返回迭代器
#        因此为了兼容python3, 需要list转换一下

# Output: [-5, -4, -3, -2, -1]
```

这个`filter`类似于一个`for`循环，但它是一个内置函数，并且更快。

**对比map和filter**

```python
In [34]: num_list = range(-5,5)                                                                                                                      

In [35]: less_zero = filter(lambda x: x<0, num_list)                                                                                                 

In [36]: less_zero2 = map(lambda x: x<0, num_list)                                                                                                   

In [37]: list(less_zero)                                                                                                                             
Out[37]: [-5, -4, -3, -2, -1]

In [38]: list(less_zero2)                                                                                                                            
Out[38]: [True, True, True, True, True, False, False, False, False, False]

```

可以看出map返回的是return的值,和filter返回的是自变量

#### Reduce

当需要对一个列表进行一些计算并返回结果时，`Reduce` 是个非常有用的函数。举个例子，当你需要计算一个整数列表的乘积时。

通常在 python 中你可能会使用基本的 for 循环来完成这个任务。

现在我们来试试 reduce：

```python
from functools import reduce
product = reduce( (lambda x, y: x * y), [1, 2, 3, 4] )

# Output: 24
```

### 3.set(集合)数据结构

`set`(集合)是一个非常有用的数据结构。它与列表(`list`)的行为类似，区别在于`set`不能包含重复的值。
这在很多情况下非常有用。例如你可能想检查列表中是否包含重复的元素，你有两个选择，第一个需要使用`for`循环，就像这样：

```Python
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
### 输出: ['b', 'n']
```

但还有一种更简单更优雅的解决方案，那就是使用`集合(sets)`，你直接这样做：

```python
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)
### 输出: set(['b', 'n'])
```

集合还有一些其它方法，下面我们介绍其中一部分。

**交集**

你可以对比两个集合的交集（两个集合中都有的数据），如下：

```python
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))
### 输出: set(['red'])
```

**差集**

你可以用差集(difference)找出无效的数据，相当于用一个集合减去另一个集合的数据，例如：

```python
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.difference(valid))
### 输出: set(['brown'])
```

你也可以用符号来创建集合，如：

```Python
a_set = {'red', 'blue', 'green'}
print(type(a_set))
### 输出: <type 'set'>
```

### 4.三元运算符

三元运算符通常在Python里被称为条件表达式，这些表达式基于真(true)/假(not)的条件判断，在Python 2.4以上才有了三元操作。

下面是一个伪代码和例子：

**伪代码:**

```Python
#如果条件为真，返回真 否则返回假
condition_is_true if condition else condition_is_false
```

**例子:**

```Python
is_fat = True
state = "fat" if is_fat else "not fat"
```

它允许用简单的一行快速判断，而不是使用复杂的多行`if`语句。 这在大多数时候非常有用，而且可以使代码简单可维护。

另一个晦涩一点的用法比较少见，它使用了元组，请继续看：

**伪代码:**

```Python
#(返回假，返回真)[真或假]
(if_test_is_false, if_test_is_true)[test]
```

**例子:**

```Python
fat = True
fitness = ("skinny", "fat")[fat]
print("Ali is ", fitness)
#输出: Ali is fat
```

这之所以能正常工作，是因为在Python中，True等于1，而False等于0，这就相当于在元组中使用0和1来选取数据。

上面的例子没有被广泛使用，而且Python玩家一般不喜欢那样，因为没有Python味儿(Pythonic)。这样的用法很容易把真正的数据与true/false弄混。

另外一个不使用元组条件表达式的缘故是因为在**元组中会把两个条件都执行**，而 `if-else` 的条件表达式不会这样。

例如:

```python
condition = True
print(2 if condition else 1/0)
#输出: 2

print((1/0, 2)[condition])
#输出ZeroDivisionError异常
```

这是因为在元组中是先建数据，然后用True(1)/False(0)来索引到数据。 而`if-else`条件表达式遵循普通的`if-else`逻辑树， 因此，如果逻辑中的条件异常，或者是重计算型（计算较久）的情况下，最好尽量避免使用元组条件表达式。

### 5.**装饰器**

装饰器(Decorators)是Python的一个重要部分。简单地说：他们是修改其他函数的功能的函数。他们有助于让我们的代码更简短，也更Pythonic（Python范儿）。

#### 一切皆对象

首先我们来理解下Python中的函数

```python
def hi(name="yasoob"):
    return "hi " + name

print(hi())
# output: 'hi yasoob'

# 我们甚至可以将一个函数赋值给一个变量，比如
greet = hi
# 我们这里没有在使用小括号，因为我们并不是在调用hi函数
# 而是在将它放在greet变量里头。我们尝试运行下这个

print(greet())
# output: 'hi yasoob'

# 如果我们删掉旧的hi函数，看看会发生什么！
del hi
print(hi())
#outputs: NameError

print(greet())
#outputs: 'hi yasoob'
```

#### 在函数中定义函数

刚才那些就是函数的基本知识了。我们来让你的知识更进一步。在Python中我们可以在一个函数中定义另一个函数：

```python
def hi(name="yasoob"):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")

hi()
#output:now you are inside the hi() function
#       now you are in the greet() function
#       now you are in the welcome() function
#       now you are back in the hi() function

# 上面展示了无论何时你调用hi(), greet()和welcome()将会同时被调用。
# 然后greet()和welcome()函数在hi()函数之外是不能访问的，比如：

greet()
#outputs: NameError: name 'greet' is not defined
```

那现在我们知道了可以在函数中定义另外的函数。也就是说：我们可以创建嵌套的函数。现在你需要再多学一点，就是函数也能返回函数。

#### 从函数中返回函数

其实并不需要在一个函数里去执行另一个函数，我们也可以将其作为输出返回出来：

```python
def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome

a = hi()
print(a)
#outputs: <function greet at 0x7f2143c01500>

#上面清晰地展示了`a`现在指向到hi()函数中的greet()函数
#现在试试这个

print(a())
#outputs: now you are in the greet() function
```

再次看看这个代码。在`if/else`语句中我们返回`greet`和`welcome`，而不是`greet()`和`welcome()`。为什么那样？这是因为当你把一对小括号放在后面，这个函数就会执行；然而如果你不放括号在它后面，那它可以被到处传递，并且可以赋值给别的变量而不去执行它。

你明白了吗？让我再稍微多解释点细节。

当我们写下`a = hi()`，`hi()`会被执行，而由于`name`参数默认是*yasoob*，所以函数`greet`被返回了。如果我们把语句改为`a = hi(name = "ali")`，那么`welcome`函数将被返回。我们还可以打印出`hi()()`，这会输出*now you are in the greet() function*。

#### 将函数作为参数传给另一个函数

```Python
def hi():
    return "hi yasoob!"

def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())

doSomethingBeforeHi(hi)
#outputs:I am doing some boring work before executing hi()
#        hi yasoob!
```

现在你已经具备所有必需知识，来进一步学习装饰器真正是什么了。装饰器让你在一个函数的前后去执行代码。

#### 你的第一个装饰器

在上一个例子里，其实我们已经创建了一个装饰器！现在我们修改下上一个装饰器，并编写一个稍微更有用点的程序：

```python
def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

a_function_requiring_decoration()
#outputs: "I am the function which needs some decoration to remove my foul smell"

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
#now a_function_requiring_decoration is wrapped by wrapTheFunction()

a_function_requiring_decoration()
#outputs:I am doing some boring work before executing a_func()
#        I am the function which needs some decoration to remove my foul smell
#        I am doing some boring work after executing a_func()
```

你看明白了吗？我们刚刚应用了之前学习到的原理。这正是python中装饰器做的事情！它们封装一个函数，并且用这样或者那样的方式来修改它的行为。现在你也许疑惑，我们在代码里并没有使用@符号？那只是一个简短的方式来生成一个被装饰的函数。这里是我们如何使用@来运行之前的代码：

```Python
@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")

a_function_requiring_decoration()
#outputs: I am doing some boring work before executing a_func()
#         I am the function which needs some decoration to remove my foul smell
#         I am doing some boring work after executing a_func()

#the @a_new_decorator is just a short way of saying:
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
```

希望你现在对Python装饰器的工作原理有一个基本的理解。如果我们运行如下代码会存在一个问题：

```python
print(a_function_requiring_decoration.__name__)
# Output: wrapTheFunction
```

这并不是我们想要的！Ouput输出应该是“a_function_requiring_decoration”。这里的函数被warpTheFunction替代了。它重写了我们函数的名字和注释文档(docstring)。幸运的是Python提供给我们一个简单的函数来解决这个问题，那就是functools.wraps。我们修改上一个例子来使用functools.wraps：

```Python
from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")

print(a_function_requiring_decoration.__name__)
# Output: a_function_requiring_decoration
```

现在好多了。我们接下来学习装饰器的一些常用场景。

蓝本规范:

```Python
from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = True
print(func())
# Output: Function is running
'''
func = decorator_name(func)
func():
	if not can_run:
            return "Function will not run"
        return func()
'''

can_run = False
print(func())
# Output: Function will not run
```

注意：@wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。

#### 使用场景

**授权(Authorization)**

装饰器能有助于检查某个人是否被授权去使用一个web应用的端点(endpoint)。它们被大量使用于Flask和Django web框架中。这里是一个例子来使用基于装饰器的授权：

```Python
from functools import wraps

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)
    return decorated
```

**日志(Logging)**

日志是装饰器运用的另一个亮点。这是个例子：

```Python
from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x


result = addition_func(4)
# Output: addition_func was called
```

#### 带参数的装饰器

来想想这个问题，难道`@wraps`不也是个装饰器吗？但是，它接收一个参数，就像任何普通的函数能做的那样。那么，为什么我们不也那样做呢？

这是因为，当你使用`@my_decorator`语法时，你是在应用一个以单个函数作为参数的一个包裹函数。记住，Python里每个东西都是一个对象，而且这包括函数！记住了这些，我们可以编写一下能返回一个包裹函数的函数。

#### 在函数中嵌入装饰器

我们回到日志的例子，并创建一个包裹函数，能让我们指定一个用于输出的日志文件。

```python
from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit()	# 后面跟()相当与执行了这个函数,于是就把正真的装饰器返回出来了
def myfunc1():
    pass

myfunc1()
# Output: myfunc1 was called
# 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串

@logit(logfile='func2.log')
def myfunc2():
    pass

myfunc2()
# Output: myfunc2 was called
# 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串
```

#### 装饰器类

现在我们有了能用于正式环境的`logit`装饰器，但当我们的应用的某些部分还比较脆弱时，异常也许是需要更紧急关注的事情。比方说有时你只想打日志到一个文件。而有时你想把引起你注意的问题发送到一个email，同时也保留日志，留个记录。这是一个使用继承的场景，但目前为止我们只看到过用来构建装饰器的函数。

幸运的是，类也可以用来构建装饰器。那我们现在以一个类而不是一个函数的方式，来重新构建`logit`。

```Python
from functools import wraps

class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        pass
```

这个实现有一个附加优势，在于比嵌套函数的方式更加整洁，而且包裹一个函数还是使用跟以前一样的语法：

```Python
@logit()
def myfunc1():
    pass
```

现在，我们给`logit`创建子类，来添加email的功能(虽然email这个话题不会在这里展开)。

```Python
class email_logit(logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''
    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(logit, self).__init__(*args, **kwargs)

    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        pass
```

从现在起，`@email_logit`将会和`@logit`产生同样的效果，但是在打日志的基础上，还会多发送一封邮件给管理员。

### 6.**对象变动(Mutation)**

***初学者在使用Python的可变对象(比如列表)时最琢磨不透的问题***

举个例子:

```Python
foo = ['hi']
print(foo)
# Output: ['hi']
bar = foo
bar += ['bye']
print(foo)
# Output: ['hi', 'bye']
```

这可能不是你的预期,你的预期可能是下面这样:

```Python
foo = ['hi']
print(foo)
# Output: ['hi']

bar = foo
bar += ['bye']

print(foo)
# Output: ['hi']

print(bar)
# Output: ['hi', 'bye']
```

这不是一个bug。这是对象可变性(**mutability**)在作怪。每当你将一个变量赋值为另一个可变类型的变量时，对这个数据的任意改动会同时反映到这两个变量上去。新变量只不过是老变量的一个别名而已(这不就是引用吗)。***这个情况只是针对可变数据类型***。下面的函数和可变数据类型让你一下就明白了：

```Python
def add_to(num, target=[]):
    target.append(num)
    return target

add_to(1)
# Output: [1]

add_to(2)
# Output: [1, 2]

add_to(3)
# Output: [1, 2, 3]
```

你可能预期它表现的不是这样子。你可能希望，当你调用`add_to`时，有一个新的列表被创建，就像这样：

```python
def add_to(num, target=[]):
    target.append(num)
    return target

add_to(1)
# Output: [1]

add_to(2)
# Output: [2]

add_to(3)
# Output: [3]
```

啊哈！这次又没有达到预期，是列表的可变性在作怪。***在Python中当函数被定义时，默认参数只会运算一次，而不是每次被调用时都会重新运算。****你应该永远不要定义可变类型的默认参数*，除非你知道你正在做什么。你应该像这样做：

```python
def add_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target
```

现在每当你在调用这个函数不传入`target`参数的时候，一个新的列表会被创建。举个例子：

```Python
add_to(42)
# Output: [42]

add_to(42)
# Output: [42]

add_to(42)
# Output: [42]
```

### 7.`__slots__`魔法

在Python中，每个类都有实例属性。默认情况下Python用一个字典来保存一个对象的实例属性。这非常有用，因为它允许我们在运行时去设置任意的新属性。

然而，对于有着已知属性的小类来说，它可能是个瓶颈。这个字典浪费了很多内存。Python不能在对象创建时直接分配一个固定量的内存来保存所有的属性。因此如果你创建许多对象（我指的是成千上万个），它会消耗掉很多内存。
不过还是有一个方法来规避这个问题。这个方法需要使用`__slots__`来告诉Python不要使用字典，而且只给一个固定集合的属性分配空间。

这里是一个使用与不使用`__slots__`的例子：

- 不使用 `__slots__`:

```
class MyClass(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()
    # ...
```

- 使用 `__slots__`:

```Python
class MyClass(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()
    # ...
```

第二段代码会为你的内存减轻负担。通过这个技巧，有些人已经看到内存占用率几乎40%~50%的减少。

稍微备注一下，你也许需要试一下PyPy。它已经默认地做了所有这些优化。

以下你可以看到一个例子，它用IPython来展示在有与没有`__slots__`情况下的精确内存占用，感谢 https://github.com/ianozsvald/ipython_memory_usage

```Python
Python 3.4.3 (default, Jun  6 2015, 13:32:34)
Type "copyright", "credits" or "license" for more information.

IPython 4.0.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: import ipython_memory_usage.ipython_memory_usage as imu

In [2]: imu.start_watching_memory()
In [2] used 0.0000 MiB RAM in 5.31s, peaked 0.00 MiB above current, total RAM usage 15.57 MiB

In [3]: %cat slots.py
class MyClass(object):
        __slots__ = ['name', 'identifier']
        def __init__(self, name, identifier):
                self.name = name
                self.identifier = identifier

num = 1024*256
x = [MyClass(1,1) for i in range(num)]
In [3] used 0.2305 MiB RAM in 0.12s, peaked 0.00 MiB above current, total RAM usage 15.80 MiB

In [4]: from slots import *
In [4] used 9.3008 MiB RAM in 0.72s, peaked 0.00 MiB above current, total RAM usage 25.10 MiB

In [5]: %cat noslots.py
class MyClass(object):
        def __init__(self, name, identifier):
                self.name = name
                self.identifier = identifier

num = 1024*256
x = [MyClass(1,1) for i in range(num)]
In [5] used 0.1758 MiB RAM in 0.12s, peaked 0.00 MiB above current, total RAM usage 25.28 MiB

In [6]: from noslots import *
In [6] used 22.6680 MiB RAM in 0.80s, peaked 0.00 MiB above current, total RAM usage 47.95 MiB
```

### 8.容器(`Collections`)

Python附带一个模块，它包含许多容器数据类型，名字叫作`collections`。我们将讨论它的作用和用法。

我们将讨论的是：

- defaultdict
- counter
- deque
- namedtuple
- enum.Enum (包含在Python 3.4以上)

#### defaultdict

我个人使用`defaultdict`较多，与`dict`类型不同，你不需要检查**key**是否存在，所以我们能这样做：

```Python
from collections import defaultdict

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)
```

运行输出

```Python
# defaultdict(<type 'list'>,
#    {'Arham': ['Green'],
#     'Yasoob': ['Yellow', 'Red'],
#     'Ahmed': ['Silver'],
#     'Ali': ['Blue', 'Black']
# })
```

另一种重要的是例子就是：当你在一个字典中对一个键进行嵌套赋值时，如果这个键不存在，会触发`keyError`异常。 `defaultdict`允许我们用一个聪明的方式绕过这个问题。 首先我分享一个使用`dict`触发`KeyError`的例子，然后提供一个使用`defaultdict`的解决方案。

**问题**：

```Python
some_dict = {}
some_dict['colours']['favourite'] = "yellow"

## 异常输出：KeyError: 'colours'
```

**解决方案**：

```python
import collections
tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"

## 运行正常
```

你可以用`json.dumps`打印出`some_dict`，例如：

```python
import json
print(json.dumps(some_dict))

## 输出: {"colours": {"favourite": "yellow"}}
```

#### counter

Counter是一个计数器，它可以帮助我们针对某项数据进行计数。比如它可以用来计算每个人喜欢多少种颜色：

```Python
from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(name for name, colour in colours)
print(favs)

## 输出:
## Counter({
##     'Yasoob': 2,
##     'Ali': 2,
##     'Arham': 1,
##     'Ahmed': 1
##  })
```

我们也可以在利用它统计一个文件，例如：

```python
with open('filename', 'rb') as f:
    line_count = Counter(f)
print(line_count)
```

#### deque

deque提供了一个双端队列，你可以从头/尾两端添加或删除元素。要想使用它，首先我们要从`collections`中导入`deque`模块：

```Python
from collections import deque
```

现在，你可以创建一个`deque`对象。

```Python
d = deque()
```

它的用法就像python的`list`，并且提供了类似的方法，例如：

```Python
d = deque()
d.append('1')
d.append('2')
d.append('3')

print(len(d))

## 输出: 3

print(d[0])

## 输出: '1'

print(d[-1])

## 输出: '3'
```

你可以从两端取出(pop)数据：

```Python
d = deque(range(5))
print(len(d))

## 输出: 5

d.popleft()

## 输出: 0

d.pop()

## 输出: 4

print(d)

## 输出: deque([1, 2, 3])
```

我们也可以限制这个列表的大小，当超出你设定的限制时，数据会从对队列另一端被挤出去(pop)。
最好的解释是给出一个例子：

```Python
d = deque(maxlen=30)
```

现在当你插入30条数据时，最左边一端的数据将从队列中删除。

你还可以从任一端扩展这个队列中的数据：

```Python
d = deque([1,2,3,4,5])
d.extendleft([0])
d.extend([6,7,8])
print(d)

## 输出: deque([0, 1, 2, 3, 4, 5, 6, 7, 8])
```

#### namedtuple

您可能已经熟悉元组。
一个元组是一个不可变的列表，你可以存储一个数据的序列，它和命名元组(`namedtuples`)非常像，但有几个关键的不同。
主要相似点是都不像列表，你不能修改元组中的数据。为了获取元组中的数据，你需要使用整数作为索引：

```Python
man = ('Ali', 30)
print(man[0])

## 输出: Ali
```

嗯，那`namedtuples`是什么呢？它把元组变成一个针对简单任务的容器。你不必使用整数索引来访问一个`namedtuples`的数据。你可以像字典(`dict`)一样访问`namedtuples`，但`namedtuples`是不可变的。

```Python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")

print(perry)

## 输出: Animal(name='perry', age=31, type='cat')

print(perry.name)

## 输出: 'perry'
```

现在你可以看到，我们可以用名字来访问`namedtuple`中的数据。我们再继续分析它。一个命名元组(`namedtuple`)有两个必需的参数。它们是元组名称和字段名称。

在上面的例子中，我们的元组名称是`Animal`，字段名称是'name'，'age'和'type'。
`namedtuple`让你的元组变得**自文档**了。你只要看一眼就很容易理解代码是做什么的。
你也不必使用整数索引来访问一个命名元组，这让你的代码更易于维护。
而且，**namedtuple的每个实例没有对象字典**，所以它们很轻量，与普通的元组比，并不需要更多的内存。这使得它们比字典更快。

然而，要记住它是一个元组，属性值在`namedtuple`中是不可变的，所以下面的代码不能工作：

```Python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
perry.age = 42

## 输出:
## Traceback (most recent call last):
##     File "", line 1, in
## AttributeError: can't set attribute
```

你应该使用命名元组来让代码**自文档**，**它们向后兼容于普通的元组**，这意味着你可以既使用整数索引，也可以使用名称来访问`namedtuple`：

```Python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
print(perry[0])

## 输出: perry
```

最后，你可以将一个命名元组转换为字典，方法如下：

```Python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type="cat")
print(perry._asdict())

## 输出: OrderedDict([('name', 'Perry'), ('age', 31), ...
```

#### enum.Enum (Python 3.4+)

另一个有用的容器是枚举对象，它属于`enum`模块，存在于Python 3.4以上版本中（同时作为一个独立的PyPI包`enum34`供老版本使用）。Enums(枚举类型)基本上是一种组织各种东西的方式。

让我们回顾一下上一个'Animal'命名元组的例子。
它有一个type字段，问题是，type是一个字符串。
那么问题来了，万一程序员输入了`Cat`，因为他按到了Shift键，或者输入了'CAT'，甚至'kitten'？

枚举可以帮助我们避免这个问题，通过不使用字符串。考虑以下这个例子：

```python 
from collections import namedtuple
from enum import Enum

class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9
    # 依次类推

    # 但我们并不想关心同一物种的年龄，所以我们可以使用一个别名
    kitten = 1  # (译者注：幼小的猫咪)
    puppy = 2   # (译者注：幼小的狗狗)

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type=Species.cat)
drogon = Animal(name="Drogon", age=4, type=Species.dragon)
tom = Animal(name="Tom", age=75, type=Species.cat)
charlie = Animal(name="Charlie", age=2, type=Species.kitten)
```

**现在，我们进行一些测试：**

```python 
>>> charlie.type == tom.type
True
>>> charlie.type
<Species.cat: 1>
```

这样就没那么容易错误，我们必须更明确，而且我们应该只使用定义后的枚举类型。

有三种方法访问枚举数据，例如以下方法都可以获取到'cat'的值：

```python 
Species(1)
Species['cat']
Species.cat
```

这只是一个快速浏览`collections`模块的介绍，建议你阅读本文最后的官方文档。

### 9.枚举

枚举(`enumerate`)是Python内置函数。它的用处很难在简单的一行中说明，但是大多数的新人，甚至一些高级程序员都没有意识到它。

它允许我们遍历数据并自动计数，

下面是一个例子：

```python
for counter, value in enumerate(some_list):
    print(counter, value)
```

不只如此，`enumerate`也接受一些可选参数，这使它更有用。

```python 
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)

# 输出:
(1, 'apple')
(2, 'banana')
(3, 'grapes')
(4, 'pear')
```

上面这个可选参数允许我们定制从哪个数字开始枚举。
你还可以用来创建包含索引的元组列表， 例如：

```python 
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
# 输出: [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]
```

### 10.对象自省

#### dir

它是用于自省的最重要的函数之一。它返回一个列表，列出了一个对象所拥有的属性和方法。这里是一个例子：

```python 
my_list = [1, 2, 3]
dir(my_list)
# Output: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
# '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__',
# '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
# '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__',
# '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop',
# 'remove', 'reverse', 'sort']
```

上面的自省给了我们一个列表对象的所有方法的名字。当你没法回忆起一个方法的名字，这会非常有帮助。如果我们运行`dir()`而不传入参数，那么它会返回当前作用域的所有名字。



#### `type`和`id`

`type`函数返回一个对象的类型。举个例子：

```python
print(type(''))
# Output: <type 'str'>

print(type([]))
# Output: <type 'list'>

print(type({}))
# Output: <type 'dict'>

print(type(dict))
# Output: <type 'type'>

print(type(3))
# Output: <type 'int'>
```

`id()`函数返回任意不同种类对象的唯一ID，举个例子：

```python 
name = "Yasoob"
print(id(name))
# Output: 139972439030304
```

#### `inspect`模块

`inspect`模块也提供了许多有用的函数，来获取活跃对象的信息。比方说，你可以查看一个对象的成员，只需运行：

```python
import inspect
print(inspect.getmembers(str))
# Output: [('__add__', <slot wrapper '__add__' of ... ...
```

还有好多个其他方法也能有助于自省。如果你愿意，你可以去探索它们。

### 11.**各种推导式(comprehensions)**

推导式（又称解析式）是Python的一种独有特性，如果我被迫离开了它，我会非常想念。推导式是可以从一个数据序列构建另一个新的数据序列的结构体。 共有三种推导，在Python2和3中都有支持：

- 列表(`list`)推导式
- 字典(`dict`)推导式
- 集合(`set`)推导式

我们将一一进行讨论。一旦你知道了使用列表推导式的诀窍，你就能轻易使用任意一种推导式了。

#### 列表推导式（`list` comprehensions）

列表推导式（又称列表解析式）提供了一种简明扼要的方法来创建列表。
它的结构是在一个中括号里包含一个表达式，然后是一个`for`语句，然后是0个或多个`for`或者`if`语句。那个表达式可以是任意的，意思是你可以在列表中放入任意类型的对象。返回结果将是一个新的列表，在这个以`if`和`for`语句为上下文的表达式运行完成之后产生。

### 规范

```python
variable = [out_exp for out_exp in input_list if out_exp == 2]
```

这里是另外一个简明例子:

```python
multiples = [i for i in range(30) if i % 3 is 0]
print(multiples)
# Output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
```

这将对快速生成列表非常有用。
有些人甚至更喜欢使用它而不是`filter`函数。
列表推导式在有些情况下超赞，特别是当你需要使用`for`循环来生成一个新列表。举个例子，你通常会这样做：

```python
squared = []
for x in range(10):
    squared.append(x**2)
```

你可以使用列表推导式来简化它，就像这样：

```python
squared = [x**2 for x in range(10)]
```

#### 字典推导式（`dict` comprehensions）

字典推导和列表推导的使用方法是类似的。这里有个我最近发现的例子：

```python
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)	# 注:若不存在这个key就会返回后面的0
    for k in mcase.keys()
}

# mcase_frequency == {'a': 17, 'z': 3, 'b': 34}
```

在上面的例子中我们把同一个字母但不同大小写的值合并起来了。

就我个人来说没有大量使用字典推导式。

你还可以快速对换一个字典的键和值：

```python
{v: k for k, v in some_dict.items()}
```

#### 集合推导式（`set` comprehensions）

它们跟列表推导式也是类似的。 唯一的区别在于它们使用大括号`{}`。 举个例子：

```python
squared = {x**2 for x in [1, 1, 2]}
print(squared)
# Output: {1, 4}
```

### 12.**lambda表达式**

***这个也是Python中非常重要的语法之一***

`lambda`表达式是一行函数。
它们在其他语言中也被称为匿名函数。如果你不想在程序中对一个函数使用两次，你也许会想用lambda表达式，它们和普通的函数完全一样。

**原型**

```Python
    lambda 参数:操作(参数)
```

**例子**

```Python
    add = lambda x, y: x + y

    print(add(3, 5))
    # Output: 8
```

这还有一些lambda表达式的应用案例，可以在一些特殊情况下使用：

**列表排序**

```Python
    a = [(1, 2), (4, 1), (9, 10), (13, -3)]
    a.sort(key=lambda x: x[1])

    print(a)
    # Output: [(13, -3), (4, 1), (1, 2), (9, 10)]
```

**列表并行排序**

```python
    data = zip(list1, list2)
    data.sort()
    list1, list2 = map(lambda t: list(t), zip(*data))
```

### 13.一行式

本章节,我将向大家展示一些一行式的Python命令，这些程序将对你非常有帮助。

**简易Web Server**

你是否想过通过网络快速共享文件？好消息，Python为你提供了这样的功能。进入到你要共享文件的目录下并在命令行中运行下面的代码：

```Python
    # Python 2
    python -m SimpleHTTPServer

    # Python 3
    python -m http.server
```

**漂亮的打印**

你可以在Python REPL漂亮的打印出列表和字典。这里是相关的代码：

```Python
    from pprint import pprint

    my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
    pprint(my_dict)
```

这种方法在字典上更为有效。此外，如果你想快速漂亮的从文件打印出json数据，那么你可以这么做：

```Python
    cat file.json | python -m json.tool
```

**脚本性能分析** 这可能在定位你的脚本中的性能瓶颈时，会非常奏效：

```Python
    python -m cProfile my_script.py
```

备注：`cProfile`是一个比`profile`更快的实现，因为它是用c写的

**CSV转换为json**

在命令行执行这条指令

```Python
    python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"
```

确保更换`csv_file.csv`为你想要转换的csv文件

**列表辗平**

您可以通过使用`itertools`包中的`itertools.chain.from_iterable`轻松快速的辗平一个列表。下面是一个简单的例子：

```python
    a_list = [[1, 2], [3, 4], [5, 6]]
    print(list(itertools.chain.from_iterable(a_list)))
    # Output: [1, 2, 3, 4, 5, 6]

    # or
    print(list(itertools.chain(*a_list)))
    # Output: [1, 2, 3, 4, 5, 6]
```

**一行式的构造器**

避免类初始化时大量重复的赋值语句

```python
    class A(object):
        def __init__(self, a, b, c, d, e, f):
            self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})
            # locals() 函数会以字典类型返回当前位置的全部局部变量。
```

更多的一行方法请参考[Python官方文档](https://wiki.python.org/moin/Powerful Python One-Liners)。

### 14.For - Else

循环是任何语言的一个必备要素。同样地，`for`循环就是Python的一个重要组成部分。然而还有一些东西是初学者并不知道的。我们将一个个讨论一下。

我们先从已经知道的开始。我们知道可以像这样使用`for`循环：

```python
fruits = ['apple', 'banana', 'mango']
for fruit in fruits:
    print(fruit.capitalize())

# Output: Apple
#         Banana
#         Mango
```

这是一个`for`循环非常基础的结构。现在我们继续看看，Python的`for`循环的一些鲜为人所知的特性。

#### `else`从句

`for`循环还有一个`else`从句，我们大多数人并不熟悉。***这个`else`从句会在循环正常结束时执行***。这意味着，循环没有遇到任何`break`. 一旦你掌握了何时何地使用它，它真的会非常有用。我自己对它真是相见恨晚。

有个常见的构造是跑一个循环，并查找一个元素。如果这个元素被找到了，我们使用`break`来中断这个循环。有两个场景会让循环停下来。 - 第一个是当一个元素被找到，`break`被触发。 - 第二个场景是循环结束。

现在我们也许想知道其中哪一个，才是导致循环完成的原因。一个方法是先设置一个标记，然后在循环结束时打上标记。另一个是使用`else`从句。

这就是`for/else`循环的基本结构：

```Python
for item in container:
    if search_something(item):
        # Found it!
        process(item)
        break
else:
    # Didn't find anything..
    not_found_in_container()
```

考虑下这个简单的案例，它是我从官方文档里拿来的：

```Python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break
```

它会找出2到10之间的数字的因子。现在是趣味环节了。我们可以加上一个附加的else语句块，来抓住质数，并且告诉我们：

```Python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
```

### 15.协程

Python中的协程和生成器很相似但又稍有不同。主要区别在于： *生成器是数据的生产者* 协程则是数据的消费者

首先我们先来回顾下生成器的创建过程。我们可以这样去创建一个生成器:

```python
    def fib():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a+b
```

然后我们经常在`for`循环中这样使用它:

```python
    for i in fib():
        print i
```

这样做不仅快而且不会给内存带来压力，因为我们所需要的值都是动态生成的而不是将他们存储在一个列表中。更概括的说如果现在我们在上面的例子中使用`yield`便可获得了一个协程。协程会消费掉发送给它的值。Python实现的`grep`就是个很好的例子：

```python
    def grep(pattern):
        print("Searching for", pattern)
        while True:
            line = (yield)	
            if pattern in line:
                print(line) 
```

等等！`yield`返回了什么？啊哈，我们已经把它变成了一个协程。它将不再包含任何初始值，相反要从外部传值给它。我们可以通过`send()`方法向它传值。这有个例子：

```python
    search = grep('coroutine')
    next(search)
    #output: Searching for coroutine
    search.send("I love you")
    search.send("Don't you love me?")
    search.send("I love coroutine instead!")
    #output: I love coroutine instead!
```

发送的值会被`yield`接收。我们为什么要运行`next()`方法呢？这样做正是为了启动一个协程。就像协程中包含的生成器并不是立刻执行，而是通过`next()`方法来响应`send()`方法。因此，你必须通过`next()`方法来执行`yield`表达式。

我们可以通过调用`close()`方法来关闭一个协程。像这样：

```python
    search = grep('coroutine')
    search.close()
```

### 16.函数缓存 (Function caching)

函数缓存允许我们将一个函数对于给定参数的返回值缓存起来。
当一个I/O密集的函数被频繁使用相同的参数调用的时候，函数缓存可以节约时间。
在Python 3.2版本以前我们只有写一个自定义的实现。在Python 3.2以后版本，有个`lru_cache`的装饰器，允许我们将一个函数的返回值快速地缓存或取消缓存。

#### Python 3.2及以后版本

我们来实现一个斐波那契计算器，并使用`lru_cache`。

```python
from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

>>> print([fib(n) for n in range(10)])
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

那个`maxsize`参数是告诉`lru_cache`，最多缓存最近多少个返回值。

我们也可以轻松地对返回值清空缓存，通过这样：

```python
fib.cache_clear()
```

### 17.上下文管理器(Context managers)

上下文管理器允许你在有需要的时候，精确地分配和释放资源。

使用上下文管理器最广泛的案例就是`with`语句了。
想象下***你有两个需要结对执行的相关操作，然后还要在它们中间放置一段代码。***
***上下文管理器就是专门让你做这种事情的。***举个例子：

```Python
with open('some_file', 'w') as opened_file:
    opened_file.write('Hola!')
```

上面这段代码打开了一个文件，往里面写入了一些数据，然后关闭该文件。如果在往文件写数据时发生异常，它也会尝试去关闭文件。上面那段代码与这一段是等价的：

```Python
file = open('some_file', 'w')
try:
    file.write('Hola!')
finally:
    file.close()
```

当与第一个例子对比时，我们可以看到，通过使用`with`，许多样板代码(boilerplate code)被消掉了。 这就是`with`语句的主要优势，它确保我们的文件会被关闭，而不用关注嵌套代码如何退出。

上下文管理器的一个常见用例，是资源的加锁和解锁，以及关闭已打开的文件（就像我已经展示给你看的）。

让我们看看如何来实现我们自己的上下文管理器。这会让我们更完全地理解在这些场景背后都发生着什么。

#### 基于类的实现

一个上下文管理器的类，最起码要定义`__enter__`和`__exit__`方法。
让我们来构造我们自己的开启文件的上下文管理器，并学习下基础知识。

```Python
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()
```

通过定义`__enter__`和`__exit__`方法，我们可以在`with`语句里使用它。我们来试试：

```Python
with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')
```

我们的`__exit__`函数接受三个参数。这些参数对于每个上下文管理器类中的`__exit__`方法都是必须的。我们来谈谈在底层都发生了什么。

1. `with`语句先暂存了`File`类的`__exit__`方法
2. 然后它调用`File`类的`__enter__`方法
3. `__enter__`方法打开文件并返回给`with`语句
4. 打开的文件句柄被传递给`opened_file`参数
5. 我们使用`.write()`来写文件
6. `with`语句调用之前暂存的`__exit__`方法
7. `__exit__`方法关闭了文件

#### 处理异常

我们还没有谈到`__exit__`方法的这三个参数：`type`, `value`和`traceback`。
在第4步和第6步之间，如果发生异常，Python会将异常的`type`,`value`和`traceback`传递给`__exit__`方法。
它让`__exit__`方法来决定如何关闭文件以及是否需要其他步骤。在我们的案例中，我们并没有注意它们。

那如果我们的文件对象抛出一个异常呢？万一我们尝试访问文件对象的一个不支持的方法。举个例子：

```Python
with File('demo.txt', 'w') as opened_file:
    opened_file.undefined_function('Hola!')
```

我们来列一下，当异常发生时，`with`语句会采取哪些步骤。 1. 它把异常的`type`,`value`和`traceback`传递给`__exit__`方法 2. 它让`__exit__`方法来处理异常 3. 如果`__exit__`返回的是True，那么这个异常就被优雅地处理了。 4. 如果`__exit__`返回的是True以外的任何东西，那么这个异常将被`with`语句抛出。

在我们的案例中，`__exit__`方法返回的是`None`(如果没有`return`语句那么方法会返回`None`)。因此，`with`语句抛出了那个异常。

```python
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
AttributeError: 'file' object has no attribute 'undefined_function'
```

我们尝试下在`__exit__`方法中处理异常：

```python
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        print("Exception has been handled")
        self.file_obj.close()
        return True

with File('demo.txt', 'w') as opened_file:
    opened_file.undefined_function()

# Output: Exception has been handled
```

我们的`__exit__`方法返回了`True`,因此没有异常会被`with`语句抛出。

这还不是实现上下文管理器的唯一方式。还有一种方式，我们会在下一节中一起看看。

#### 基于生成器的实现

我们还可以用装饰器(decorators)和生成器(generators)来实现上下文管理器。
Python有个`contextlib`模块专门用于这个目的。我们可以使用一个生成器函数来实现一个上下文管理器，而不是使用一个类。
让我们看看一个基本的，没用的例子：

```Python
from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()
```

OK啦！这个实现方式看起来更加直观和简单。然而，这个方法需要关于生成器、`yield`和装饰器的一些知识。在这个例子中我们还没有捕捉可能产生的任何异常。它的工作方式和之前的方法大致相同。

让我们小小地剖析下这个方法。 1. Python解释器遇到了`yield`关键字。因为这个缘故它创建了一个生成器而不是一个普通的函数。 2. 因为这个装饰器，`contextmanager`会被调用并传入函数名（`open_file`）作为参数。 3. `contextmanager`函数返回一个以`GeneratorContextManager`对象封装过的生成器。 4. 这个`GeneratorContextManager`被赋值给`open_file`函数，我们实际上是在调用`GeneratorContextManager`对象。

那现在我们既然知道了所有这些，我们可以用这个新生成的上下文管理器了，像这样：

```Python
with open_file('some_file') as f:
    f.write('hola!')
```

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

