from PageObject.loginpage import LoginPage


class Login(LoginPage):
	"""登陆邮箱"""
	def login(self, user, pwd):
		page = LoginPage(self.driver)
		page.login_input(user, pwd)
		page.login_button()

