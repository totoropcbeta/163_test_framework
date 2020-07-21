import traceback
import unittest
import logging
import os
from ddt import ddt, data, unpack
from selenium.common.exceptions import NoSuchElementException

from TestAction.login import Login
from Utils.exceldealutil import ParseExcel
from TestAction.new_contact import NewContact
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
excelPath = base_dir + '/TestData/newcontact.xlsx'
sheetName = 'Sheet1'
excel = ParseExcel(excelPath, sheetName)


@ddt
class Testcontactcase(unittest.TestCase):
    """163新建联系人测试"""
    @classmethod
    def setUpClass(cls):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')  # 无可视化模式
        option.add_argument('no-sandbox')  # 取消沙盒模式
        option.add_argument('disable-dev-shm-usage')
        cls.driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=option)
        cls.driver.maximize_window()
        log = Login(cls.driver)
        log.open()
        log.login("wangyiwebtest", "wangyi2020")
        # print("new contact test start.")

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.driver.quit()
        # print("new contact test finished.")

    @data(*excel.getDatasFromSheet())
    @unpack
    def test_contact(self, name, email, star, phone, note, assertion):
        try:
            # print(name, email, star, phone, note, assertion)
            con = NewContact(self.driver)
            con.newcontact(name, email, star, phone, note)
            self.assertIn(assertion, self.driver.page_source)
            self.driver.refresh()
        except NoSuchElementException as e:
            logging.error("页面元素不存在,异常堆栈信息:" + str(traceback.format_exc()))
        except AssertionError as e:
            logging.info("测试用例:%s, 期望: \'%s\',, 失败" % ((name, email, star, phone, note), assertion))
        except Exception as e:
            logging.error("未知错误, 错误信息:" + str(traceback.format_exc()))
        else:
            logging.info("测试用例:%s, 期望: \'%s\', 通过" % ((name, email, star, phone, note), assertion))


if __name__ == '__main__':
    unittest.main()
