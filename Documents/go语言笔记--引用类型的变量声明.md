# 谈谈golang中的引用类型与地址分配

go语言中的`引用类型`(我更愿意称其为`指向类型`)其实就是`存放地址的类型`,比如`slice`,`map`,`channel`,和其他指针类型(`*int`...)

要实用这些(存放地址的)类型之前就必须要为其分配`内存`.下面我一一举例说明一下(以下操作均在函数内部操作,意味着可以使用`:=`来声明定义变量)

## 1. 值类型的指针形式

*以int为例*

- 一个错误的例子

  ```go
  var i *int
  *i = 1
  ```

  panic: runtime error: invalid memory address or nil pointer dereference

  错误原因,i为指针变量,但是未被分配地址就试图操作其内容

- 解决方法(写法一)

  ```go
  var i *int
  i = new(int)
  *i = 1
  ```

- 解决方法(写法二)

  ```go
  i := new(int)
  *i = 1
  ```

- new函数

  new函数用于给本身不带有指针类型的类型带上指针,这话是我给出的解释,说白了就是输入`值类型`返回`该类型的指针`.new函数可以分配内存并且初始化为零值.这是他的函数定义:`func new(Type) *Type`

## 2. Slice

slice本身就是一个带指针的类型(引用类型),所以使用他之前必须分配地址,但他比较特殊,由于`append`函数的功能,我们几乎不会遇到`slice`内存未分配的函数,更多的是遇到下标越界

- 声明时为分配内存的例子一

  ```go
  var s []int	// 定义一个存放int的切片,未分配内存
  s[0] = 1 // 报错,panic: runtime error: index out of range [0] with length 0
  ```

- 声明时为分配内存的例子二

  ```go
  var s []int // 定义一个存放int的切片,未分配内存
  s = append(s, 1) // 未报错
  ```

  有些人可能会感到奇怪,这里明明没有分配内存怎么可以使用slice而不报错,原因就是,append函数会自动分配内存(其实就是扩容策略,没有发生下标越界错误也是因为扩容策略),这是append函数的文档:

  ```go
  // The append built-in function appends elements to the end of a slice. If
  // it has sufficient capacity, the destination is resliced to accommodate the
  // new elements. If it does not, a new underlying array will be allocated.
  // Append returns the updated slice. It is therefore necessary to store the
  // result of append, often in the variable holding the slice itself:
  //	slice = append(slice, elem1, elem2)
  //	slice = append(slice, anotherSlice...)
  // As a special case, it is legal to append a string to a byte slice, like this:
  //	slice = append([]byte("hello "), "world"...)
  func append(slice []Type, elems ...Type) []Type
  ```

- make函数对于slice

  make函数是用于对`slice`,`map`,`channell`专属的内存分配函数,它的返回值是类型本身,因为这三种类型本身带有指针,另外make函数对这三种类型有智能的判断,对slice来说,make函数是这种样子`make(sliceType, length int, capacity int)sliceType`,它接受三个参数,分别是切片类型,长度,和容量,其中容量可以省略(和length相同),如果length大于0, 则已经被分配的空间会先存放类型零值.

- 声明时分配内存的写法一

  ```go
  var s []int
  s = make([]int,0)
  fmt.Println(s) // []
  
  var s []int
  s = make([]int,3)
  fmt.Println(s) // [0 0 0]
  ```

- 声明时分配内存的写法二

  ```go
  s := make([]int, 2)
  ```

- 不使用make函数分配内存的写法

  ```go
  s := []int{}
  ```

  这种写法只能用于`:=`,其实就是通过`{}`来事先初始化,已经初始化了,肯定也就分配内存了,只不过上面的写法是初始化为空的初始化,再举个例子更好的帮大家理解一下

  ```go
  s := []int{1,2,3}
  ```

## 3. map

如slice一样,map也是一个带指针的类型(引用类型)

- 一个错误的例子

  ```go
  var m map[string]interface{}
  m["age"] = 1
  ```

  panic: assignment to entry in nil map

  错误原因:map是引用类型,未分配内存便尝试操作其中的内容

- make函数对于map

  和slice不同,make函数对于map是这样子的`make(mapType, capacity int)mapType`,它只接受两个参数分别是map类型和容量,如果传递多个参数会编译时报错,和slice一样capacity可以被省略.**值得注意的是虽然第二个值是容量,但是map并不能使用`cap`函数获取其容量,而且通过`len`函数获得是map的长度而不是容量**,举个例子说明一下

  ```go
  m := make(map[string]interface{}, 10)
  fmt.Println(len(m)) // 0
  m["name"] = "horika"
  // fmt.Println(cap(m))  // panic
  fmt.Println(len(m)) // 1
  ```

- 通过make函数给map分配内存写法一

  ```go
  var m map[string]string
  m = make(map[string]string, 1) // 容量可以被省略 m = make(map[string]string)
  ```
  
- 通过make函数给map分配内存写法二

  ```go
  m := make(map[string]int)
  ```

- 不通过make函数分配内存的写法

  ```go
  m := map[int][int]{}
  ```

  原理和slice的这种写法一样,通过`:=`和`{}`来进行初始化,一旦被初始化了,也就被分配内存了.举个初始化不为空的例子:

  ```go
  m := map[int]int{
  	1: 1,
  }
  ```

## channel

在go语言中channel是为了`goroutine`的通信,他也是一种引用类型.`channel`的使用必须通过`make`函数分配内存.

- 一个错误的例子一

  ```go
  var c chan int // 定义一个传递int的通道
  go printI(c)   // 尝试向一个为分配内存的通道取值; 这是事先定义的接收一个int通道的函数,
  			   // 如果没有这一句下面的操作会堵塞,因为为分配的通道肯定是没有缓冲的
  c <- 1		   // 尝试向一个没有分配内存的通道传值
  ```

  无论是传值还是取值都会报错

  goroutine 1 [chan send (nil chan)]:

  goroutine 18 [chan receive (nil chan)]:

- 一个错误的例子二

  ```go
  var c chan int // 定义一个传递int的通道
  close(c)	   // 尝试关闭一个没有分配内存的通道
  ```

  panic: close of nil channel

  如果关闭一个没有没有分配内存的通道也会报错

- make函数对于channel

  与以上两种类型都不同make函数对于channel是这样的`make(chanType, buffer int)chanType`,它接收两个参数,第一个是通道的类型,第二个是缓冲大小(省略则是无缓冲通道).

- 改正上述例子

  ```go
  c := make(chan int)
  go printI(c)
  c <- 1
  close(c)
  ```

  或者

  ```go
  var c chan int
  c = make(chan int)
  go printI(c)
  c <- 1
  close(c)
  ```

  当然如果带有缓冲,传值时就不怕阻塞了

  ```go
  c := make(chan int, 1)
  c <- 1
  close(c)
  ```

  

