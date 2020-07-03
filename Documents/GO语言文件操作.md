# GO语言文件操作

# 获取文件信息

## FileInfo接口

在`os`包中有一个`FileInfo`接口它包含了一个文件的基本信息,如下

```go
// A FileInfo describes a file and is returned by Stat and Lstat.
type FileInfo interface {
	Name() string       // base name of the file
	Size() int64        // length in bytes for regular files; system-dependent for others
	Mode() FileMode     // file mode bits
	ModTime() time.Time // modification time
	IsDir() bool        // abbreviation for Mode().IsDir()
	Sys() interface{}   // underlying data source (can return nil)
}
```

从上面描述可以看到FileInfo描述一个文件并且被Stat和Lstat方法返回

从`os`包中可以看到这两个函数的定义,记住里面的两个函数`statNolog`和`lstatNolog`

```go
// Stat returns a FileInfo describing the named file.
// If there is an error, it will be of type *PathError.
func Stat(name string) (FileInfo, error) {
	testlog.Stat(name)
	return statNolog(name)
}

// Lstat returns a FileInfo describing the named file.
// If the file is a symbolic link, the returned FileInfo
// describes the symbolic link. Lstat makes no attempt to follow the link.
// If there is an error, it will be of type *PathError.
func Lstat(name string) (FileInfo, error) {
	testlog.Stat(name)
	return lstatNolog(name)
}
```



## fileStat结构体

同样在os包中定义了`fileState`结构体

```go
// A fileStat is the implementation of FileInfo returned by Stat and Lstat.
type fileStat struct {
	name    string
	size    int64
	mode    FileMode
	modTime time.Time
	sys     syscall.Stat_t
}
```

在`types_unix.go`文件中定义了如下方法

```go
func (fs *fileStat) Size() int64        { return fs.size }
func (fs *fileStat) Mode() FileMode     { return fs.mode }
func (fs *fileStat) ModTime() time.Time { return fs.modTime }
func (fs *fileStat) Sys() interface{}   { return &fs.sys }
```

在`types.go`中还定义以下两个方法

```GO
func (fs *fileStat) Name() string { return fs.name }
func (fs *fileStat) IsDir() bool  { return fs.Mode().IsDir() }
```

可以看到这个结构体刚好实现了`FileInfo`接口

实际上,进入`statNolog`和`lstatNolog`可知,`Stat`和`Lsate`函数就是返回了指向`fileStat`的指针

```go
// statNolog stats a file with no test logging.
func statNolog(name string) (FileInfo, error) {
	var fs fileStat
	err := syscall.Stat(name, &fs.sys)
	if err != nil {
		return nil, &PathError{"stat", name, err}
	}
	fillFileStatFromSys(&fs, name)
	return &fs, nil
}

// lstatNolog lstats a file with no test logging.
func lstatNolog(name string) (FileInfo, error) {
	var fs fileStat
	err := syscall.Lstat(name, &fs.sys)
	if err != nil {
		return nil, &PathError{"lstat", name, err}
	}
	fillFileStatFromSys(&fs, name)
	return &fs, nil
}
```

所以本质上就是利用`fileStat`结构体存放文件相关信息,并做操作



## 查看文件信息

介绍了这么多,写一个golang读取文件信息的例子,(当前目录下的go.mod文件)

```go
package main

import (
	"fmt"
	"os"
)

func main() {
	fileInfo, err := os.Stat("go.mod")
	if err != nil {
		println("读取文件出错")
		return
	}
	fmt.Println("文件名:", fileInfo.Name())
	fmt.Println("文件大小:", fileInfo.Size())
	fmt.Println("文件权限:", fileInfo.Mode())
	fmt.Println("文件修改时间:", fileInfo.ModTime())
	fmt.Println("文件是否是目录:", fileInfo.IsDir())
}
```

输出

```
文件名: go.mod
文件大小: 24
文件权限: -rw-r--r--
文件修改时间: 2020-06-16 09:04:23.418186928 +0800 CST
文件是否是目录: false
```

其实上面方法就是对应`FileInfo`接口中的方法，但是少了一个`Sys`方法，通过这个方法你可以获得更加详细的信息，这个比较特殊，如果你直接打印会得到类似如下的输出：

```go
fmt.Println(fileInfo.Sys())
// &{2064 23337987 1 33188 1000 1000 0 0 24 4096 8 {1592269464 801520234} {1592269463 418186928} {1592269463 418186928} [0 0 0]}
```

其实`Sys`方法就是返回了`fileStat`的`sys`属性,上面我们已经看过`fileStat`的定义,可以发现`sys`属性就是一个`syscall.Stat_t`类型

这是`Stat_t`的定义

```go
type Stat_t struct {
	Dev       uint64
	Ino       uint64
	Nlink     uint64
	Mode      uint32
	Uid       uint32
	Gid       uint32
	X__pad0   int32
	Rdev      uint64
	Size      int64
	Blksize   int64
	Blocks    int64
	Atim      Timespec
	Mtim      Timespec
	Ctim      Timespec
	X__unused [3]int64
}
```

可以通过反射来获取上述属性的信息,以获取 Ctim 为例:

```GO
package main

import (
	"fmt"
	"os"
	"reflect"
)

func main() {
	fileInfo, err := os.Stat("go.mod")
	if err != nil {
		println("读取文件出错")
		return
	}

	Ctim := reflect.ValueOf(fileInfo.Sys()).Elem().FieldByName("Ctim").Field(0)
	fmt.Println(Ctim) // 1592269463
}
```

## 文件路径

也许有人会奇怪,为什么`fileStat`结构体里没有文件路径相关信息,其实者不难理解,我们既然能够打开一个文件,前提就是我们知道这个文件放在哪里.而我接下来要做的操作知识针对文件路径,而不是文件本身.

针对路径golang中有一个专门的包`path`

常用方法如下

