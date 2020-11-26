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

0. get python installed on your system
1. clone this repository
2. install dependencies: selenium python binding + firefox + geckodriver
3. cd into the repo and run the python script. `cd oops-EFonline && python fuckEF.py`
4. login your account in the browser controlled by this program, the program will detect whether you have successfully logged in.
5. manually navigate to the testing page, where you can see the exercises.  when a testing page is deteced, the program will help you to skip the test.
6. wait until the lesson is finished, you will be leaded back to the `studyplan` page.  
7. repeat step 5/6. have fun.


--------------------------------------

==这是一个分割线,下面没有任何有意义的内容==

--------------------------------------

## 关于这玩意怎么搞的

直接联系我吧,把这种东西在github上面公开发布出来不太好.  


