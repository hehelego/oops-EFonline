# oops-EFonline

## description

a python script that helps you to pass EF online exercises efficiently.

> **有问题请发issue** ,在IM上面联系我不会取得及时反馈,邮件不回. 

## dependencies

- python-selenium
- firefox
- geckodriver

## license

GPL v3.0

## todo

- [x] 不再等待确定时间后操作,而是检查所需的元素是否已经出现在DOM中(partially.为了防止操作过快,快过浏览器响应,仍然保持了一个操作间隔时间,你可以修改代码中的`RESP_TIME`适应不同响应速度)
- [x] 自动解决alert/notification
- [x] 检查并删除mask,防止不可点击exception
- [ ] 自动寻找仍未完成的lesson
- [ ] 整单元掉过
- [ ] `webdriver.option.headless=true`降低资源占用.


## usage


```bash
git clone https://github.com/hehelego/oops-EFonline.git
cd oops-EFonline
sudo pacman -S firefox geckodriver python python-selenium
python fuckEF.py
```

在浏览器中登录,在CLI输入ok后按enter,手动点击到答题界面.    
看到`The lesson have been fully loaded?`时,确认跳过测试输入ok,否则输入break之后按enter继续.  

如果这一节最后有speak那么会需要你手动操作一下...  

之后手动点到下一课的答题界面,确认页面加载完成,看到`fully loaded`之后输入ok继续...  
重复上面的操作.  


根据本人实测,大概半小时能刷一个module.


--------------------------------------

==这是一个分割线,下面没有任何有意义的内容==

--------------------------------------

## 关于这玩意怎么搞的

直接联系我吧,把这种东西在github上面公开发布出来不太好.  


