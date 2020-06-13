import time
import os
import unittest
import yagmail
from Commonlib.HTMLTestRunner import HTMLTestRunner


# 把测试报告作为附件发送到指定邮箱。
def send_mail(report):
    yag = yagmail.SMTP(
        user="wangyiwebtest@163.com",
        password="NEPXGACWQWRERVNZ",
        host='smtp.163.com'
    )
    subject = "自动化测试报告"
    contents = "请查看附件。"
    yag.send('957584602@qq.com', subject, contents, report)
    print('email has send out !')


if __name__ == '__main__':
    # 定义测试用例的目录为当前目录
    base_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = base_dir + '/TestCase'
    suit = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    # 取当前日期时间
    now_time = time.strftime("%Y-%m-%d %H:%M:%S")
    html_report = base_dir + '/TestReport/' + now_time + '_test_report.html'
    with open(html_report, 'wb') as fp:
        # 调用HTMLTestRunner，运行测试用例
        runner = HTMLTestRunner(
            stream=fp,
            verbosity=2,
            title="163邮箱Web自动化测试报告",
            description="Ubuntu20.04,Chrome83"
        )
        runner.run(suit)
        fp.close()
        send_mail(html_report)  # 发送报告
