# 谈谈golang中的channel

在golang中channel用于`goroutine`之间的通信,在阅读这篇文章之前,我已经默认你已经熟悉了(至少了解了)goroutine

## 1. channel的定义

channel是引用类型,需要实用make来创建channel,如下

`make(chan Type, [buffer])`

make对于channel接收两个参数,第一个是通道的类型,第二个是个可选参数代表通道缓冲区的大小(省略代表无缓冲),比如创建一个用于传递`int`类型的通道可以如下定义:

```go
make(chan int)	// 无缓冲
make(chan int, 2) // 带有两个缓冲的通道
```

*要想使用通道必须make! 以下的种种操作都是基于已经make后的channel,不再讨论由于通道没有make而引起的低级错误*

## 2. channel的操作

### 1. 向channel中放入元素

- 我们可以使用`<-`符号指向`channel`来将元素放入channel中

- *注意向通道中传值必须要求该通道还有容量(缓冲),而且通道不能关闭*

- *对于无缓冲的或者缓冲已经满了的channel不可以轻易的传入值,必须要有goroutine同时在取元素才可以放入*

**向一个有缓冲,非满的channel传值**

```go
c := make(chan int, 1) // 定义一个带有一个缓冲的通道
c <- 1				   // 向通道中传入一个1,正常
```

**向一个有缓冲,满的channel传值**

```go
c := make(chan int, 1) // 定义一个带有一个缓冲的通道
c <- 1				   // 向通道中传入一个值,这个值传入后填满了该通道
c <- 2                 // 再向通道中传入一个值,报错!!!!!!!!!!!!!!!!!!!!!!!!!!!
```

**向一个无缓冲,的channel传值**

```go
c := make(chan int) // 定义一个无缓冲通道
c <- 1              // 向无缓冲通道传值,报错!!!!!!!!!!!!!!!!!!!!!!!!!!!!
```

其实上述两种错误均是由于通道满了而引起的(无缓冲的通道可以看成是缓冲为0的通道),解决方法很简单,只要保证有个goroutine同时在从该通道中取值即可,我这里针对`向一个有缓冲,满的channel传值`给出解决思路

```go
package main

import (
	"fmt"
	"sync"
	"time"
)

var wg sync.WaitGroup

func main() {
	c := make(chan int, 1)

	c <- 1  // 因为我们定义的通道带有一个缓冲,
	        // 所以在发布任务之前允许存在最多一个任务投递,也可以写在发布任务之后

	// for循环用于发布任务
	for i := 0; i < 2; i++ {
		wg.Add(1)
		go doWork(c)	// 如果通道现在是空的 goroutine会等待,
		                // 如果检测到现在是空的且没有任务投递,就会报错
	}

	c <- 2	// 多余的任务投递必须在任务发布之后

	wg.Wait()
}

func doWork(i chan int) {
	defer wg.Done()
	a := <-i
	fmt.Printf("%d号开始工作了\n", a)
	time.Sleep(time.Second * 2) // 模拟耗时
	fmt.Printf("%d号结束工作了,输出:%d\n", a, a)
}
```

对于空channel传值报错的解决思路就留给读者了



### 2. 从channel中取出元素

- 我们可以使用`<-`符号指向`变量`来将channel中的元素放`变量`中

  此时可以接收两个值一个数值一个状态

  ```go
  v, ok := <-c   // c是通道,v是取到的值,ok是状态,正常时是true,从关闭的空通道取值是false
  ```

- 可以通过`range`取值

- *注意从通道中取值必须要求该通道还有值*

- *对于无缓冲的或者缓冲已经空了的channel不可以轻易的取出值,必须要同时在放元素才可以取出*

- 可以向已经关闭的通道取值

**ok为true的例子**

```go
c := make(chan int, 1)
c <- 1
a, ok := <-c
fmt.Println(a, ok)  // 输出 1 true
```

**ok为false的例子**

```go
c := make(chan int, 1)
close(c)
a, ok := <-c
fmt.Println(a, ok)  // 输出 0 false
```

**ok的应用--循环取值**

