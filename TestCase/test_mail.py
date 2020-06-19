import unittest
import os
from TestAction.login import Login
from Utils.exceldealutil import ParseExcel
from ddt import ddt, data, unpack
from TestAction.send_mail import SendEmail
from selenium import webdriver
from time import sleep
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
        # print(recipients, topic, text, assertion)
        sen = SendEmail(self.driver)
        sen.send_email(recipients, topic, text)
        self.assertIn(assertion, self.driver.page_source)
        sleep(2)
        self.driver.refresh()


if __name__ == '__main__':
    unittest.main()
