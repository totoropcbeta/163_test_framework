# 163_test_framework
测试环境：Ubuntu20.04, Chrome83

工具：python3.8+selenium3+pycharm2020.1

可选使用yagmail发送测试报告邮件,在根目录run_tests.py中配置,发送方邮箱需要开启官方SMTP服务。

请先安装requirements

`pip3 install -r requirements.txt`

虚拟机环境下,务必将虚拟机设置到全屏状态,以免出现测试error


已加入log日志记录并处理异常,HTML报告也可以查看用例失败和发生错误时的详细信息和截图。

在初次执行Jenkins任务构建时,出现如下错误


```
selenium.common.exceptions.WebDriverException: Message: unknown error: Chrome failed to start: exited abnormally
  (unknown error: DevToolsActivePort file doesn't exist)
  (The process started from chrome location /usr/bin/chromium-browser is no longer running, so ChromeDriver is assuming that Chrome has crashed.)
```


为ChromeDriver添加如下参数


```
option = webdriver.ChromeOptions()
option.add_argument('headless')  # 无可视化模式
option.add_argument('no-sandbox')  # 取消沙盒模式
option.add_argument('disable-dev-shm-usage')
driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=option)
```

Jenkins配置过程见我的博客
[Ubuntu20.04从Java配置到Jenkins持续集成Python自动化测试](https://blog.csdn.net/weixin_42656409/article/details/106848580)
