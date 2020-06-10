import unittest
from TestAction.login import Login
from TestAction.send_mail import SendEmail
from selenium import webdriver
from time import sleep


class TestSendEmail(unittest.TestCase):
    """163发送邮件测试"""
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        log = Login(cls.driver)
        log.open()
        cls.driver.implicitly_wait(10)
        log.login("wangyiwebtest", "wangyi2020")
        print("send email test start.")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(2)
        cls.driver.quit()
        print("send email test end.")

    def test_001(self):
        """全部正确填写"""
        sen = SendEmail(self.driver)
        sen.send_email("957584602@qq.com", "测试邮件", "这是一封测试邮件。")
        self.assertIn("发送成功", self.driver.page_source)
        sleep(2)
        self.driver.refresh()


if __name__ == '__main__':
    unittest.main()
