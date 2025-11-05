import allure
import pytest

from pages.fourth_page import FourthPage


class TestFourthPage:

    @pytest.mark.positive

    def test_fourth_page(self, page):
        fourth_page=FourthPage(page)
        with allure.step("Open URL"):
            fourth_page.open_page("https://www.saucedemo.com/")
        with allure.step("Fill login field"):
            fourth_page.fill_login_field("problem_user")
        with allure.step("Fill password field"):
            fourth_page.fill_password_field("secret_sauce")
        with allure.step("Clicking Login Button"):
            fourth_page.click_login_button()
        with allure.step("Checking open URL"):
            fourth_page.opened_page()


    def test_empty_username_field(self, page):
        fourth_page = FourthPage(page)
        with allure.step("Open URL"):
            fourth_page.open_page("https://www.saucedemo.com/")
        with allure.step("Fill login field"):
            fourth_page.fill_login_field("")
        with allure.step("Fill password field"):
            fourth_page.fill_password_field("secret_sauce")
        with allure.step("Clicking Login Button"):
            fourth_page.click_login_button()
        with allure.step("Error message"):
            assert fourth_page.error_message_empty_username() == "Epic sadface: Username is required"

    def test_empty_password_field(self, page):
        fourth_page = FourthPage(page)
        with allure.step("Open URL"):
            fourth_page.open_page("https://www.saucedemo.com/")
        with allure.step("Fill login field"):
            fourth_page.fill_login_field("problem_user")
        with allure.step("Fill password field"):
            fourth_page.fill_password_field("")
        with allure.step("Clicking Login Button"):
            fourth_page.click_login_button()
        with allure.step("Error message"):
            assert fourth_page.error_message_empty_password() == "Epic sadface: Password is required"
