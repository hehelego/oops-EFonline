firefox看XHR记录发现只是一个submit activity score


发现页面里面有一个activity-id
`<div class="ets-act-bd-activity" data-at-id="activity-container" data-at-activity-id="adc75d84-defd-41d4-8f8e-caf3047a5d17" data-woven="school-ui-activity/activity/movie-presentation/continuousMovie@2189">`

或者更直接地,这里直接就有

```html
<div class="ets-ui-acc-step-nav" data-woven="school-ui-activity-container/widget/activity/navigation/main@362">
	<ul class="ets-ui-acc-act-nav">
		<li class="ets-ui-acc-act-nav-act" data-at-id="student_activity!bf167c41-b86c-4e94-b0a7-34e2fce6ad12">
			<a class="" data-nav-index="0" data-act-id="student_activity!bf167c41-b86c-4e94-b0a7-34e2fce6ad12" data-action="route" href="javascript:void(0)">1</a>
		</li> 
		<li class="ets-ui-acc-act-nav-act" data-at-id="student_activity!0975cd4f-1d5b-43b2-81dc-2ce3d1bc6deb">
			<a class=" ets-ui-acc-act-nav-active" data-nav-index="1" data-act-id="student_activity!0975cd4f-1d5b-43b2-81dc-2ce3d1bc6deb" data-action="route" href="javascript:void(0)">2</a>
		</li> 
		<li class="ets-ui-acc-act-nav-act" data-at-id="student_activity!b11b0a8e-9f81-444c-ac24-83eabfbd143a">
			<a class="" data-nav-index="2" data-act-id="student_activity!b11b0a8e-9f81-444c-ac24-83eabfbd143a" data-action="route" href="javascript:void(0)">3</a>
		</li> 
		<li class="ets-ui-acc-act-nav-act" data-at-id="student_activity!1e8d6849-8141-4bb6-b318-2a7aaef63cf7">
			<a class="" data-nav-index="3" data-act-id="student_activity!1e8d6849-8141-4bb6-b318-2a7aaef63cf7" data-action="route" href="javascript:void(0)">4</a>
		</li> 
		<li class="ets-ui-acc-act-nav-act" data-at-id="student_activity!8399b8a5-915b-441d-8911-8557b461095c">
			<a class="" data-nav-index="4" data-act-id="student_activity!8399b8a5-915b-441d-8911-8557b461095c" data-action="route" href="javascript:void(0)">5</a>
		</li> 
		<li class="ets-ui-acc-act-nav-summary">
			<a href="javascript:void(0)" data-action="route" class="">&nbsp;</a>
		</li> 
	</ul>
</div>
```

```javascript
await fetch("https://corporate.ef.com.cn/services/api/school/command/scoring/submitactivityscore?c=countrycode%3dcn%7cculturecode%3dzh-CN%7cpartnercode%3dCncp%7csiteversion%3d47-1%7cstudentcountrycode%3dcn%7cdevicetypeid%3d1%7cproductid%3d100", {
		"credentials": "include",
		"headers": {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0",
		"Accept": "*/*",
		"Accept-Language": "en-US,en;q=0.5",
		"Content-Type": "application/json; charset=utf-8",
		"x-request-id": "1606202209195",
		"X-Requested-With": "XMLHttpRequest"
		},
		"referrer": "https://corporate.ef.com.cn/school/studyplan",
		"body": "{\"studentActivityId\":\"49e52017-be76-4731-b88f-1a53aa3d0f10\",\"score\":100,\"minutesSpent\":2,\"studyMode\":0}",
		"method": "POST",
		"mode": "cors"
		});
```

还差一步了,就是模拟登录获取cookie  
这比较困难,我们还是真实登录一下,然后用一个叫cookie manager的firefox extension来export cookie.然后用py来读取
