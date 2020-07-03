# 用golang刷算法--堆排序算法

## 堆排序算法流程

将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。将其与末尾元素进行交换，此时末尾就为最大值。然后将剩余n-1个元素重新构造成一个堆，这样会得到n个元素的次小值。如此反复执行，便能得到一个有序序列了

**大顶堆：arr[i] >= arr[2i+1] && arr[i] >= arr[2i+2]**  

**小顶堆：arr[i] <= arr[2i+1] && arr[i] <= arr[2i+2]** 

## 用golang实现

```go
func HeapSort(intList []int) {
	end := len(intList) - 1
	for end >= 0{
		heap(intList, end)
		intList[0], intList[end] = intList[end], intList[0]
		end--
	}
}

func heap(intList []int, end int) {
	i := end
	// 判断end是否是奇数
	if end%2 == 1 {
		// 比较end和其父亲的大小
		if intList[end] > intList[(end-1)/2] {
			// 和父亲交换位置
			intList[end], intList[(end-1)/2] = intList[(end-1)/2], intList[end]
		}
		i = end - 1
	}
	for ; i > 0; i -= 2 {
		// 判断孩子和父亲的大小
		father := intList[(i-2)/2]
		leftChild := intList[i-1]
		rightChild := intList[i]
		maxIndex := i // 两个孩子中大的一个的下标
		if leftChild > rightChild{
			maxIndex = i-1
		}
		if father < intList[maxIndex] {
			intList[(i-2)/2], intList[maxIndex] = intList[maxIndex], intList[(i-2)/2]
		}
	}
}
```

