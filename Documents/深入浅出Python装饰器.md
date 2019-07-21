## 1.前言

装饰器是Python的特有的语法,刚接触装饰器的同学可能会觉得装饰器很难理解,装饰器的功能也可以不用装饰器实现,但是装饰器无疑是提高你Python代码质量的利器(尤其是使用在一些具有重复功能的场景),是Python程序员的必备技能.下面我将由浅入深的讲解装饰器语法.在学习装饰器前请记住一点.

***装饰器的本质就是函数*** 

## 2.Python函数

既然装饰器是函数,那我们就先从函数说起

Python中的函数很简单,比如:

```Python
def add(a, b):
    return a+b
```

这就是一个标准的函数,有形参有返回值,知道这么多就够了!

## 3.在函数里面定义函数

Python的语法很自由,这使我们可以在函数里面定义一个函数.举个例子:

```Python
def func():
    def inFunc():
        print("---我在里面---")
```

当然这么写那么里面的函数就永远不会被执行.如何让里面的函数执行呢?有两种方法,我相信聪明的你们都已经猜到了!

1.在函数里面调用函数里面定义的函数,请看例子:

```Python
def func():
    def inFunc():
        print("---我在里面---")
    inFunc()
```

这样子当我们在调用func()函数时,就实现了两步:

1. 定义了一个函数inFunc()
2. 调用了刚刚定义的函数

这样就可以执行内部函数了

2.第二种方法就是将内部函数返回给外部变量,用外部变量调用

## 4.返回一个函数

```Python
def func():
    def inFunc():
        print("---我在里面---")
    return inFunc

f = func()

if __name__ == '__main__':
	f()
```

注意返回时不要在函数名后面加`()`,因为加上`()`代表执行这个函数的意思.

上面的代码运行到`f = func()`时因为`func`后面加了`()`就回去执行`func`函数,`func`函数先会定义一个`inFunc`函数,然后没有执行就把刚定义的函数返回,变量`f`接收了`func`返回的函数`f()`就执行了刚刚接收的函数,即`inFunc`函数

## 5.函数作为参数

既然函数里面可以定义函数,函数又可以返回函数,那么函数的参数也可以是函数吗?答案是肯定的,看个例子:

```Python
def func():
    print("---我是函数func---")

def otherFunc(f):
    f()

if __name__ == '__main__':
	otherFunc(func)
```

这个例子很简单,你们可以自己理一下,这里就不在解释了,这个例子只是为了说明Python中函数的参数是可以为函数的.

## 6.把上面的组合起来

其实我们认为高大上的装饰器就是把我上面所说的拼在一个函数里就是装饰器了.

如下所示:

```Python
def myDecorator(func):  # 函数参数
    def inMyDecorator():  # 定义内部函数
        func()  # 调用参数传进来的函数
        print("---我就加了一丢丢新功能---")   

    return inMyDecorator  # 返回内部定义的函数
```

那我们要怎么调用它呢,按照之前的逻辑先要定义一个函数作为上面那个函数的参数吧(其实这就是被装饰的函数)这里定义一个函数`myFunc`如下

```python 
def myFunc():
    print("---这是我的函数---")
```

然后呢?总要用一个变量来接收上面那个函数吧,接收完后总要调用吧.那么总的代码如下:

```Python
def myDecorator(func):  # 函数参数
    def inMyDecorator():  # 定义内部函数
        func()  # 调用参数传进来的函数
        print("---我就加了一丢丢新功能---")

    return inMyDecorator  # 返回内部函数


def myFunc():
    print("---这是我的函数---")


f = myDecorator(myFunc)

if __name__ == '__main__':
	f()
```

输出:

```
---这是我的函数---
---我就加了一丢丢新功能---
```

看!这是不是有点像装饰器的样子了呢!但总感觉有什么不像(装饰器可没有变量`f`),那好吧,把`f`换成`myFunc`就好了吧(虽然他是之前函数名,但我们是可以改变他指向的内存空间的,一句话:用过的名字还是可以再被利用的)

再看:

```Python
def myDecorator(func):  # 函数参数
    def inMyDecorator():  # 定义内部函数
        func()  # 调用参数传进来的函数
        print("---我就加了一丢丢新功能---")

    return inMyDecorator  # 返回内部函数

def myFunc():
    print("---这是我的函数---")

myFunc = myDecorator(myFunc)

if __name__ == '__main__':
    myFunc()
```

输出:

```
---这是我的函数---
---我就加了一丢丢新功能---
```

这下看着舒服多了.

解释一下上面代码的执行过程:

1. 定义了函数`myDecorator`(实际上就是装饰器)
2. 定义了函数`myFunc`(实际上就是被装饰的函数)
3. 执行到`myFunc = myDecorator(myFunc)`
   1. 这里转去执行`myDecorator`函数,并把`myFunc`作为参数传给`myDecorator`函数
   2. `myDecorator`函数的形参`func`接收了实参`myFunc`函数
   3. 在`myDecorator`函数里面定义了一个`inMyDecorator`函数,没有执行这个函数而是把这个函数给返回了
   4. 变量`myFunc`接收了`myDecorator`函数的返回值即`inMyDecorator`函数
