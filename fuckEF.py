# written by spinach/hehelego
# distributed under CC0 license.


# fuck EF online, a python script that helps you to skip EF online exercises. 
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
    def wait_cond(cond):
        while not cond():
            sleep(1)
        return None
    def wait_interval(dt):
        sleep(dt)
        return None
    url_login=r'https://corporate.ef.com.cn/partner/Corp/default.aspx'
    url_home=r'https://corporate.ef.com.cn/campus/mypage/home'
    RESP_TIME=1


    from selenium import webdriver
    from selenium.common.exceptions import ElementClickInterceptedException
    from time import sleep
    from random import randint as gen


    

    option = webdriver.firefox.options.Options()
    option.set_preference("dom.webnotifications.enabled",False)
    driver = webdriver.Firefox(options=option)


    def solve_lesson():
        while True:
            try: ## TODO: replace the wait_interval with wait:html element loaded
                wait_interval(RESP_TIME)
                links = driver \
                        .find_element_by_css_selector('ul.ets-ui-acc-act-nav') \
                        .find_elements_by_tag_name('a')[:-1]
                for i in links:
                    actid= i.get_attribute('data-act-id')
                    actid= actid.split('!')[-1]
                    driver.execute_script( script \
                            .replace('<act-id>',actid) \
                            .replace('<score>',str(100-gen(0,10))) \
                            .replace('<time-cost>',str(gen(1,5)))\
                            )
                    pass
                wait_interval(RESP_TIME)
                driver.find_element_by_css_selector('li.ets-ui-acc-act-nav-summary').click()
                wait_interval(RESP_TIME)
                finished = (driver.find_element_by_tag_name('.ets-btn-white > span:nth-child(1)').text=='返回到单元')
                driver.find_element_by_css_selector('div.ets-btn-white.ets-btn-large').click()
                if finished:
                    break
            except Exception:
                wait_cond(lambda :'OK'==input('Manual intervention required(OK to continue)').upper())
                ## TODO:
                ## delete div.tck-ui-container and retry
                ## click <a class="tck-ui-ft-link tck-ui-ft-cancel" data-action="cancel">取消</a>
        return None



    try:
        driver.get(url_login)
        wait_cond(lambda :input('please login(OK to continue)').upper()=='OK')
        wait_cond(lambda :driver.current_url.startswith(url_home))

        while True:
            user_input = input('The lesson have been fully loaded?').upper()
            if user_input== 'BREAK':
                break
            solve_lesson()
            pass
    finally:
        driver.quit()
        pass
