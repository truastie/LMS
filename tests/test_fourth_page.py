import allure
import pytest

from pages.fourth_page import FourthPage


class TestFourthPage:

    @pytest.mark.positive

    def test_third_page(self, page):
        third_page=FourthPage(page)
        with allure.step("Open URL"):
            third_page.open_page("https://www.saucedemo.com/")
        with allure.step("Fill login field"):
            third_page.fill_login_field("problem_user")
        with allure.step("Fill password field"):
            third_page.fill_password_field("secret_sauce")
        with allure.step("Clicking Login Button"):
            third_page.click_login_button()