| 方法名           | 功能               |
| ---------------- | ------------------ |
| filepath.IsAbs() | 判断是否为绝对路径 |
| filepath.Rel()   | 获取相对路径       |
| filepath.Abs()   | 获取绝对路径       |
| path.Join()      | 拼接路径           |

示例

```go
package main

import (
	"fmt"
	"path"
	"path/filepath"
)

func main() {
	path1 := "/home/kain/Documents/code/go_module/file_io/main.go"
	path2 := "./go.mod"
	path3 := "go.mod"

	fmt.Println(filepath.IsAbs(path1))	// true
	fmt.Println(filepath.IsAbs(path2))  // false
	fmt.Println(filepath.IsAbs(path3))  // false

	fmt.Println(filepath.Rel("/home/kain", path1))  // Documents/code/go_module/file_io/main.go <nil>

	fmt.Println(filepath.Abs(path1))	// /home/kain/Documents/code/go_module/file_io/main.go <nil>
	fmt.Println(filepath.Abs(path2))    // /home/kain/Documents/code/go_module/file_io/go.mod <nil>
	fmt.Println(filepath.Abs(path3))    // /home/kain/Documents/code/go_module/file_io/go.mod <nil>

	fmt.Println(path.Join(path1, "."))  // /home/kain/Documents/code/go_module/file_io/main.go
	fmt.Println(path.Join(path1, "..")) // /home/kain/Documents/code/go_module/file_io
	fmt.Println(path.Join("/home", path2)) // /home/go.mod
}
```



# 文件创建删除（目录）

## 检查文件是否存在

golang中通过`Stat`返回的错误,然后调用`IsExist`或`IsNotExist`来判断是否存在

```GO
package main

import "os"

func main() {
	println(PathExist("test.txt"))    	// true
	println(PathExist("go.mod"))       // false
}

func PathExist(path string) bool{
	_, err := os.Stat(path)
	return os.IsNotExist(err)
}
```

## 创建目录

### os.MKdir()

该函数用于创建一层目录,定义如下

```go
// Mkdir creates a new directory with the specified name and permission
// bits (before umask).
// If there is an error, it will be of type *PathError.
func Mkdir(name string, perm FileMode) error {
	if runtime.GOOS == "windows" && isWindowsNulName(name) {
		return &PathError{"mkdir", name, syscall.ENOTDIR}
	}
	e := syscall.Mkdir(fixLongPath(name), syscallMode(perm))

	if e != nil {
		return &PathError{"mkdir", name, e}
	}

	// mkdir(2) itself won't handle the sticky bit on *BSD and Solaris
	if !supportsCreateWithStickyBit && perm&ModeSticky != 0 {
		e = setStickyBit(name)

		if e != nil {
			Remove(name)
			return e
		}
	}

	return nil
}
```

示例

```GO
err := os.MKdir("demo", 0777)
```

### os.MKdirAll()

该函数用于创建多层目录,定义如下

```go
func MkdirAll(path string, perm FileMode) error {
	// Fast path: if we can tell whether path is a directory or file, stop with success or error.
	dir, err := Stat(path)
	if err == nil {
		if dir.IsDir() {
			return nil
		}
		return &PathError{"mkdir", path, syscall.ENOTDIR}
	}

	// Slow path: make sure parent exists and then call Mkdir for path.
	i := len(path)
	for i > 0 && IsPathSeparator(path[i-1]) { // Skip trailing path separator.
		i--
	}

	j := i
	for j > 0 && !IsPathSeparator(path[j-1]) { // Scan backward over element.
		j--
	}

	if j > 1 {
		// Create parent.
		err = MkdirAll(fixRootDirectory(path[:j-1]), perm)
		if err != nil {
			return err
		}
	}

	// Parent now exists; invoke Mkdir and use its result.
	err = Mkdir(path, perm)
	if err != nil {
		// Handle arguments like "foo/." by
		// double-checking that directory doesn't exist.
		dir, err1 := Lstat(path)
		if err1 == nil && dir.IsDir() {
			return nil
		}
		return err
	}
	return nil
}
```

示例

```go
err := os.MkdirAll("dir1/dir2/dir3", os.ModePerm) // os.ModePerm = 0777
```

##　创建文件

### os.Creat()

用该方法创建文本文件，如果文件已经存在，会将其覆盖，定义如下

```go
func Create(name string) (*File, error) {
	return OpenFile(name, O_RDWR|O_CREATE|O_TRUNC, 0666)
}
```

可以发现，他就是通过打开文件的方式来创建文件，通过 `O_TRUNC`标志，来覆盖原文件．

示例

```go
f, err := os.Create("test.txt")
```

## 删除文件（目录）

### os.Remove()

该方法用于删除文件或者空目录,定义如下

```go
func Remove(name string) error {
	// System call interface forces us to know
	// whether name is a file or directory.
	// Try both: it is cheaper on average than
	// doing a Stat plus the right one.
	e := syscall.Unlink(name)
	if e == nil {
		return nil
	}
	e1 := syscall.Rmdir(name)
	if e1 == nil {
		return nil
	}

	// Both failed: figure out which error to return.
	// OS X and Linux differ on whether unlink(dir)
	// returns EISDIR, so can't use that. However,
	// both agree that rmdir(file) returns ENOTDIR,
	// so we can use that to decide which error is real.
	// Rmdir might also return ENOTDIR if given a bad
	// file path, like /etc/passwd/foo, but in that case,
	// both errors will be ENOTDIR, so it's okay to
	// use the error from unlink.
	if e1 != syscall.ENOTDIR {
		e = e1
	}
	return &PathError{"remove", name, e}
}
```

示例

```go
err := os.Remove("demo")
```

### os.RemoveAll()

该方法用于删除目录下面所有子节点,定义如下

```go
// RemoveAll removes path and any children it contains.
// It removes everything it can but returns the first error
// it encounters. If the path does not exist, RemoveAll
// returns nil (no error).
// If there is an error, it will be of type *PathError.
func RemoveAll(path string) error {
	return removeAll(path)
}
```

