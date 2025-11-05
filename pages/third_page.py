from pages.base_page import BasePage
from playwright.sync_api import expect

class ThirdPage(BasePage):
    def __init__(self, page,timeout=5000):
        super().__init__(page,timeout)
        self.page=page
        self.LOGIN_FIELD=self.page.locator('//*[@id="user-name"]')
        self.PASSWORD_FIELD=self.page.locator('//*[@id="password"]')
        self.BUTTON=self.page.locator('//*[@id="login-button"]')
        self.SORT=self.page.locator('//*[@class="product_sort_container"]')

    def fill_login_field(self, login):
        self.LOGIN_FIELD.fill(login, timeout=self.timeout)

    def fill_password_field(self, password):
        self.PASSWORD_FIELD.fill(password, timeout=self.timeout)

    def click_login_button(self):
        self.BUTTON.click(timeout=self.timeout)

    def check_opened_page(self):
        expect(self.page).to_have_url('https://www.saucedemo.com/inventory.html')

    def choose_sort_by_price(self):
        self.SORT.click()
        self.SORT.select_option('hilo')

