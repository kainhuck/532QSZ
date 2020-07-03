# 用python刷算法--快速排序算法

## 快速排序算法流程

1. 选定一个基准值(任意选,以第一个为例)
2. 定义左右指针指向左右两端
3. 左指针往右移动,如果遇到大于基准值的数就把它和右指针的值调换位置,然后左指针不动,右指针开始向左移动,如果遇到小于基准值的数就把他和左指针的值调换位置,然后开始移动左指针,以此类推,知道左右指针相遇
4. 递归上述过程知道排序结束

## 用python实现

```python
def quickSort(intList: list) -> list:
    # 如果长度小于等于1就结束
    if len(intList) <= 1:
        return intList

    # 1. 将第一个值选为基准值
    flag = intList[0]
    # 定义左右指针
    left, right = 0, len(intList) - 1

    i = 1
    while i <= right:
        if intList[i] > flag:
            intList[i], intList[right] = intList[right], intList[i]
            right -= 1
        else:
            intList[i], intList[left] = intList[left], intList[i]
            left += 1
            i += 1

    # 传列表的切片不会改变本身变量所以需要返回
    leftList = quickSort(intList[:left])
    rightList = quickSort(intList[left+1:])
    return leftList + [flag] + rightList
```

