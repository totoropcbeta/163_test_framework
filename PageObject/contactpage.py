from PageObject.basepage import BasePage
from time import sleep


class ContactPage(BasePage):
    """邮箱新建联系人Page"""
    def new_contact(self):
        """点击通讯录"""
        sleep(2)
        el_txl = self.by_xpath("//li[@title = '通讯录']")
        el_txl.click()
        """点击新建联系人"""
        sleep(2)
        el_new = self.by_xpath("//span[text() = '新建联系人']")
        el_new.click()

    def contact_msg(self, name, email, star, phone, note):
        """联系人信息"""
        sleep(2)
        if name:
            el_name = self.by_xpath("//*[@title = '编辑详细姓名']/preceding-sibling::div/input")
            el_name.send_keys(name)
        if email:
            self.by_xpath("//*[@id = 'iaddress_MAIL_wrap']//input").send_keys(email)
        if star:
            self.by_xpath("//span[text() = '设为星标联系人']/preceding-sibling::span/b").click()
        if phone:
            self.by_xpath("//*[@id = 'iaddress_TEL_wrap']//dd//input").send_keys(phone)
        if note:
            self.by_xpath("//textarea").send_keys(note)

    def confirm(self):
        """确定"""
        el_cfm = self.by_xpath("//span[text() = '确 定']")
        el_cfm.click()
