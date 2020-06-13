import unittest
import os
from ddt import ddt, data, unpack
from TestAction.login import Login
from Utils.logindealutil import ParseExcel
from selenium import webdriver
from time import sleep
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)
excelPath = base_dir + '/TestData/userslogin.xlsx'
sheetName = 'Sheet1'
excel = ParseExcel(excelPath, sheetName)


@ddt
class Testlogincase(unittest.TestCase):
    """163登陆测试"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 设置隐式等待
        self.driver.implicitly_wait(10)
        # 设置浏览器的最大化
        self.driver.maximize_window()
        # print("login test start.")

    def tearDown(self):
        self.driver.quit()
        # print("login test finished.")

    @data(*excel.getDatasFromSheet())
    @unpack
    def test_login(self, user, password, assertion):
        # print(user, password, assertion)
        log = Login(self.driver)
        log.open()
        log.login(user, password)
        sleep(2)
        # 断言
        self.assertIn(assertion, self.driver.page_source)


if __name__ == '__main__':
    unittest.main()

