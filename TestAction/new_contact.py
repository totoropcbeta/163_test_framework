


class Contact(Commonshare):
    """新建联系人"""
    def new_contact(self, name, email, star, phone, note):
        self.click("xpath", "//div[text()='通讯录']")
        self.click("class", "nui-btn-text")  # 新建联系人
        self.input_data("id", "input_N", name)  # 姓名
        self.input_data("xpath", "//*[@id = 'iaddress_MAIL_wrap']//input", email)  # 电子邮箱
        if star:
            self.click("id", "fly0")  # 设为星标联系人
        self.input_data("xpath", "//*[@id = 'iaddress_TEL_wrap']//dd//input", phone)  # 手机号码
        self.input_data("id", "input_DETAIL", note)  # 备注
        self.click("xpath", "//span[text() = '确 定']")