import logging
import traceback
import unittest
import os
from ddt import ddt, data, unpack
from selenium.common.exceptions import NoSuchElementException

from TestAction.login import Login
from Utils.exceldealutil import ParseExcel
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
excelPath = base_dir + '/TestData/userslogin.xlsx'
sheetName = 'Sheet1'
excel = ParseExcel(excelPath, sheetName)


@ddt
class Testlogincase(unittest.TestCase):
    """163登陆测试"""
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_argument('no-sandbox')
        option.add_argument('disable-dev-shm-usage')
        self.driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=option)
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
        try:
            # print(user, password, assertion)
            log = Login(self.driver)
            log.open()
            log.login(user, password)
            sleep(2)
            # 断言
            self.assertIn(assertion, self.driver.page_source)
        except NoSuchElementException as e:
            logging.error("页面元素不存在,异常堆栈信息:" + str(traceback.format_exc()))
        except AssertionError as e:
            logging.info("测试用例:%s, 期望: \'%s\',, 失败" % ((user, password), assertion))
        except Exception as e:
            logging.error("未知错误, 错误信息:" + str(traceback.format_exc()))
        else:
            logging.info("测试用例:%s, 期望: \'%s\', 通过" % ((user, password), assertion))


if __name__ == '__main__':
    unittest.main()

