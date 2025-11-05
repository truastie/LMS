from pages.second_page import SecondPage
import pytest
import allure

from utils.generator import random_email, random_number, random_name, random_birth_date, random_subject, \
    random_state_city


class TestSecondPage:

    @pytest.mark.parametrize('gender', ["Male", "Female", "Other"])
    @pytest.mark.parametrize('hobbies', ["Sports", "Reading", "Music"])
    def test_second_page(self, page, gender, hobbies):
        sec_page=SecondPage(page)
        with allure.step("Open URL"):
            sec_page.open_page("https://demoqa.com/automation-practice-form")
        with allure.step("Fill name field"):
            sec_page.fill_name_field(random_name())
        with allure.step("Fill last name"):
            sec_page.fill_last_name_field(random_name())
        with allure.step("Fill email field"):
            sec_page.fill_email_field(random_email())
        with allure.step("Select gender by parametrize"):
            sec_page.select_gender(gender)
        with allure.step("Fill mobile number"):
            sec_page.fill_mobile_number(random_number())
        with allure.step("Select date of birth"):
            sec_page.select_date_of_birth(random_birth_date())
        with allure.step("Fill Subjects in Subject field"):
            sec_page.fill_subjects_field(random_subject())
        with allure.step("Select hobbies by parametrize"):
            sec_page.select_hobbies(hobbies)
        with allure.step("Select picture"):
            sec_page.select_picture(r"C:\Users\nasty\PycharmProjects\Exercise\utils\pic.jpg")
        with allure.step("Fill current address"):
            sec_page.fill_current_address(random_name())
        with allure.step("Select state and city"):
            state, city=random_state_city()
            sec_page.select_state_city(state, city)
        with allure.step("Click Submit Button"):
            sec_page.click_button()
