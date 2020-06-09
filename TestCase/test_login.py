import unittest
from TestAction.login import Login


class Testlogincase(unittest.TestCase):
    """163登陆测试"""
    @classmethod
    def setUpClass(cls):
        print("start")

    @classmethod
    def tearDownClass(cls):
        print("end")

    def test_001(self):
        """输入正确账号密码"""
        log = Login()
        log.login("wangyiwebtest", "wangyi2020")
        # 获取用于断言的用户名
        data = log.get_text("id", "spnUid")
        # 断言
        self.assertEqual("wangyiwebtest@163.com", data)

    def test_002(self):
        """不输入账号密码"""
        log = Login()
        log.login("", "")
        # 获取用于断言的用户名
        data = log.get_text("class", "ferrorhead")
        # 断言
        self.assertEqual("请输入帐号", data)

    def test_003(self):
        """输入账号不输入密码"""
        log = Login()
        log.login("wangyiwebtest", "")
        # 获取用于断言的用户名
        data = log.get_text("id", "nerror")
        # 断言
        self.assertEqual("请输入密码", data)

    def test_004(self):
        """输入密码不输入账号"""
        log = Login()
        log.login("", "wangyi2020")
        # 获取用于断言的用户名
        data = log.get_text("class", "ferrorhead")
        # 断言
        self.assertEqual("请输入帐号", data)

    def test_005(self):
        """输入正确账号错误密码"""
        log = Login()
        log.login("wangyiwebtest", "aaaaaaaa")
        # 获取用于断言的用户名
        data = log.get_text("id", "nerror")
        # 断言
        self.assertEqual("帐号或密码错误", data)


if __name__ == '__main__':
    unittest.main()
