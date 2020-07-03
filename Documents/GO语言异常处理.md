# 对比其他语言

其他语言比如Python用的是`try Except finally`的方式来进行异常处理,执行逻辑是:尝试执行一段代码,如果发生异常则执行...无论是否发生异常都执行...;相比起来go语言的异常处理就简单许多,因为程序中的异常基本上都是可预期的,所以GO语言处理异常的方式是返回这个异常,如果没有发生异常则该值为nil,只要判断这个预期的返回值是否是`nil`便知道有没有异常发生.go语言中还有一种`panic`机制,`panic`可以理解为致命的异常会中断程序的运行,但是通过`recover`函数可捕获这个`panic`让程序继续运行.

# error

GO语言中一个普通的错误被称为error,它本质是一个接口类型,可以在`builtin.go`中看到其定义

```go
// The error built-in interface type is the conventional interface for
// representing an error condition, with the nil value representing no error.
type error interface {
	Error() string
}
```

error可以出现在很多地方,比如打开一个不存在的文件,还有数学运算错误等等.

例子:

```go
package main

import (
	"fmt"
	"os"
)

type people interface {
	name() string
}

func main() {
	_, err := os.Open("不存在.go")
	if err != nil {
		fmt.Println(err)	// open 不存在.go: no such file or directory
	}
}
```

# 创建error

前面我们获得error的方法是接受别人写好函数的返回值,现在我们尝试自己创建一个error,

在errors包中有多个创建error的方法,其中最常用的是errors.New()方法,该方法接收一个字符串用于描述这个错误.

其实现如下:

```go
// New returns an error that formats as the given text.
// Each call to New returns a distinct error value even if the text is identical.
func New(text string) error {
	return &errorString{text}
}

// errorString is a trivial implementation of error.
type errorString struct {
	s string
}

func (e *errorString) Error() string {
	return e.s
}
```

New方法返回了一个errorString结构体并将参数text穿进这个结构体中,这个结构体因为实现了Error方法所以他是一个error类型.

利用errors.New方法创建新error的例子:

```go
package main

import (
	"errors"
	"fmt"
)

func main() {
	err := errors.New("我自己创建的一个错误")
	fmt.Println(err) // 我自己创建的一个错误
}
```

除了errors.New()方法创建error外,还可以用fmt.Errorf函数创建新的error,让我们看看fmt.Errorf函数内部的实现:

```go
func Errorf(format string, a ...interface{}) error {
	p := newPrinter()
	p.wrapErrs = true
	p.doPrintf(format, a)
	s := string(p.buf)
	var err error
	if p.wrappedErr == nil {
		err = errors.New(s)
	} else {
		err = &wrapError{s, p.wrappedErr}
	}
	p.free()
	return err
}
```

在`var err error`之前的语句看不懂没关系, 我简单的说一下:创建了一个pp结构体指针,然后设置了wrapErrs为true,并调用doPrintf方法将我们的格式化输入转化成对应字符串,此时还存在p的缓冲区中,然后通过string进行类型转化将得到的字符串村进变量s.关键看那个判断语句,这说明,Errorf函数生成错误有两种方式,要么调用errors.New要么返回一个wrapError类型实例.errors.New已经介绍过,下面看看wrapError结构体:

```go
type wrapError struct {
	msg string
	err error
}

func (e *wrapError) Error() string {
	return e.msg
}
```

相信大家都能明白了吧

举个fmt.Errorf的例子

```go
package main

import (
	"fmt"
)

func main() {
	err := fmt.Errorf("error error error")
	fmt.Println(err) // error error error
}
```



# 番外篇 String() 和 Error()

在golang中如果直接打印一个普通对象,得到的结果就会向下面一样,

```go
package main

import "fmt"

type People struct {
	name string
	age  int
}

func main(){
	p := &People{
		name: "horika",
		age:  10,
	}
	fmt.Println(p) // &{horika 10}
	fmt.Printf("%s\n", p) // &{horika %!s(int=10)}
}
```

也许有时候我们需要在打印或者转换成字符串时想要让他输出自定义的一句话,这时我们可以给这个结构体增加一个`String`方法,如下:

```go
package main

import "fmt"

type People struct {
	name string
	age  int
}

func (p *People) String() string{
	return fmt.Sprintf("我叫%s, 我今年%d岁", p.name, p.age)
}

func main(){
	p := &People{
		name: "horika",
		age:  10,
	}
	fmt.Println(p)	// 我叫horika, 我今年10岁
	fmt.Printf("%s\n", p) // 我叫horika, 我今年10岁
}
```