removeAll()

```go
func removeAll(path string) error {
	if path == "" {
		// fail silently to retain compatibility with previous behavior
		// of RemoveAll. See issue 28830.
		return nil
	}

	// The rmdir system call does not permit removing ".",
	// so we don't permit it either.
	if endsWithDot(path) {
		return &PathError{"RemoveAll", path, syscall.EINVAL}
	}

	// Simple case: if Remove works, we're done.
	err := Remove(path)
	if err == nil || IsNotExist(err) {
		return nil
	}

	// RemoveAll recurses by deleting the path base from
	// its parent directory
	parentDir, base := splitPath(path)

	parent, err := Open(parentDir)
	if IsNotExist(err) {
		// If parent does not exist, base cannot exist. Fail silently
		return nil
	}
	if err != nil {
		return err
	}
	defer parent.Close()

	if err := removeAllFrom(parent, base); err != nil {
		if pathErr, ok := err.(*PathError); ok {
			pathErr.Path = parentDir + string(PathSeparator) + pathErr.Path
			err = pathErr
		}
		return err
	}
	return nil
}
```

示例

```go
err := os.RemoveAll("dir1")
```

# 读写文件

对文件进行读写操作肯定要先打开文件

## 打开关闭文件

### 打开

前面在创建文件时我们已经了解过了文件的打开,使用函数`os.OpenFile()`来实现,定义如下

```go
// OpenFile is the generalized open call; most users will use Open
// or Create instead. It opens the named file with specified flag
// (O_RDONLY etc.). If the file does not exist, and the O_CREATE flag
// is passed, it is created with mode perm (before umask). If successful,
// methods on the returned File can be used for I/O.
// If there is an error, it will be of type *PathError.
func OpenFile(name string, flag int, perm FileMode) (*File, error) {
   testlog.Open(name)
   f, err := openFileNolog(name, flag, perm)
   if err != nil {
      return nil, err
   }
   f.appendMode = flag&O_APPEND != 0

   return f, nil
}
```

它的内部是调用`openFileNolog`函数来实现,有兴趣的同学可以去了解一下

它接收的三个参数分别是文件路径,标志和权限,

标志就是打开方式,可以一种或多种,golang中的标志如下

```go
// Flags to OpenFile wrapping those of the underlying system. Not all
// flags may be implemented on a given system.
const (
	// Exactly one of O_RDONLY, O_WRONLY, or O_RDWR must be specified.
	O_RDONLY int = syscall.O_RDONLY // open the file read-only.
	O_WRONLY int = syscall.O_WRONLY // open the file write-only.
	O_RDWR   int = syscall.O_RDWR   // open the file read-write.
	// The remaining values may be or'ed in to control behavior.
	O_APPEND int = syscall.O_APPEND // append data to the file when writing.
	O_CREATE int = syscall.O_CREAT  // create a new file if none exists.
	O_EXCL   int = syscall.O_EXCL   // used with O_CREATE, file must not exist.
	O_SYNC   int = syscall.O_SYNC   // open for synchronous I/O.
	O_TRUNC  int = syscall.O_TRUNC  // truncate regular writable file when opened.
)
```

权限只在文件不存在时创建文件需要,如果只是普通打开文件,权限填0即可,再如果知识简单得到只读一个已存在的文件,可以使用`os.Open()`函数来实现,这是它的定义

```go
// Open opens the named file for reading. If successful, methods on
// the returned file can be used for reading; the associated file
// descriptor has mode O_RDONLY.
// If there is an error, it will be of type *PathError.
func Open(name string) (*File, error) {
	return OpenFile(name, O_RDONLY, 0)
}
```

不知道你们有没有发现,上述介绍的几个函数的第一个返回值是`os.File`类型的指针,这究竟是什么呢?

让我们来看看它的定义

```go
// File represents an open file descriptor.
type File struct {
	*file // os specific
}
```

它又指向了`file`类型指针,那就看看这个`file`吧

```go
// file is the real representation of *File.
// The extra level of indirection ensures that no clients of os
// can overwrite this data, which could cause the finalizer
// to close the wrong file descriptor.
type file struct {
	pfd         poll.FD
	name        string
	dirinfo     *dirInfo // nil unless directory being read
	nonblock    bool     // whether we set nonblocking mode
	stdoutOrErr bool     // whether this is stdout or stderr
	appendMode  bool     // whether file is opened for appending
}
```

那个`FD`是文件描述符(file descriptor),有兴趣的同学可以展开看看`file`结构体的内部

下面我们来看看`File`结构体都支持哪些操作(这些方法可以在`file.go, stat_unix.go, file_unix.g, file_posix.go, dir.go`中找到)

```
f.Fd()
f.Stat()
f.Name()
f.Close()
f.Write()
f.Chdir()
f.Chmod()
f.Chown()
f.Read()
f.ReadAt()
f.Readdir()
f.Readdirnames()
f.Seek()
f.SetDeadline()
f.SetReadDeadline()
f.Sync()
f.SyscallConn()
f.Truncate()
f.WriteAt()
f.WriteString()
```

虽然方法很多,但是常用的也就几个,无非是读写和关闭.下面我将介绍几个常用的函数,其余的你们有兴趣就去了解吧

### 关闭

`f.Close()`关闭一个打开的文件,方法定义如下,

```go
func (f *File) Close() error {
	if f == nil {
		return ErrInvalid
	}
	return f.file.close()
}
```

调用`f.file.close()`来关闭文件,这里就不深入了

## 读文件

`f.Read()`读取文件内容,方法定义如下

```go
// Read reads up to len(b) bytes from the File.
// It returns the number of bytes read and any error encountered.
// At end of file, Read returns 0, io.EOF.
func (f *File) Read(b []byte) (n int, err error) {
	if err := f.checkValid("read"); err != nil {
		return 0, err
	}
	n, e := f.read(b)
	return n, f.wrapErr("read", e)
}
```

