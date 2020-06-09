from PageObject.basepage import BasePage


class ContactPage(BasePage):
    """邮箱新建联系人Page"""
    def new_contact(self):
        """点击新建联系人"""
        el_new = self.by_xpath("//span[text() = '新建联系人']")
        el_new.clicl()

    def contact_msg(self, name, email, star, phone, note):
        """联系人信息"""
        self.by_xpath("//*[@title = '编辑详细姓名']/preceding-sibling::div/input'").send_keys(name)
        self.by_xpath("//*[@id = 'iaddress_MAIL_wrap']//input").send_keys(email)
        if star:
            self.by_xpath("//span[text() = '设为星标联系人']/preceding-sibling::span/b").click()
        self.by_xpath("//*[@id = 'iaddress_TEL_wrap']//dd//input").send_keys(phone)
        self.by_xpath("//textarea").send_keys(note)

    def confirm(self):
        """确定"""
        el_cfm = self.by_xpath("//span[text() = '确 定']")
        el_cfm.click()