```go
for {
    v, ok := <- c
    if !ok {
        break
    }
    fmt.Println(v)
}
```

**range取值**

```go
func main() {
	c := make(chan int, 10)
	for i:=0; i< 10; i++ {
		c <- i
	}
	close(c)

	for v := range c{
		fmt.Println(v)
	}
}
```

**向一个有缓冲,非空的channel取值**

```go
c := make(chan int, 1) // 定义一个带有一个缓冲的通道
c <- 1				   // 向通道中传入一个1,使通道非空
i := <-c			   // 从通道中取出一个值赋给变量i
// 如果只是想取出值而不想对该值做任何其他操作,可以这么写    <-c   左边省略接收者
```

**向一个有缓冲,空的channel取值**

```go
c := make(chan int, 1) // 定义一个带有一个缓冲的通道
<-c                    // 向空通道中取出一个值,报错!!!!!!!!!!!!!!!!!!!!!!!!!!!
```

**向一个无缓冲,的channel取值**

```go
c := make(chan int) // 定义一个无缓冲通道
<-c                 // 向无缓冲通道取值,报错!!!!!!!!!!!!!!!!!!!!!!!!!!!!
```

其实上述两种错误均是由于通道空了而引起的(无缓冲的通道可以看成是缓冲为0的通道),解决方法很简单,只要保证同时在从该通道中存值即可,我这里针对`向一个有缓冲,空的channel取值`给出解决思路

```go
package main

import (
	"fmt"
	"sync"
	"time"
)

var wg sync.WaitGroup

func main() {
	c := make(chan int, 1)
	wg.Add(1)
	go doWork(c)
	<-c			// 取值必须在放值之后
	wg.Wait()
}

func doWork(i chan int) {
	defer wg.Done()
	fmt.Printf("goroutine开始工作了\n", )
	time.Sleep(time.Second * 2) // 模拟耗时
	i <- 1
	fmt.Printf("goroutine结束工作了,放入:%d\n", 1)
}
```

对于空channel取值报错的解决思路就留给读者了



### 3. 关闭通道

对于一个通道我们可以使用`close`内置函数来进行关闭,关闭后的通道具有以下特点

- 向一个已经关闭的通道发送值是不允许的,会报错
- 从一个已经关闭但是里面还有值的通道取值是允许的,可以正常获取到值
- 从一个已经关闭但是为空的通道取值是允许的,会获取通道类型元素的零值
- 不可以再次关闭一个已经关闭的通道,会报错
- 已经关闭的通道无法再次打开

**例子1: 向一个已经关闭的通道发送值**

```go
c := make(chan int, 1)
close(c)
c <- 1		// 报错!!!!!!!!!!!
```

**例子2: 从一个已经关闭但是里面还有值的通道取值**

```go
c := make(chan int, 1)
c <- 1
close(c)
a := <-c
fmt.Println(a)	// 输出 1
```

**例子3: 从一个已经关闭但是为空的通道取值**

```go
c := make(chan int, 1)
close(c)
a := <-c
fmt.Println(a)  // 输出 0 
```

**例子4: 关闭一个已经关闭的通道**

```go
c := make(chan int, 1)
close(c)
close(c) // 报错: panic: close of closed channel
```



## 3. 单向通道

- 在函数中使用通道时我们可以限制其为只读通道或者只写通道

**定义只读通道的例子**

```go
func doWork(i <-chan int) {
	<-i		 // 只能取值
	//i <- 1 // 存值操作将不被允许
}
```

**定义只写通道的例子**

```go
func doWork(i chan <- int) {
	i <- 1      // 只能存值
	//<-i		// 取值操作将不被允许
}
```





```go
func main() {
	c := make(chan int, 10)

	wg.Add(2)

	// 开一个go程循环存值
	go func(c chan int) {
		defer wg.Done()
		for i:=0; i< 10; i++ {
			c <- i
		}
		close(c)
	}(c)

	// 开一个go程循环取值
	go func(c chan int) {
		defer wg.Done()
		for {
			v, ok := <- c
			if !ok {
				break
			}
			fmt.Println(v)
		}
	}(c)

	wg.Done()
}
```





