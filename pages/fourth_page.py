from pages.base_page import BasePage


class FourthPage(BasePage):
    def __init__(self, page,timeout=5000):
        super().__init__(page,timeout)
        self.page=page
        self.LOGIN_FIELD = self.page.locator('//*[@id="user-name"]')
        self.PASSWORD_FIELD = self.page.locator('//*[@id="password"]')
        self.BUTTON = self.page.locator('//*[@id="login-button"]')

    def fill_login_field(self, login):
        self.LOGIN_FIELD.fill(login, timeout=self.timeout)

    def fill_password_field(self, password):
        self.PASSWORD_FIELD.fill(password, timeout=self.timeout)

    def click_login_button(self):
        self.BUTTON.click(timeout=self.timeout)
