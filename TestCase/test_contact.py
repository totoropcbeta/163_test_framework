import unittest
from TestAction.login import Login
from TestAction.new_contact import NewContact
from selenium import webdriver
from time import sleep


class Testcontactcase(unittest.TestCase):
    """163新建联系人测试"""
    @classmethod
    def setUpClass(cls):
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

    def test_001(self):
        """全部填写"""
        con = NewContact(self.driver)
        con.newcontact("张三", "85858685@163.com", True, "13285698745", "联系人1")
        self.assertIn("85858685@163.com", self.driver.page_source)
        self.driver.refresh()

    def test_002(self):
        """不选星标"""
        con = NewContact(self.driver)
        con.newcontact("李四", "6848668486@163.com", False, "15964258963", "联系人2")
        self.assertIn("6848668486@163.com", self.driver.page_source)
        self.driver.refresh()

    def test_003(self):
        """不填邮件地址"""
        con = NewContact(self.driver)
        con.newcontact("王五", "", False, "18654235874", "联系人3")
        self.assertIn("请正确填写邮件地址。", self.driver.page_source)
        self.driver.refresh()

    def test_004(self):
        """填写错误邮件地址"""
        con = NewContact(self.driver)
        con.newcontact("钱六", "957584565@", False, "159564236985", "联系人4")
        self.assertIn("请正确填写邮件地址。", self.driver.page_source)
        self.driver.refresh()


if __name__ == '__main__':
    unittest.main()
