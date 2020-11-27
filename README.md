# oops-EFonline

## description

a python script that helps you to pass EF online exercises efficiently. it can automatically solve 1 level each time.

> spinach: **有问题请发issue** ,在IM上面联系我不会取得及时反馈,邮件不回.  
> teafrogsf: use IM or email is also OK, because timely feedback is often not available XD.

## dependencies

- python-selenium
- `firefox+geckodriver` or `googlechrome+chromedriver`

## license

GPL v3.0

## todo

- [x] 不再等待确定时间后操作,而是检查所需的元素是否已经出现在DOM中(partially.为了防止操作过快,快过浏览器响应,仍然保持了一个操作间隔时间,你可以修改代码中的`RESP_TIME`适应不同响应速度)
- [x] 自动解决alert/notification
- [x] 检查并删除mask,防止不可点击exception
- [x] 自动寻找仍未完成的lesson
- [x] 整单元跳过
- [ ] `webdriver.option.headless=true`降低资源占用.


## usage

### on a linux distro(arch linux for example)

```bash
git clone https://github.com/hehelego/oops-EFonline.git
cd oops-EFonline
sudo pacman -S firefox geckodriver python python-selenium
python fuckEF.py
```

0. get python installed on your system
1. clone this repository
2. install dependencies: selenium python binding + browser + geckodriver
3. cd into the repo and run the python script. `cd oops-EFonline && python fuckEF.py`
4. login your account in the browser controlled by this program, the program will detect whether you have successfully logged in.
5. then the program will automatically run. have fun.

### on Windows

```bash
git clone https://github.com/hehelego/oops-EFonline.git
cd oops-EFonline
python fuckEF.py
```

0. get python installed on your system
1. clone this repository
2. install pip
3. install dependencies: selenium python binding + browser (use Tuna for faster speed) + selenium driver
4. cd into the repo and run the python script. `cd oops-EFonline && python fuckEF.py`
5. login your account in the browser controlled by this program, the program will detect whether you have successfully logged in.
6. then the program will automatically run. have fun.


### choose another browser

edit `fuckEF.py` change `browser_choice` to `'chrome'` if you prefer googlechrome.


## known issues

negative integer: it does not seem to affect use.
microphone notification: it does not seem to affect use.


----------------------------------------

## 关于这玩意怎么搞的

直接联系我吧,把这种东西在github上面公开发布出来不太好.  


