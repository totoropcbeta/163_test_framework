import unittest
from TestAction.login import Login
from TestAction.new_contact import NewContact
from selenium import webdriver


class Testcontactcase(unittest.TestCase):
    """163新建联系人测试"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        log = Login()
        log.login("wangyiwebtest", "wangyi2020")
        print("new contact test start.")

    @classmethod
    def tearDownClass(cls):
        print("new contact test finished.")

    def test_001(self):
        """全部填写"""
        con = NewContact(self.driver)
        con.newcontact("张三", "85858685@163.com", True, "13285698745", "联系人1")
        data = con.get_text("xpath", "//*[text() = '85858685@163.com']")
        self.assertEqual("85858685@163.com", data)


if __name__ == '__main__':
    unittest.main()
