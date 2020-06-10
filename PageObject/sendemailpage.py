from PageObject.basepage import BasePage
from time import sleep


class SendEmailPage(BasePage):
    """写信Page"""
    def write_button(self):
        # 点击写信
        sleep(2)
        el_wl = self.by_xpath("//span[text() = '写 信']/parent::li")
        el_wl.click()

    def write_letter(self, email, topic, text):
        # 编辑信件
        sleep(2)
        el_mail = self.by_xpath("//*[@title = '发给多人时地址请以分号隔开']/child::div/input")
        el_mail.send_keys(email)
        el_topic = self.by_xpath("//*[@aria-label = '邮件主题输入框，请输入邮件主题']/child::input")
        el_topic.send_keys(topic)
        el_text = self.by_xpath("//*[text() = '编辑邮件正文']/ancestor::html/child::body")
        el_topic.send_keys(text)

    def send_button(self):
        # 点击发送
        sleep(2)
        el_send = self.by_xpath("//span[text() = '发送']")
        el_send.click()