n代表实际读取的字节数,其本质是调用read函数来实现读取,继续深入发现 `read`函数调用了`f.pfd.Read()`,该函数最后调用了`fd.eofError()`方法,在该方法内部,如果读取到最末尾,返回`io.EOF`错误.

示例

```go
package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	var f *os.File
	var err error
	var n int	// 存放读取字节数
	// 初始化一个切片用于存放读取的数据
	bs := make([]byte, 1024*8, 1024*8)

	f,err = os.Open("test.txt")
	if err != nil {
		fmt.Println("文件打开失败")
		return
	}
	
    // 注意关闭文件
	defer f.Close()

	for {
		n, err = f.Read(bs)
		if n == 0 || err == io.EOF{
			fmt.Println("文件读取结束")
			return
		}
		fmt.Println(string(bs[:n]))
	}
}
```

## 写文件

### f.Write()

该方法用字节切片的方式写入文件,定义如下

```go
// Write writes len(b) bytes to the File.
// It returns the number of bytes written and an error, if any.
// Write returns a non-nil error when n != len(b).
func (f *File) Write(b []byte) (n int, err error) {
	if err := f.checkValid("write"); err != nil {
		return 0, err
	}
	n, e := f.write(b)
	if n < 0 {
		n = 0
	}
	if n != len(b) {
		err = io.ErrShortWrite
	}

	epipecheck(f, e)

	if e != nil {
		err = f.wrapErr("write", e)
	}

	return n, err
}
```

示例

```go
package main

import (
	"fmt"
	"os"
)

func main() {
	var f *os.File
	var err error
	var n int	// 存放写入字节数

	f, err = os.OpenFile("test.txt", os.O_RDWR|os.O_CREATE|os.O_APPEND, os.ModePerm)

	if err != nil {
		fmt.Println("文件打开失败")
		return
	}

	// 别忘了关闭文件
	defer f.Close()

	n, err = f.Write([]byte("123abc你好"))
	if err != nil {
		fmt.Println("写入文件失败")
		return
	}else{
		fmt.Printf("成功写入%d个字节\n", n)　// 一个汉字3个字节
	}
}
```

注意, 写文件就不能通过`Open`函数来打开了,`Open`函数是只读的

利用标志`os.O_CREATE`,会在文件不存在时创建

利用标志`os.O_APPEND`,表示追加写入

### f.WriteString()

该方法用字符串的方式写入文件,定义如下

```go
// WriteString is like Write, but writes the contents of string s rather than
// a slice of bytes.
func (f *File) WriteString(s string) (n int, err error) {
	return f.Write([]byte(s))
}
```

可以看到他的本质就是给你转换成字节切片,这个示例我就不演示了,相信大家都能看懂

留个思考题:*请大家阅读相关源码并说明`os.fileState`和`os.file`这两个结构体有何不同,各自的使用场景又是什么?*

 有答案的可以在评论区留言





**如果你看到这里你应该知道了如何使用golang来实现文件的相关操作,但是你们肯定和我一样,觉得golang的文件读写操作很麻烦.下面我们来了解一下文件操作的另外两种方法 `ioutil`和`bufio`**,下面内容部分参考了GO语言中文文档,但文档中的有些内容已经过时,我已经将它更新.





# ioutil

正如其名字ioutil这是一个读写操作包,这里举例一些常用的方法

- `func ReadFile(filename string) ([]byte, error)`

  ReadFile 从filename指定的文件中读取数据并返回文件的内容。成功的调用返回的err为nil而非EOF。因为本函数定义为读取整个文件，它不会将读取返回的EOF视为应报告的错误。

  定义:

  ```go
  func ReadFile(filename string) ([]byte, error) {
  	f, err := os.Open(filename)
  	if err != nil {
  		return nil, err
  	}
  	defer f.Close()
  	// It's a good but not certain bet that FileInfo will tell us exactly how much to
  	// read, so let's try it but be prepared for the answer to be wrong.
  	var n int64 = bytes.MinRead
  
  	if fi, err := f.Stat(); err == nil {
  		// As initial capacity for readAll, use Size + a little extra in case Size
  		// is zero, and to avoid another allocation after Read has filled the
  		// buffer. The readAll call will read into its allocated internal buffer
  		// cheaply. If the size was wrong, we'll either waste some space off the end
  		// or reallocate as needed, but in the overwhelmingly common case we'll get
  		// it just right.
  		if size := fi.Size() + bytes.MinRead; size > n {
  			n = size
  		}
  	}
  	return readAll(f, n)
  }
  ```

  从源码可以看出,ReadFile函数本质也是利用os.File结构体,并调用`readAll`函数处理,这里就不深入了,感兴趣的同学可以去看看,

  例子:

  ```go
  package main
  
  import (
  	"fmt"
  	"io/ioutil"
  )
  
  func main() {
  	bs, err := ioutil.ReadFile("test.txt")
  	if err != nil {
  		fmt.Println("文件打开出错")
  		return
  	}
  	println(string(bs))
  }
  ```

  

- `func WriteFile(filename string, data []byte, perm os.FileMode) error`

  函数向filename指定的文件中写入数据。如果文件不存在将按给出的权限创建文件，否则在写入数据之前清空文件。

  定义:

  ```go
  // WriteFile writes data to a file named by filename.
  // If the file does not exist, WriteFile creates it with permissions perm
  // (before umask); otherwise WriteFile truncates it before writing.
  func WriteFile(filename string, data []byte, perm os.FileMode) error {
  	f, err := os.OpenFile(filename, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, perm)
  	if err != nil {
  		return err
  	}
  	_, err = f.Write(data)
  	if err1 := f.Close(); err == nil {
  		err = err1
  	}
  	return err
  }
  ```

  你没看错这就是这个函数的源码,是不是非常眼熟,这和我们之前写的代码十分相似.

  例子:

  ```go
  package main
  
  import (
  	"io/ioutil"
  	"os"
  )
  
  func main() {
  	err := ioutil.WriteFile("hello.txt", []byte("hello世界"),os.ModePerm)
  	if err != nil {
  		println("文件打开失败")
  	}
  }
  ```

  

