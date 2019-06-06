 

## \__init__(self, [...)

类似与构造函数(真正的是\__new\_\_()和\_\_init__()合称为构造函数),可以称其为初始化方法

实例化操作（“调用”类对象）会创建一个空对象。 许多类喜欢创建带有特定初始状态的自定义实例。 为此类定义可能包含一个名为 [`__init__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__init__) 的特殊方法，就像这样:

```python
def __init__(self):
    self.data = []
```

当一个类定义了 [`__init__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__init__) 方法时，类的实例化操作会自动为新创建的类实例发起调用 [`__init__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__init__)。 因此在这个示例中，可以通过以下语句获得一个经初始化的新实例:

```python 
x = MyClass()
```

当然，[`__init__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__init__) 方法还可以有额外参数以实现更高灵活性。 在这种情况下，提供给类实例化运算符的参数将被传递给 [`__init__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__init__)。 例如，:

```python 
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```

## \__new__(cls, [...)

`__new__` 是在一个对象实例化的时候所调用的第一个方法。它的第一个参数是这个类，其他的参数是用来直接传递给 `__init__` 方法。 可以称其为创造函数(我起的名字)

```python 
class A(object):
    def __init__(self):
        print("这里是__init__方法")

    def __del__(self):
        print("这里是__del__方法")

    def __new__(cls):
        print("这里是__new__方法")

a = A()
```

out

```python 
这里是__new__方法
```

注意:

1. 可以看到\__init__和 \_\_del\_\_方法都未被调用,说明对象未被成功创建
2. \__new__()函数里面的参数是***cls***是一个类

如何创建一个对象:

`需要调用并return父类的__new__方法`

示例2:

```python 
class A(object):
    def __init__(self):
        print("这里是__init__方法")

    def __del__(self):
        print("这里是__del__方法")

    def __new__(cls):
        print("这里是__new__方法")
        return object.__new__(cls)

a = A()
```

out:

```python 
这里是__new__方法
这里是__init__方法
这里是__del__方法
```

**使用场景**

创建单例类

```python
class A(object):

    __isinstance = None

    def __new__(cls):
        if not cls.__isinstance:
            cls.__isinstance = object.__new__(cls)
        return cls.__isinstance

a = A()
b = A()
c = A()
print("a", id(a))
print("b", id(b))
print("c", id(c))
```

out:

```python
a 139626091296080
b 139626091296080
c 139626091296080
```

可见每次创建的类都是同一个,这样做可在某些时候减少内存开支.

## \__del__(self, [...)

类似于析构函数

当一个对象在删除的时需要更多的清洁工作的时候此方法会很有用，比如套接字对象或者是文件对象。注意，如果解释器退出的时候对象还存存在，就不能保证 `__del__` 能够被执行.

## \__next__()

[`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 语句会调用容器对象中的 [`iter()`](https://docs.python.org/zh-cn/3/library/functions.html#iter)。 该函数返回一个定义了 [`__next__()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法的迭代器对象，该方法将逐一访问容器中的元素。 当元素用尽时，[`__next__()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 将引发 [`StopIteration`](https://docs.python.org/zh-cn/3/library/exceptions.html#StopIteration) 异常来通知终止 `for` 循环。 你可以使用 [`next()`](https://docs.python.org/zh-cn/3/library/functions.html#next) 内置函数来调用 [`__next__()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法；这个例子显示了它的运作方式:

```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<iterator object at 0x00A1DB50>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
```

##  \__iter__()

 定义一个 [`__iter__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__iter__) 方法来返回一个带有 [`__next__()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法的对象。 如果类已定义了 `__next__()`，则 [`__iter__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__iter__) 可以简单地返回 `self`:

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```

```python 
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s
```

## \__dict__

 模块对象有一个秘密的只读属性 [`__dict__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#object.__dict__)，它返回用于实现模块命名空间的字典；[`__dict__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#object.__dict__) 是属性但不是全局名称。 显然，使用这个将违反命名空间实现的抽象，应当仅被用于事后调试器之类的场合。

## \__str__()

当实现了该方法的类的对象被打印时,输出该方法的return值