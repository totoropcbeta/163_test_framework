import unittest
import os
from ddt import ddt, data, unpack
from TestAction.login import Login
from Utils.exceldealutil import ParseExcel
from TestAction.new_contact import NewContact
from selenium import webdriver
from time import sleep
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
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usa')
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        log = Login(cls.driver)
        log.open()
        log.login("totoropcbeta", "totoro520jcl")
        print("new contact test start.")

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.driver.quit()
        print("new contact test finished.")

    @data(*excel.getDatasFromSheet())
    @unpack
    def test_contact(self, name, email, star, phone, note, assertion):
        print(name, email, star, phone, note, assertion)
        con = NewContact(self.driver)
        con.newcontact(name, email, star, phone, note)
        self.assertIn(assertion, self.driver.page_source)
        self.driver.refresh()


if __name__ == '__main__':
    unittest.main()
