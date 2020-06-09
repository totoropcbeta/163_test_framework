from Commonlib.Commonlib import Commonshare


class Login(Commonshare):
	def login(self, user, pwd):
		# 打开url
		self.open_url("https://mail.163.com/")
		# 定位输入账号
		self.input_data("name", "email", user)
		# 定位输入密码
		self.input_data("name", "password", pwd)
		# 定位登录
		self.click("id", "dologin")
