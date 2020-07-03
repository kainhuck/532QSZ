# 用python刷算法--归并排序算法

## 归并排序算法流程

并归排序采用的是分治的思想,先将乱序的数组逐级拆分成一个个小部分,最底层每个部分长度为一(各个部分视为有序),然后在将有序的部分按照完全二叉树两两合并逐级往上,直到排序结束

参考如下图片(来源:https://www.cnblogs.com/chengxiao/p/6194356.html)

![img](https://images2015.cnblogs.com/blog/1024555/201612/1024555-20161218163120151-452283750.png)

每部分的合并规则如下:

![img](https://images2015.cnblogs.com/blog/1024555/201612/1024555-20161218194508761-468169540.png)

## 用python实现

```python
def mergeSort(intList: list) -> list:
    length = len(intList)
    # 长度为1直接返回
    if length <= 1:
        return intList

    # 先分
    middle = int(length / 2)
    left = mergeSort(intList[:middle])
    right = mergeSort(intList[middle:])

    # 后治
    return merge(left, right)


def merge(left: list, right: list) -> list:
    leftLen = len(left)
    rightLen = len(right)
    # 定义i, j指向左右列表的开始
    i, j = 0, 0
    # 定义临时列表
    temp = []

    while i < leftLen and j < rightLen:
        if left[i] < right[j]:
            # 将左边的值放入temp中
            temp.append(left[i])
            # i++
            i += 1
        else:
            # 将右边的值放入temp
            temp.append(right[j])
            # j++
            j += 1

    # 结束循环后会多有一个列表有余
    if i < leftLen:
        temp = temp+left[i:]
    elif j < rightLen:
        temp = temp + right[j:]

    return temp
```

