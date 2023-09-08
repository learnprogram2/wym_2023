> https://www.yuque.com/aceld/golang/yyrlis











## 3. 逃逸现象，变量何时在堆、栈分配

Golang中一个函数内局部变量，不管是不是动态new出来的，它会被分配在堆还是栈，是由编译器做逃逸分析之后做出的决定。

go的设计者不希望开发者管这些

## 4. Golang中make与new有何区别？

```go
   var i *int
   *i=10
// 报错：
// panic: runtime error: invalid memory address or nil pointer dereference
// [signal SIGSEGV: segmentation violation code=0x1 addr=0x0 pc=0x4849df]
```

对于引用类型的变量，我们不光要声明它，还要为它分配内容空间，否则我们的值放在哪里去呢？

  要分配内存，就引出来今天的`new`和`make`。

```go
// The new built-in function allocates memory. The first argument is a type,
// not a value, and the value returned is a pointer to a newly
// allocated zero value of that type.
func new(Type) *Type
// 重点：分配的内存置为零, 返回的是pointer
```

```go
// The make built-in function allocates and initializes an object of type
// slice, map, or chan (only). Like new, the first argument is a type, not a
// value. Unlike new, make's return type is the same as the type of its
// argument, not a pointer to it. The specification of the result depends on
// the type:
//
//	Slice: The size specifies the length. The capacity of the slice is
//	equal to its length. A second integer argument may be provided to
//	specify a different capacity; it must be no smaller than the
//	length. For example, make([]int, 0, 10) allocates an underlying array
//	of size 10 and returns a slice of length 0 and capacity 10 that is
//	backed by this underlying array.
//	Map: An empty map is allocated with enough space to hold the
//	specified number of elements. The size may be omitted, in which case
//	a small starting size is allocated.
//	Channel: The channel's buffer is initialized with the specified
//	buffer capacity. If zero, or the size is omitted, the channel is
//	unbuffered.
func make(t Type, size ...IntegerType) Type
// 重点: 
// 1. 只能创建slice,map,chan: 三种类型是引用类型, 引用类型是指的直接在堆里,拿的指针???????
// 2. 返回的是值本身,不是pointer
```

- 都是堆空间分配(先进行逃逸分析再决定分配到哪)

## 5. GC: 三色标记混合写屏障

都是标记清除

没有整理



## 6. Interface 理解

接口的最大的意义就是实现多态的思想

符合开闭原则

依赖倒置



## 7. Defer

1. 多个defer 是栈

2. defer 在return之后执行, return赋值返回参数

   ```go
   func returnButDefer() (t int) {  //t初始化0， 并且作用域为该函数全域
       defer func() {
           t = t * 10  // t = 10
       }()
       return 1 // t = 1
   }
   ```

   

## 8. Go modules: 项目依赖

Go Modoules的目的之一就是淘汰GOPATH

- **A. 无版本控制概念.** 在执行`go get`的时候，你无法传达任何的版本信息的期望，也就是说你也无法知道自己当前更新的是哪一个版本，也无法通过指定来拉取自己所期望的具体版本。

- **B.无法同步一致第三方版本号.** 在运行 Go 应用程序的时候，你无法保证其它人与你所期望依赖的第三方库是相同的版本，也就是说在项目依赖库的管理上，你无法保证所有人的依赖版本都一致。
- **C.无法指定当前项目引用的第三方版本号.**  你没办法处理 v1、v2、v3 等等不同版本的引用问题，因为 GOPATH 模式下的导入路径都是一样的，都是`github.com/foo/bar`。



`go mod init`



**没看太懂 Go Modoules里面的相关概念.**



## 9. Go内存管理

没看太懂,这一部分涉及到的是什么知识?





























