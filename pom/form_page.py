from playwright.sync_api import expect
import re

class FormPage:

    def __init__(self, page):
        self.page = page

        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.email_input = page.get_by_placeholder("name@example.com")
        self.mobile_input = page.get_by_placeholder("Mobile Number")
        self.dob_input = page.locator("#dateOfBirthInput")
        self.current_address = page.get_by_placeholder("Current Address")
        self.state_selector = page.locator("div").filter(has_text=re.compile(r"^Select State$")).nth(3)
        self.city_selector = page.get_by_text("Select City")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.close_button = page.get_by_role("button", name="Close")

    def fill_form(self, first_name, last_name, email, gender, mobile, address, state, city, hobbies):
        # Fill name and email
        self.first_name_input.click()
        self.first_name_input.fill(first_name)
        self.last_name_input.click()
        self.last_name_input.fill(last_name)
        self.email_input.click()
        self.email_input.fill(email)

        # Select gender using dynamic selection
        self.select_gender(gender)
        # Fill mobile number
        self.mobile_input.click()
        self.mobile_input.fill(mobile)

        # Selecting a date (hardcoded example)
        self.dob_input.click()
        self.page.locator("div").filter(has_text=re.compile(r"^JanuaryFebruaryMarchAprilMayJuneJulyAugustSeptemberOctoberNovemberDecember$")).get_by_role("combobox").select_option("3")
        self.page.get_by_role("combobox").nth(1).select_option("2008")
        self.page.get_by_label("Choose Friday, April 4th,").click()

        # Fill address
        self.current_address.click()
        self.current_address.fill(address)

        # Select state and city
        self.state_selector.click()
        self.select_city(city)

        # Select hobbies
        self.select_hobbies(hobbies)
        
        # Submit form
        self.submit_button.click()
        self.close_button.click()

    def select_gender(self, gender):
        self.page.get_by_text(gender, exact=True).click()

    def select_hobbies(self, hobbies):
        for hobby in hobbies:
            self.page.get_by_text(hobby, exact=True).click()
        
    def select_state(self, state):
        self.state_selector.click()
        self.page.get_by_text(state, exact=True).click()

    def select_city(self, city):
        self.city_selector.click()
        self.page.get_by_text(city, exact=True).click()





