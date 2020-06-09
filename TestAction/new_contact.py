from PageObject.contactpage import ContactPage


class NewContact(ContactPage):
    """新建联系人"""
    def newcontact(self, name, email, star, phone, note):
        page = ContactPage(self.driver)
        page.new_contact()
        page.contact_msg(name, email, star, phone, note)
        page.confirm()
