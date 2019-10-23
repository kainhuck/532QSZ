## 先看下面的代码

```python
testList = [
    '+a+',
    '+b+',
    '*a*',
    '*b*'
]

for each_word in testList:
    if 'b' in each_word:
        print(each_word)
    if 'a' in each_word:
        testList.remove(each_word)  # pop(testList.index(each_word))    同理
```

你以为上面的代码会输出如下：

```
+b+
*b*
```

**但实际上什么也不会输出！！！**

解释一下为什么：

当循环到第0个位置时`each_word`为`'+a+'`会触发第二个条件，`'+a+'`将会从列表中删除，紧接着**python会循环第1个位置而不是下一个值**，此时由于`'+a+'`被删除，后面的所有元素会向前移一位，所以第1个位置是`*a*`，**而`'+b+'`成为了第0个位置所以被跳过了**，后面同理

