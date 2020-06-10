from PageObject.sendemailpage import SendEmailPage


class SendEmail(SendEmailPage):
    """发送邮件"""
    def send_email(self, email, topic, text):
        page = SendEmailPage(self.driver)
        page.write_button()
        page.write_letter(email, topic, text)
        page.send_button()
