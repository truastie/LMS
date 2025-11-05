from pages.base_page import BasePage

class SecondPage(BasePage):
    def __init__(self, page, timeout=5000):
        super().__init__(page, timeout)
        self.page = page
        self.FIRST_NAME=self.page.locator('//*[@id="firstName"]')
        self.LAST_NAME=self.page.locator('//*[@id="lastName"]')
        self.EMAIL_FIELD=self.page.locator('//*[@id="userEmail"]')
        self.MOBILE=self.page.locator('//*[@id="userNumber"]')
        self.DATE_BIRTH=self.page.locator('//*[@id="dateOfBirthInput"]')
        self.SUBJECTS=self.page.locator('#subjectsInput')
        self.HOBBIES=self.page.locator('//*[@id="hobbiesWrapper"]/div[2]')
        self.PICTURE=self.page.locator('#uploadPicture')
        self.CURRENT_ADDRESS=self.page.locator('//*[@id="currentAddress"]')
        self.STATE=self.page.locator('//*[@id="state"]/div/div[2]/div')
        self.CITY=self.page.locator('//*[@id="city"]/div/div[2]/div')
        self.SUBMIT_BUTTON=self.page.locator('//*[@id="submit"]')


    def fill_name_field(self, name):
        self.FIRST_NAME.click()
        self.FIRST_NAME.fill(name, timeout=self.timeout)

    def fill_last_name_field(self, last_name):
        self.LAST_NAME.fill(last_name, timeout=self.timeout)

    def fill_email_field(self, email):
        self.EMAIL_FIELD.fill(email, timeout=self.timeout)

    def select_gender(self, gender):
        self.page.locator(f"//label[text()='{gender}']").click()

    def fill_mobile_number(self, number):
        self.MOBILE.fill(number, timeout=self.timeout)

    def select_date_of_birth(self, date_str):
        self.DATE_BIRTH.click(timeout=self.timeout)
        self.DATE_BIRTH.fill(date_str)
        self.DATE_BIRTH.press("Enter")

    def fill_subjects_field(self, subjects):
        self.SUBJECTS.fill(subjects, timeout=self.timeout)
        self.SUBJECTS.press("Enter")

    def select_hobbies(self, hobbies):
        self.page.locator(f"//label[text()='{hobbies}']").click(timeout=self.timeout)

    def select_picture(self, file_name):
        self.PICTURE.set_input_files(file_name)

    def fill_current_address(self, current_address):
        self.CURRENT_ADDRESS.fill(current_address, timeout=self.timeout)

    def select_state_city(self, state, city):
        self.STATE.click()
        self.page.locator(f"//div[text()='{state}']").click()
        self.CITY.click()
        self.page.locator(f"//div[text()='{city}']").click()

    def click_button(self):
        self.SUBMIT_BUTTON.click()