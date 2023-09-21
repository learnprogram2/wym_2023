> 第二部分是基础知识
>
> 包括:
>
> - 数据结构: 一些集合 array, slice, hash, string
> - 语言基础: func, interface, reflect
> - 常用关键字: 
>
> 有的部分我看的书





# 语言基础

## 2. 接口

接口是计算机系统中多个组件共享的边界，不同的组件能够在边界上交换信息

接口的本质是引入一个新的中间层，调用方可以通过接口与具体实现分离, **上下游通过接口解耦**

**编程语言中接口的概念就更加具体**

- Go不需要显式地声明实现的接口, **接口的实现是隐式的**
- Go 语言只会在传递参数、返回参数以及变量赋值时才会对某个类型是否实现接口进行检查
  - 编译期间做类型检查

- Go 语言中有带有一组方法的接口，另一种是不带任何方法的 `interface{}`

  - iface: 有方法的interface

  - eface: interface{}

    eface不是任意类型, 结构体之类的可以转换成interface{}

    类型转换

- 实现者**结构体和指针实现接口**

  如果用指针函数, 那么不能把结构体赋值给接口

  Go 语言在[传递参数](https://draveness.me/golang/docs/part2-foundation/ch04-basic/golang-function-call/)时都是传值的, 如果是结构体, 就会拷贝一个结构体, 新的结构体需要拿一个指针才能调用.

- 隐式类型转换

  ```go
  func NilOrNot(v interface{}) bool { // v会发生隐式类型转换
  	return v == nil
  }
  ```

  







