**!!!** 注意如果我们定义的String方法是指针调用的那么我们必须打印指针对象才有效果,也就是你定义什么类型,就打印什么类型,同学们可以自己去尝试.

如果我们的结构体定义了一个`Error`方法,那么打印的时候会优先调用`Error`方法,如下

`只定义Error方法的例子`:

```go
package main

import "fmt"

type People struct {
	name string
	age  int
}

func (p *People) Error() string{
	return fmt.Sprintf("[Error] 我叫%s, 我今年%d岁", p.name, p.age)
}

func main(){
	p := &People{
		name: "horika",
		age:  10,
	}
	fmt.Println(p)	// [Error] 我叫horika, 我今年10岁
	fmt.Printf("%s\n", p) // [Error] 我叫horika, 我今年10岁
}
```

`即有String方法也有Error方法`

```go
package main

import "fmt"

type People struct {
	name string
	age  int
}

func (p *People) String() string{
	return fmt.Sprintf("[String] 我叫%s, 我今年%d岁", p.name, p.age)
}

func (p *People) Error() string{
	return fmt.Sprintf("[Error] 我叫%s, 我今年%d岁", p.name, p.age)
}

func main(){
	p := &People{
		name: "horika",
		age:  10,
	}
	fmt.Println(p)	// [Error] 我叫horika, 我今年10岁
	fmt.Printf("%s\n", p) // [Error] 我叫horika, 我今年10岁
}
```

可以看到如果Error和String方法同时存在,Error方法会覆盖String方法,

看到这里我想你们就应该明白为什么我们之前打印一个error时只需要打印它本身而不用打印err.Error()了吧

# 定义自己的错误

看了前面的介绍我相信大家都能自己写一个错误类型,无非分两步,1. 定义一个结构体,2. 该结构体实现 `Error() string`方法.然而事实真的就是这么简单.其实在前面的番外篇里已经有了自定义错误的影子

举个例子

```go
package main

import "fmt"

type MyIntNegativeError struct {
	msg string
	val int
}

func (m *MyIntNegativeError)Error() string{
	return fmt.Sprintf("[ERROR] reason %s; val: %d", m.msg, m.val)
}

func NewMyIntNegativeError(msg string, val int) *MyIntNegativeError{
	return &MyIntNegativeError{
		msg: msg,
		val: val,
	}
}

func Sub10(a int) (int, error){
	ret := a - 10

	if ret < 0 {
		return 0, NewMyIntNegativeError("a必须大于10", a)
	}

	return ret, nil
}

func main(){
	a := 9

	ret, err := Sub10(a)
	if err != nil {
		fmt.Println("出错啦", err)	// 出错啦 [ERROR] reason a必须大于10; val: 9
		return
	}
	fmt.Println(ret)
}
```

除了必须实现`Error`方法外,我一般习惯给自定义的错误实现一个构造函数.

# panic和recover

## panic

panic是一个内建函数,他会产生一个严重的错误使程序中断执行,举个例子

```go
package main

import "fmt"

func main(){
	for i:=1;i<10;i++{
		fmt.Println(i)
		if i%3 == 0{
			panic("出现数字3的倍数,我不想继续了")
		}
	}
}
```

输出

```
1
2
3
panic: 出现数字3的倍数,我不想继续了

goroutine 1 [running]:
main.main()
        /home/kain/Documents/code/go_module/file_io/main.go:9 +0xf5

```

## recover

recover可以捕获一个panic使程序恢复运行,当然你也可以再次抛出异常,通常我们都是在defer语句中执行recover,这很容易理解,因为我们必须等所有程序都执行完才能保证整个过程不会发生panic,举个例子

```go
package main

import "fmt"

func main(){
	f1()
}

func f1(){
	defer func() {
		pan := recover()
		if pan != nil{
			fmt.Println("我已经捕获了错误,错误是:", pan)
			fmt.Printf("错误类型是%T\n", pan)
		}else{
			fmt.Println("没有错误")
		}
	}()
	for i:=1;i<10;i++{
		fmt.Println(i)
		if i%3 == 0{
			panic("出现数字3的倍数,我不想继续了")
		}
	}
}
```

输出

```
1
2
3
我已经捕获了错误,错误是: 出现数字3的倍数,我不想继续了
错误类型是string
```



以上就是golang的异常处理机制