from PageObject.basepage import BasePage


class LoginPage(BasePage):
    """163邮箱登陆Page层"""
    url = "https://mail.163.com/"

    def login_input(self, user, pwd):
        # 输入帐号
        self.by_name("email").send_keys(user)
        # 输入密码
        self.by_name("password").send_keys(pwd)

    def login_button(self):
        el_login = self.by_id("dologin")
        el_login.click()
