import allure
import pytest

from pages.third_page import ThirdPage


class TestThirdPage:

    @pytest.mark.positive

    def test_third_page(self, page):
        third_page=ThirdPage(page)
        with allure.step("Open URL"):
            third_page.open_page("https://www.saucedemo.com/")
        with allure.step("Fill login field"):
            third_page.fill_login_field("standard_user")
        with allure.step("Fill password field"):
            third_page.fill_password_field("secret_sauce")
        with allure.step("Clicking Login Button"):
            third_page.click_login_button()
        with allure.step("Check that correct page was opened"):
            third_page.check_opened_page()
        with allure.step("Sorting by price from high to low"):
            third_page.choose_sort_by_price()