- `func ReadDir(dirname string) ([]os.FileInfo, error)`

  返回dirname指定的目录的目录信息的有序列表。

  定义:

  ```go
  // ReadDir reads the directory named by dirname and returns
  // a list of directory entries sorted by filename.
  func ReadDir(dirname string) ([]os.FileInfo, error) {
  	f, err := os.Open(dirname)
  	if err != nil {
  		return nil, err
  	}
  	list, err := f.Readdir(-1)
  	f.Close()
  	if err != nil {
  		return nil, err
  	}
  	sort.Slice(list, func(i, j int) bool { return list[i].Name() < list[j].Name() })
  	return list, nil
  }
  ```

  这个函数的底层也是利用`os.File`结构体,然后调用os.File的Readdir方法,并对结构进行排序输出

  例子:

  ```go
  package main
  
  import (
  	"fmt"
  	"io/ioutil"
  )
  
  func main() {
  	fs, err := ioutil.ReadDir("dir1")
  	if err != nil {
  		println("文件打开失败")
  	}
  	for i, v := range fs{
  		fmt.Println(i, v.Name(), v.IsDir(), v.Size(), v.ModTime())
  	}
  }
  ```

  

- `func ReadAll(r io.Reader) ([]byte, error)`

  ReadAll读取数据直到EOF或遇到error，返回读取的数据和遇到的错误。成功的调用返回的err为nil而非EOF。因为本函数定义为读取r直到EOF，它不会将读取返回的EOF视为应报告的错误。

  定义:

  ```go
  // ReadAll reads from r until an error or EOF and returns the data it read.
  // A successful call returns err == nil, not err == EOF. Because ReadAll is
  // defined to read from src until EOF, it does not treat an EOF from Read
  // as an error to be reported.
  func ReadAll(r io.Reader) ([]byte, error) {
  	return readAll(r, bytes.MinRead)
  }
  ```

  它接收一个参数类型为`io.Reader`,通过读源码可以看出它就是一个实现了`Read`函数的接口

  ```go
  type Reader interface {
  	Read(p []byte) (n int, err error)
  }
  ```

  我们已经知道`os.File`就是实现了`Read`方法,所以我们可以将一个`os.File`结构体传进去,

  例子

  ```go
  package main
  
  import (
  	"io/ioutil"
  	"os"
  )
  
  func main() {
  	var bs []byte
  	var err error
  	var f *os.File
  
  	f, err = os.Open("test.txt")
  	if err != nil {
  		println("打开文件失败")
  		return
  	}
  	defer f.Close()
  
  	bs, err = ioutil.ReadAll(f)
  	if err != nil {
  		println("文件读取失败")
  		return
  	}
  
  	println(string(bs))
  }
  ```

  不难发现`ReadFile`和`ReadAll`方法非常的像,只不过`ReadFile`方法内部对文件进打开操作,而`ReadAll`是在外面手动打开文件然后传进去

- `func TempDir(dir, pattern string) (name string, err error) `

  在dir目录里创建一个新的临时文件夹(其实本质就是普通文件,用作临时存储场景,需要手动删除),该文件夹的命名规则如下,使用将`pattern`用`*`分开,取最后一个做后缀,前面的做前缀,中间拼接随机数字,该操作可在其源码中看到,如下

  

  ```go
  func TempDir(dir, pattern string) (name string, err error) {
  	if dir == "" {
  		dir = os.TempDir()
  	}
  
  	prefix, suffix := prefixAndSuffix(pattern)
  
  	nconflict := 0
  	for i := 0; i < 10000; i++ {
  		try := filepath.Join(dir, prefix+nextRandom()+suffix)
  		err = os.Mkdir(try, 0700)
  		if os.IsExist(err) {
  			if nconflict++; nconflict > 10 {
  				randmu.Lock()
  				rand = reseed()
  				randmu.Unlock()
  			}
  			continue
  		}
  		if os.IsNotExist(err) {
  			if _, err := os.Stat(dir); os.IsNotExist(err) {
  				return "", err
  			}
  		}
  		if err == nil {
  			name = try
  		}
  		break
  	}
  	return
  }
  ```

  其中`prefixAndSuffix`函数定义如下

  ```go
  func prefixAndSuffix(pattern string) (prefix, suffix string) {
  	if pos := strings.LastIndex(pattern, "*"); pos != -1 {
  		prefix, suffix = pattern[:pos], pattern[pos+1:]
  	} else {
  		prefix = pattern
  	}
  	return
  }
  ```

  举个例子

  ```go
  package main
  
  import "io/ioutil"
  
  func main() {
  	name, err := ioutil.TempDir("dir1", "kain*huck")
  	if err != nil {
  		println("文件夹创建失败")
  		return
  	}
  	println(name) // dir1/kain037615429huck
  }
  ```

  

- `func TempFile(dir, pattern string) (f *os.File, err error)`

  在dir目录下创建一个新的临时文件,文件名是通过使用pattern并在末尾添加一个随机字符串生成的。如果pattern包含一个“\*”，随机字符串将替换最后一个“\*”。
  
  定义:
  
  ```go
  func TempFile(dir, pattern string) (f *os.File, err error) {
  	if dir == "" {
  		dir = os.TempDir()
  	}
  
  	prefix, suffix := prefixAndSuffix(pattern)
  
  	nconflict := 0
  	for i := 0; i < 10000; i++ {
  		name := filepath.Join(dir, prefix+nextRandom()+suffix)
  		f, err = os.OpenFile(name, os.O_RDWR|os.O_CREATE|os.O_EXCL, 0600)
  		if os.IsExist(err) {
  			if nconflict++; nconflict > 10 {
  				randmu.Lock()
  				rand = reseed()
  				randmu.Unlock()
  			}
  			continue
  		}
  		break
  	}
  	return
  }
  ```
  
  
  
  ```go
  package main
  
  import "io/ioutil"
  
  func main() {
  	f, err := ioutil.TempFile("dir1", "kain*huck")
  	if err != nil {
  		println("文件创建失败")
  		return
  	}
  	println(f.Name())	// dir1/kain115329465huck
  }
  ```
  
