# written by spinach/hehelego
# distributed under CC0 license.

# f**k EF online, a python script that helps you to skip EF online exercises. 
# 在上海科技大学,除了英语课,哪里都可以学英语.  

if __name__=='__main__':
    script=\
'''
var data={
    "credentials": "include",
    "headers": {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/json; charset=utf-8",
        "x-request-id": "1606210882390",
        "X-Requested-With": "XMLHttpRequest"
    },
    "referrer": "https://corporate.ef.com.cn/school/studyplan",
    "body": '{"studentActivityId":"<act-id>","score":<score>,"minutesSpent":<time-cost>,"studyMode":0}',
    "method": "POST",
    "mode": "cors"
}
fetch("https://corporate.ef.com.cn/services/api/school/command/scoring/submitactivityscore?c=countrycode%3dcn%7cculturecode%3dzh-CN%7cpartnercode%3dCncp%7csiteversion%3d47-1%7cstudentcountrycode%3dcn%7cdevicetypeid%3d1%7cproductid%3d100",data).then((x)=>console.log(x));
'''

    from selenium import webdriver
    from selenium.common.exceptions import ElementClickInterceptedException,NoSuchElementException
    from time import sleep
    from os import system as shellcmd
    from random import randint as gen
    
    def wait_cond(cond):
        while not cond():
            sleep(RESP_TIME)
        return None
    def wait_interval(dt):
        sleep(dt)
        return None
    url_login=r'https://corporate.ef.com.cn/partner/Corp/default.aspx'
    url_home=r'https://corporate.ef.com.cn/campus/mypage/home'
    RESP_TIME=1

    shellcmd('clear')

    option = webdriver.chrome.options.Options()
    #option.set_preference("dom.webnotifications.enabled",False)
    driver = webdriver.Chrome(options=option)

    def test_page_loaded():
        condition = None
        try:
            elem = driver.find_element_by_css_selector('ul.ets-ui-acc-act-nav')
            condition = elem.is_displayed
        except NoSuchElementException:
            condition = False
        return condition

    def solve_lesson():
        while True:
            wait_interval(RESP_TIME)
            try:
                links = driver \
                        .find_element_by_css_selector('ul.ets-ui-acc-act-nav') \
                        .find_elements_by_tag_name('a')[:-1]
                for i in links:
                    actid= i.get_attribute('data-act-id')
                    actid= actid.split('!')[-1]
                    driver.execute_script( script \
                            .replace('<act-id>',actid) \
                            .replace('<score>',str(100-gen(0,5))) \
                            .replace('<time-cost>',str(gen(2,5)))\
                            )
                    pass
                wait_interval(RESP_TIME)
                driver.find_element_by_css_selector('li.ets-ui-acc-act-nav-summary').click()
                wait_interval(RESP_TIME)
                finished = (driver.find_element_by_tag_name('.ets-btn-white > span:nth-child(1)').text=='返回到单元')
                driver.find_element_by_css_selector('div.ets-btn-white.ets-btn-large').click()
                if finished:
                    break
            except ElementClickInterceptedException:
                    pass
            except:
                pass
            try:
                driver.find_element_by_css_selector('a.tck-ui-ft-link.tck-ui-ft-cancel').click()
            except:
                pass
        return None

    def find_lesson():
        print('locating')
        driver.get(r'https://corporate.ef.com.cn/school/studyplan')
        while True:
            wait_interval(RESP_TIME)
            try:
                elem=driver.find_element_by_class_name('btn.btn-primary.btn-block.btn-sm.ets-sp-step-start')
                if elem.is_displayed:
                    elem.click()
                    return
            except: pass
            wait_interval(RESP_TIME)
            try:
                driver.find_element_by_class_name('ets-sp-sqn-item.ets-suggest').click()
                continue
            except: pass
            wait_interval(RESP_TIME)
            try:
                driver.find_element_by_class_name('ets-sp-sqn-item.ets-suggest.ets-active').click()
                continue
            except: pass
            wait_interval(RESP_TIME)
            try:
                elem=driver.find_element_by_class_name('glyphicon.icon-angle-right')
                if elem.is_displayed: elem.click()
            except: pass
    try:
        print('please login your EF account')
        driver.get(url_login)
        wait_cond(lambda :driver.current_url.startswith(url_home))
        print('login success')
        wait_interval(RESP_TIME);shellcmd('clear')


        while True:
            driver.refresh()
            print('please manually navigate to the test page; ctrl+C to break')
            find_lesson()
            wait_cond(test_page_loaded)
            print('hacking')
            solve_lesson()
            print('done')
            wait_interval(RESP_TIME);shellcmd('clear')
            pass
    finally:
        driver.quit()
        print('exit')
        pass
