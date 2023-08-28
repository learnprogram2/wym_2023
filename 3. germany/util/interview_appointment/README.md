

上海的面签比较难，自己也要学着写脚本了


识别工具：ddddocr

涉及到的接口：





## 0826

脚本终于写完了，不能抢票，只能监控。






## 0824
最近情况，照片拿到了，需要ocr api来识别，再继续下面的api。
但是因为go的ocr 没有找到合适的框架，于是改成python写。
没有写过python，但是借助chatgpt应该没问题，也不是大问题

现在在处理ocr识别，是用的ddddocr，但是我找不到框架里面用的两个配置文件，
所以只能拉项目run一下它的训练，生成两个配置文件，靠。我不知道为什么这么麻烦。

唉， 希望明天能够生成好，然后继续下面的script。


## 0814

**拿到验证码：**

看了一下页面，

`curl post https://service2.diplo.de/rktermin/extern/appointment_showMonth.do` 拿到html页面，

captcha的tag里面就是验证码

`service2.diplo.de/rktermin/extern/appointment_showMonth.do`上海北京是一样的，只是后面的地区之类的参数会变。

```go
// api: 
// method: post
// param:
//   chengdu: locationCode=cheng&realmId=170&categoryId=733
//   guangzhou: locationCode=kant&realmId=352&categoryId=577
//   shanghai: 
//   beijing: 
// headers:

// body:

```