# bufio

bufio包实现了有缓冲的I/O。它包装一个io.Reader或io.Writer接口对象，创建另一个也实现了该接口，且同时还提供了缓冲和一些文本I/O的帮助函数的对象。

## `bufio.Reader`

定义:

```go
// Reader implements buffering for an io.Reader object.
type Reader struct {
	buf          []byte
	rd           io.Reader // reader provided by the client
	r, w         int       // buf read and write positions
	err          error
	lastByte     int // last byte read for UnreadByte; -1 means invalid
	lastRuneSize int // size of last rune read for UnreadRune; -1 means invalid
}
```

常用方法

- `func NewReader(rd io.Reader) *Reader`

  定义:

  ```go
  // NewReader returns a new Reader whose buffer has the default size.
  func NewReader(rd io.Reader) *Reader {
  	return NewReaderSize(rd, defaultBufSize)
  }
  ```

  NewReader调用`NewReaderSize`创建一个具有默认大小缓冲的Reader指针

  defauleBufSize

  ```go
  const (
  	defaultBufSize = 4096
  )
  ```

- `func NewReaderSize(rd io.Reader, size int) *Reader`

  定义:

  ```GO
  // NewReaderSize returns a new Reader whose buffer has at least the specified
  // size. If the argument io.Reader is already a Reader with large enough
  // size, it returns the underlying Reader.
  func NewReaderSize(rd io.Reader, size int) *Reader {
  	// Is it already a Reader?
  	b, ok := rd.(*Reader)
  	if ok && len(b.buf) >= size {
  		return b
  	}
  	if size < minReadBufferSize {
  		size = minReadBufferSize
  	}
  	r := new(Reader)
  	r.reset(make([]byte, size), rd)
  	return r
  }
  ```

  该函数就是上述`NewReader`中被调用的函数,他可以让我们手动的提供缓冲大小,从代码可以看到,所谓缓冲就是一个byte切片,该切片会被赋值给`Reader`结构体的`buf`,

  reset

  ```go
  func (b *Reader) reset(buf []byte, r io.Reader) {
  	*b = Reader{
  		buf:          buf,
  		rd:           r,
  		lastByte:     -1,
  		lastRuneSize: -1,
  	}
  }
  ```

- `func (b *Reader) Reset(r io.Reader)`

  Reset丢弃缓冲中的数据，清除任何错误，将b重设为其下层从r读取数据。

  定义:

  ```go
  // Reset discards any buffered data, resets all state, and switches
  // the buffered reader to read from r.
  func (b *Reader) Reset(r io.Reader) {
  	b.reset(b.buf, r)
  }
  ```

  其内部实现非常简单,就是调用函数`reset`(这个函数在上面已经看过了),将当前的`Reader`中的`rd`属性(io.Reader)重新重设为`r`

- `func (b *Reader) Buffered() int`

  Buffered返回缓冲中现有的可读取的字节数。

  定义如下

  ```go
  // Buffered returns the number of bytes that can be read from the current buffer.
  func (b *Reader) Buffered() int { return b.w - b.r }
  ```

  这个就不解释了

- `func (b *Reader) Peek(n int) ([]byte, error)`

  Peek返回输入流的下n个字节，而不会移动读取位置。返回的[]byte只在下一次调用读取操作前合法。如果Peek返回的切片长度比n小，它也会返会一个错误说明原因。如果n比缓冲尺寸还大，返回的错误将是ErrBufferFull。

  定义:

  ```go
  func (b *Reader) Peek(n int) ([]byte, error) {
  	if n < 0 {
  		return nil, ErrNegativeCount
  	}
  
  	b.lastByte = -1
  	b.lastRuneSize = -1
  
  	for b.w-b.r < n && b.w-b.r < len(b.buf) && b.err == nil {
  		b.fill() // b.w-b.r < len(b.buf) => buffer is not full
  	}
  
  	if n > len(b.buf) {
  		return b.buf[b.r:b.w], ErrBufferFull
  	}
  
  	// 0 <= n <= len(b.buf)
  	var err error
  	if avail := b.w - b.r; avail < n {
  		// not enough data in buffer
  		n = avail
  		err = b.readErr()
  		if err == nil {
  			err = ErrBufferFull
  		}
  	}
  	return b.buf[b.r : b.r+n], err
  }
  ```

  别看前面这么多,那都是一些特殊情况的判断处理,看最后一句得知其实该函数就是返回了缓冲区的切

