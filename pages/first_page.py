

from pages.base_page import BasePage


class FirstPage(BasePage):
    def __init__(self, page,timeout=5000):
        super().__init__(page,timeout)
        self.page=page
        self.FULL_NAME=self.page.locator('//*[@id="userName"]')
        self.EMAIL=self.page.locator('//*[@id="userEmail"]')
        self.CURRENT_ADDRESS=self.page.locator('//*[@id="currentAddress"]')
        self.PERMANENT_ADDRESS=self.page.locator('//*[@id="permanentAddress"]')
        self.SUBMIT_BUTTON=self.page.get_by_text('Submit')


    def fill_name_field(self, name):
        self.FULL_NAME.fill(name, timeout=self.timeout)

    def email_field(self, email):
        self.EMAIL.fill(email, timeout=self.timeout)

    def current_address_field(self, cur_address):
        self.CURRENT_ADDRESS.fill(cur_address, timeout=self.timeout)

    def permanent_address_field(self, perm_address):
        self.PERMANENT_ADDRESS.fill(perm_address, timeout=self.timeout)

    def clicking_button(self):
        self.SUBMIT_BUTTON.click()



