

上海的面签比较难，自己也要学着写脚本了


识别工具：ddddocr

涉及到的接口：









## 0814

**拿到验证码：**

看了一下页面，

`curl post https://service2.diplo.de/rktermin/extern/appointment_showMonth.do` 拿到html页面，

captcha的tag里面就是验证码

`service2.diplo.de/rktermin/extern/appointment_showMonth.do`上海北京是一样的，只是后面的地区之类的参数会变。