- `func (b *Reader) Read(p []byte) (n int, err error)`

  Read读取数据写入p。本方法返回写入p的字节数。本方法一次调用最多会调用下层Reader接口一次Read方法，因此返回值n可能小于len(p)。读取到达结尾时，返回值n将为0而err将为io.EOF。

  定义:

  ```go
  func (b *Reader) Read(p []byte) (n int, err error) {
  	n = len(p)
  	if n == 0 {
  		if b.Buffered() > 0 {
  			return 0, nil
  		}
  		return 0, b.readErr()
  	}
  	if b.r == b.w {
  		if b.err != nil {
  			return 0, b.readErr()
  		}
  		if len(p) >= len(b.buf) {
  			// Large read, empty buffer.
  			// Read directly into p to avoid copy.
  			n, b.err = b.rd.Read(p)
  			if n < 0 {
  				panic(errNegativeRead)
  			}
  			if n > 0 {
  				b.lastByte = int(p[n-1])
  				b.lastRuneSize = -1
  			}
  			return n, b.readErr()
  		}
  		// One read.
  		// Do not use b.fill, which will loop.
  		b.r = 0
  		b.w = 0
  		n, b.err = b.rd.Read(b.buf)
  		if n < 0 {
  			panic(errNegativeRead)
  		}
  		if n == 0 {
  			return 0, b.readErr()
  		}
  		b.w += n
  	}
  
  	// copy as much as we can
  	n = copy(p, b.buf[b.r:b.w])
  	b.r += n
  	b.lastByte = int(b.buf[b.r-1])
  	b.lastRuneSize = -1
  	return n, nil
  }
  ```

  从中可以看到`n, b.err = b.rd.Read(p)`,说明这内部是调用io.Read方法.然后将buf中的可用内容尽可能的复制给p.

  鉴于篇幅过长,以下其他常用方法就留给读者自己去分析吧,

  - `func (b *Reader) ReadByte() (c byte, err error)`

    ReadByte读取并返回一个字节。如果没有可用的数据，会返回错误。

  - `func (b *Reader) ReadRune() (r rune, size int, err error)`

    ReadRune读取一个utf-8编码的unicode码值，返回该码值、其编码长度和可能的错误。如果utf-8编码非法，读取位置只移动1字节，返回U+FFFD，返回值size为1而err为nil。如果没有可用的数据，会返回错误。

  - `func (b *Reader) ReadLine() (line []byte, isPrefix bool, err error)`

    ReadLine是一个低水平的行数据读取原语。大多数调用者应使用ReadBytes('\n')或ReadString('\n')代替，或者使用Scanner。

    ReadLine尝试返回一行数据，不包括行尾标志的字节。如果行太长超过了缓冲，返回值isPrefix会被设为true，并返回行的前面一部分。该行剩下的部分将在之后的调用中返回。返回值isPrefix会在返回该行最后一个片段时才设为false。返回切片是缓冲的子切片，只在下一次读取操作之前有效。ReadLine要么返回一个非nil的line，要么返回一个非nil的err，两个返回值至少一个非nil。

    返回的文本不包含行尾的标志字节（"\r\n"或"\n"）。如果输入流结束时没有行尾标志字节，方法不会出错，也不会指出这一情况。在调用ReadLine之后调用UnreadByte会总是吐出最后一个读取的字节（很可能是该行的行尾标志字节），即使该字节不是ReadLine返回值的一部分。

  - `func (b *Reader) ReadString(delim byte) (string, error)`

    ReadString读取直到第一次遇到delim字节，返回一个包含已读取的数据和delim字节的字符串。如果ReadString方法在读取到delim之前遇到了错误，它会返回在错误之前读取的数据以及该错误（一般是io.EOF）。当且仅当ReadString方法返回的切片不以delim结尾时，会返回一个非nil的错误。

  - `func (b *Reader) ReadSlice(delim byte) (line []byte, err error)`

    ReadSlice读取直到第一次遇到delim字节，返回缓冲里的包含已读取的数据和delim字节的切片。该返回值只在下一次读取操作之前合法。如果ReadSlice放在在读取到delim之前遇到了错误，它会返回在错误之前读取的数据在缓冲中的切片以及该错误（一般是io.EOF）。如果在读取到delim之前缓冲就被写满了，ReadSlice失败并返回ErrBufferFull。因为ReadSlice的返回值会被下一次I/O操作重写，调用者应尽量使用ReadBytes或ReadString替代本法功法。当且仅当ReadBytes方法返回的切片不以delim结尾时，会返回一个非nil的错误。

  - `func (b *Reader) ReadBytes(delim byte) ([]byte, error)`

    ReadBytes读取直到第一次遇到delim字节，返回一个包含已读取的数据和delim字节的切片。如果ReadBytes方法在读取到delim之前遇到了错误，它会返回在错误之前读取的数据以及该错误（一般是io.EOF）。当且仅当ReadBytes方法返回的切片不以delim结尾时，会返回一个非nil的错误。

  例子1:

  ```go
  package main
  
  import (
  	"bufio"
  	"fmt"
  	"os"
      "io"
  )
  
  func main() {
  	f,err := os.Open("test.txt")
  	if err != nil {
  		panic(err)
  	}
  	defer f.Close()
  	reader := bufio.NewReader(f)
  	p := make([]byte, 12)
  	n, err :=reader.Read(p)
  	if err != nil &&  err != io.EOF {
  	panic(err)
  	}
  	println(n)
  
  	fmt.Println(string(p))
  }
  ```

  例子2:

  ```go
  package main
  
  import (
  	"bufio"
  	"fmt"
  	"io"
  	"os"
  )
  
  func main() {
  	f,err := os.Open("test.txt")
  	if err != nil {
  		panic(err)
  	}
  	defer f.Close()
  	reader := bufio.NewReader(f)
  	for{
  		str, err := reader.ReadString('\n')
  		if err == io.EOF{
  			fmt.Println(str)
  			break
  		}
  		if err != nil{
  			panic(err)
  		}
  		fmt.Print(str)
  	}
  }
  ```

## `bufio.Writer`

`bufio.Writer`其实和`bufio.Reader`操作很对应.

定义:

```go
// Writer implements buffering for an io.Writer object.
// If an error occurs writing to a Writer, no more data will be
// accepted and all subsequent writes, and Flush, will return the error.
// After all data has been written, the client should call the
// Flush method to guarantee all data has been forwarded to
// the underlying io.Writer.
type Writer struct {
	err error
	buf []byte
	n   int
	wr  io.Writer
}
```

下面列举几个最最常用的方法

- `func NewWriter(w io.Writer) *Writer`

  NewWriter创建一个具有默认大小缓冲、写入w的*Writer。

  定义:

  ```go
  // NewWriter returns a new Writer whose buffer has the default size.
  func NewWriter(w io.Writer) *Writer {
  	return NewWriterSize(w, defaultBufSize)
  }
  ```

  该方法调用`NewWriterSize`,返回一个带有默认缓冲区的`Writer`指针

  defaultBufSize

  ```go
  const (
  	defaultBufSize = 4096
  )
  ```

