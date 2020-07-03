# 用python刷算法--堆排序算法

## 堆排序算法流程

将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。将其与末尾元素进行交换，此时末尾就为最大值。然后将剩余n-1个元素重新构造成一个堆，这样会得到n个元素的次小值。如此反复执行，便能得到一个有序序列了

**大顶堆：arr[i] >= arr[2i+1] && arr[i] >= arr[2i+2]**  

**小顶堆：arr[i] <= arr[2i+1] && arr[i] <= arr[2i+2]** 

## 用python实现

```go
def heapSort(intList: [int]) -> None:
    end = len(intList) - 1
    while end >= 0:
        # 进行大顶堆的构造
        heap(intList, end)
        # 交换第一个与最后一个的位置
        intList[0], intList[end] = intList[end], intList[0]
        end -= 1


def heap(intList: [int], end: int) -> None:
    i = end
    # 判断end是否是孤立
    if end % 2:
        # 孤立
        # 判断end和父元素的大小
        if intList[int((end-1)/2)] < intList[end]:
            intList[int((end-1)/2)
                    ], intList[end] = intList[end], intList[int((end-1)/2)]
        i = end-1

    while i > 0:
        # 判断两个孩纸节点和父元素的大小
        father = intList[int((i-2)/2)]
        leftChild = intList[i-1]
        rightChild = intList[i]
        maxIndex = i if rightChild > leftChild else i-1
        if father < intList[maxIndex]:
            intList[int(
                (i-2)/2)], intList[maxIndex] = intList[maxIndex],  intList[int((i-2)/2)]
        i -= 2
```

