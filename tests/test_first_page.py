import pytest
import allure
from pages.first_page import FirstPage


@pytest.mark.positive

class TestFirstPage:

    def test_first_page(self, page):
        first_page=FirstPage(page)
        with allure.step("Open URL"):
            first_page.open_page("https://demoqa.com/text-box")
        with allure.step("Fill name field"):
            first_page.fill_name_field("Hello")
        with allure.step("Fill email field"):
            first_page.email_field("1245@gmail.com")
        with allure.step("Fill Current Address"):
            first_page.current_address_field("Example of address")
        with allure.step("Fill Permanent address"):
            first_page.permanent_address_field("Example of permanent address")
        with allure.step("Clicking Submit Button"):
            first_page.clicking_button()

@pytest.mark.negative

class TestFirstPageNegative:
    @pytest.mark.parametrize('email', ['a', '@gmail.com'])
    def test_negative_first_page(self, page, email):
        first_page = FirstPage(page)
        with allure.step("Open URL"):
            first_page.open_page("https://demoqa.com/text-box")
        with allure.step("Fill name field"):
            first_page.fill_name_field("Hello")
        with allure.step("Fill email field"):
            first_page.email_field(email)
        with allure.step("Fill Current Address"):
            first_page.current_address_field("Example of address")
        with allure.step("Fill Permanent address"):
            first_page.permanent_address_field("Example of permanent address")
        with allure.step("Clicking Submit Button"):
            first_page.clicking_button()