- `func NewWriterSize(w io.Writer, size int) *Writer`

  NewWriterSize创建一个具有最少有size尺寸的缓冲、写入w的*Writer。如果参数w已经是一个具有足够大缓冲的*Writer类型值，会返回w。

  ```go
  // NewWriterSize returns a new Writer whose buffer has at least the specified
  // size. If the argument io.Writer is already a Writer with large enough
  // size, it returns the underlying Writer.
  func NewWriterSize(w io.Writer, size int) *Writer {
  	// Is it already a Writer?
  	b, ok := w.(*Writer)
  	if ok && len(b.buf) >= size {
  		return b
  	}
  	if size <= 0 {
  		size = defaultBufSize
  	}
  	return &Writer{
  		buf: make([]byte, size),
  		wr:  w,
  	}
  }
  ```

  这个函数的实现过程和`NewReaderSize`如出一辙,只不过`NewReaderSize`中调用了`reset`方法,这里直接初始化指针对象

- `func (b *Writer) Reset(w io.Writer)`

  Reset丢弃缓冲中的数据，清除任何错误，将b重设为将其输出写入w。

  定义:

  ```go
  // Reset discards any unflushed buffered data, clears any error, and
  // resets b to write its output to w.
  func (b *Writer) Reset(w io.Writer) {
  	b.err = nil
  	b.n = 0
  	b.wr = w
  }
  ```

  这个方法就不多做解释了,一眼就明白

- `func (b *Writer) Buffered()`

  Buffered返回缓冲中已使用的字节数。

  定义:

  ```GO
  // Buffered returns the number of bytes that have been written into the current buffer.
  func (b *Writer) Buffered() int { return b.n }
  ```

  这个方法就更不用解释了

- `func (b *Writer) Available() int`

  Available返回缓冲中还有多少字节未使用。

  定义:

  ```go
  // Available returns how many bytes are unused in the buffer.
  func (b *Writer) Available() int { return len(b.buf) - b.n }
  ```

  不解释

- `func (b *Writer) Write(p []byte) (nn int, err error)`

  Write将p的内容写入缓冲。返回写入的字节数。如果返回值nn < len(p)，还会返回一个错误说明原因。

  定义:

  ```go
  func (b *Writer) Write(p []byte) (nn int, err error) {
  	for len(p) > b.Available() && b.err == nil {
  		var n int
  		if b.Buffered() == 0 {
  			// Large write, empty buffer.
  			// Write directly from p to avoid copy.
  			n, b.err = b.wr.Write(p)
  		} else {
  			n = copy(b.buf[b.n:], p)
  			b.n += n
  			b.Flush()
  		}
  		nn += n
  		p = p[n:]
  	}
  	if b.err != nil {
  		return nn, b.err
  	}
  	n := copy(b.buf[b.n:], p)
  	b.n += n
  	nn += n
  	return nn, nil
  }
  ```

  从`n, b.err = b.wr.Write(p)`可得这是通过调用`io.Writer`接口中的`Write`方法,

  `n := copy(b.buf[b.n:], p)`这一句和前面Read方法刚好相反,这是将p复制给buf的可用部分

- `func (b *Writer) WriteString(s string) (int, error)`

  WriteString写入一个字符串。返回写入的字节数。如果返回值nn < len(s)，还会返回一个错误说明原因。

  定义:

  ```go
  func (b *Writer) WriteString(s string) (int, error) {
  	nn := 0
  	for len(s) > b.Available() && b.err == nil {
  		n := copy(b.buf[b.n:], s)
  		b.n += n
  		nn += n
  		s = s[n:]
  		b.Flush()
  	}
  	if b.err != nil {
  		return nn, b.err
  	}
  	n := copy(b.buf[b.n:], s)
  	b.n += n
  	nn += n
  	return nn, nil
  }
  ```

  关键语句`n := copy(b.buf[b.n:], s)`不解释

- `func (b *Writer) Flush() error`

  Flush方法将缓冲中的数据写入下层的io.Writer接口。

  定义:

  ```go
  func (b *Writer) Flush() error {
  	if b.err != nil {
  		return b.err
  	}
  	if b.n == 0 {
  		return nil
  	}
  	n, err := b.wr.Write(b.buf[0:b.n])
  	if n < b.n && err == nil {
  		err = io.ErrShortWrite
  	}
  	if err != nil {
  		if n > 0 && n < b.n {
  			copy(b.buf[0:b.n-n], b.buf[n:b.n])
  		}
  		b.n -= n
  		b.err = err
  		return err
  	}
  	b.n = 0
  	return nil
  }
  ```

  解释一下,如果b有错误就直接返回错误,如果b中没有写入值,则不做任何处理,否则就将缓冲中的n个值写进底层io.Writer中,如果写入的值数量小于缓冲取的值并且没有出错,则将err定义为`io.ErrShortWrite`错误,如果err不为空,并且写进底层`io.Writer`中的数据小于缓冲中原有的数据时,将剩余的数据写进缓冲区开头,将缓冲区已用空间设置为原来大小减去写人底层大小.如果err为空则代表成功将所有缓冲数据写入`io.Writer`将已用空间置为0

其他`bufio`中的方法就留给读者自己去探索吧!

举个例子:

```go
package main

import (
	"bufio"
	"os"
)

func main() {
	f, err := os.OpenFile("test.txt", os.O_RDWR|os.O_CREATE|os.O_APPEND, os.ModePerm)
	if err != nil {
		panic(err)
	}
	defer f.Close()

	writer := bufio.NewWriter(f)
	writer.WriteString("让我康康是哪位靓仔看到了这句话\n")
	writer.Write([]byte("原来是你!\n"))

	writer.Flush()
}
```

注意:最后一定要flush一下,否则数据就不会写入文件,注意使用`OpenFile`函数打开文件并指定可写,否则将写不进去.



到这里这篇文章就结束了,我写了一整天将近8000个字,感谢你坚持看到这里,这是对我最大的支持,如果有什么意见或者不足指出欢迎指出