4. 调用`myFunc`函数,注意这里的`myFunc`函数已经不是最初定义的那个函数了,而是`inMyDecorator`函数
   1. 执行`myFunc`函数相当于执行`inMyDecorator`函数
   2. 在`inMyDecorator`函数内先调用了 `func`,这个`func`就是第2步定义的函数
      1. 转去执行第2步定义的函数,即打印`"---这是我的函数---"`
   3. 执行到`print("---我就加了一丢丢新功能---")`这句打印`"---我就加了一丢丢新功能---"`
5. 结束

## 7.使用`@`符号

其实Python中为了我们的省力把很多的步骤都用一个`@`符号代替掉了

看一个装饰器的官方写法(使用`@`符号):

```Python
def myDecorator(func):  # 函数参数
    def inMyDecorator():  # 定义内部函数
        func()  # 调用参数传进来的函数
        print("---我就加了一丢丢新功能---")

    return inMyDecorator  # 返回内部函数


@myDecorator
def myFunc():
    print("---这是我的函数---")


if __name__ == '__main__':
    myFunc()
```

其实这段代码的功能和之前的写法是一模一样的.

```Python
@myDecorator
def myFunc():
    print("---这是我的函数---")
```

等价于

```Python
def myFunc():
    print("---这是我的函数---")

myFunc = myDecorator(myFunc)
```

## 8.被装饰的函数带参数

之前写的函数例子都是不带参数的,但是实际上带参数的函数更为常见,那如何向函数传参数呢?仔细想想,`myFunc`函数在被装饰后就是`inMyDecorator`函数.那么只要想办法步参数传给`inMyDecorator`函数不就行了嘛

代码稍作修改(就改了两处):

```Python
def myDecorator(func):  # 函数参数
    def inMyDecorator(*args, **kwargs):  # 定义内部函数
        func(*args, **kwargs)  # 调用参数传进来的函数
        print("---我就加了一丢丢新功能---")

    return inMyDecorator  # 返回内部函数


def myFunc(a):
    print("---这是我的函数参数:{}---".format(a))


myFunc = myDecorator(myFunc)

if __name__ == '__main__':
    myFunc("kainhuck")
```

输出:

```
---这是我的函数参数:kainhuck---
---我就加了一丢丢新功能---
```



## 9.没想到你坚持看到了这里

希望看完这篇文章后你能写一个自己的装饰器,后续我会继续更新,参数的装饰器,和用类写一个装饰器.觉得有帮助请点个推荐吧.

往期精彩:[提升Python编程效率的几种方法](https://www.cnblogs.com/kainhuck/p/10987747.html)

## 10.一些装饰器代码

### 规定函数参数

```Python
def require_ints(decorated):
    def inner(*args, **kwargs):
        kwarg_values = [i for i in kwargs.values()]
        for arg in list(args) + kwarg_values:
            if not isinstance(arg, int):
                raise TypeError('%s only accepts intergers as argument.' % decorated.__name__)

        return decorated(*args, **kwargs)

    return inner


@require_ints
def foo(x, y):
    return x + y


if __name__ == '__main__':
    result = foo(1, "das")
    print(result)
```

### 函数注册表

```Python
registry = []


def register(func):
    registry.append(func)
    return func


@register
def foo():
    return 123

@register
def bar():
    return 321

if __name__ == '__main__':
    for func in registry:
        a = func()
        print(a)
```

注意上面装饰器的定义,如定义成下面这样会有什么不同

```Python
def register(func):
    def inner():
        registry.append(func)
        return func

    return inner
```

### 记录日志

```Python
import functools
import logging
import time


def logged(func):
    @functools.wraps(func)
    def inner(*arg, **kwargs):
        start = time.time()
        return_value = func(*arg, **kwargs)
        end = time.time()
        delta = end - start

        logger = logging.getLogger('decorator.logged')
        logger.warn('Called method %s at %.2f; execution time %.2f second; result %r.' % (func.__name__, start, delta,
                    return_value))

        return return_value

    return inner


@logged
def add(x, y):
    return x + y


if __name__ == '__main__':
    add(1, 2)
```

### 传参数的装饰器也可以不传参数使用

```Python
import functools


def outSide(decorated_=None, num=1):
    def actual_decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            print(num)
            return func(*args, **kwargs)

        return inner

    if decorated_:
        return actual_decorator(decorated_)
    else:
        return actual_decorator


@outSide(num=2333)
def add(x, y):
    return x + y


@outSide
def sub(x, y):
    return x - y


if __name__ == '__main__':
    print(add(1, 2))
    print(sub(2, 1))
```

### 装饰类

```Python
import functools
import time

def sortable_by_creation_time(cls):
    # 保存类的__init__方法
    original_init = cls.__init__

    @functools.wraps(original_init)
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self._created = time.time()

    cls.__init__ = new_init

    cls.__lt__ = lambda self, other: self._created < other._created
    cls.__gt__ = lambda self, other: self._created > other._created

    return cls

@sortable_by_creation_time
class Sortable(object):
    def __init__(self, identifier):
        self.identifier = identifier

    def __repr__(self):
        return self.identifier


first = Sortable("first")
second = Sortable("second")
third = Sortable("third")

sortables = [second, first, third]

print(sorted(sortables))
```

