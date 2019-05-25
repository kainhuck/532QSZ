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

### 1.生成器（Generators）

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

### 5.装饰器

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

