import logging
import traceback
import unittest
import os

from selenium.common.exceptions import NoSuchElementException

from TestAction.login import Login
from Utils.exceldealutil import ParseExcel
from ddt import ddt, data, unpack
from TestAction.send_mail import SendEmail
from selenium import webdriver
from time import sleep

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='163_web_test.log',
                    filemode='a+',
                    )
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)
excelPath = base_dir + '/TestData/sendemail.xlsx'
sheetName = 'Sheet1'
excel = ParseExcel(excelPath, sheetName)


@ddt
class TestSendEmail(unittest.TestCase):
    """163发送邮件测试"""
    @classmethod
    def setUpClass(cls) -> None:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_argument('no-sandbox')
        option.add_argument('disable-dev-shm-usage')
        cls.driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=option)
        cls.driver.maximize_window()
        log = Login(cls.driver)
        log.open()
        cls.driver.implicitly_wait(10)
        log.login("wangyiwebtest", "wangyi2020")
        # print("send email test start.")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(2)
        cls.driver.quit()
        # print("send email test end.")

    @data(*excel.getDatasFromSheet())
    @unpack
    def test_email(self, recipients, topic, text, assertion):
        try:
            # print(recipients, topic, text, assertion)
            sen = SendEmail(self.driver)
            sen.send_email(recipients, topic, text)
            self.assertIn(assertion, self.driver.page_source)
            sleep(2)
            self.driver.refresh()
        except NoSuchElementException as e:
            logging.error("页面元素不存在,异常堆栈信息:" + str(traceback.format_exc()))
        except AssertionError as e:
            logging.info("测试用例:%s, 期望: \'%s\',, 失败" % ((recipients, topic, text), assertion))
        except Exception as e:
            logging.error("未知错误, 错误信息:" + str(traceback.format_exc()))
        else:
            logging.info("测试用例:%s, 期望: \'%s\', 通过" % ((recipients, topic, text), assertion))


if __name__ == '__main__':
    unittest.main()
