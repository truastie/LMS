import allure
import pytest

from pages.fourth_page import FourthPage


class TestFourthPage:

    @pytest.mark.positive
    @pytest.mark.parametrize("login, password, expect_success", [
        ("problem_user", "secret_sauce", True),
        ("problem_user", "wrong_password", False),
        ("", "", False),
    ])
    def test_fourth_page(self, page, login, password, expect_success):
        fourth_page=FourthPage(page)
        with allure.step("Open URL"):
            fourth_page.open_page("https://www.saucedemo.com/")
        with allure.step("Fill login field"):
            fourth_page.fill_login_field(login)
        with allure.step("Fill password field"):
            fourth_page.fill_password_field(password)
        with allure.step("Clicking Login Button"):
            fourth_page.click_login_button()


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
