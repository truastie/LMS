from playwright.sync_api import expect

from pages.base_page import BasePage


class FourthPage(BasePage):
    def __init__(self, page,timeout=5000):
        super().__init__(page,timeout)
        self.page=page
        self.LOGIN_FIELD = self.page.locator('//*[@id="user-name"]')
        self.PASSWORD_FIELD = self.page.locator('//*[@id="password"]')
        self.BUTTON = self.page.locator('//*[@id="login-button"]')
        self.ERROR_EMPTY_PASSWORD=self.page.get_by_text('Epic sadface: Password is required')
        self.ERROR_EMPTY_USERNAME=self.page.get_by_text('Epic sadface: Username is required')

    def fill_login_field(self, login):
        self.LOGIN_FIELD.fill(login, timeout=self.timeout)

    def fill_password_field(self, password):
        self.PASSWORD_FIELD.fill(password, timeout=self.timeout)

    def click_login_button(self):
        self.BUTTON.click(timeout=self.timeout)

    def opened_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html", timeout=self.timeout)

    def error_message_empty_username(self):
        if self.ERROR_EMPTY_USERNAME.is_visible():
            return self.ERROR_EMPTY_USERNAME.text_content()

    def error_message_empty_password(self):
        if self.ERROR_EMPTY_PASSWORD.is_visible():
            return self.ERROR_EMPTY_PASSWORD.text_content()



