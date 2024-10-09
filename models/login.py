from playwright.sync_api import Page

from models.base import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._username_input = page.get_by_placeholder("Username")
        self._password_input = page.get_by_placeholder("Password")
        self._login_button = page.get_by_text("Login")

    # Getters
    @property
    def username_input(self):
        return self._username_input

    @property
    def password_input(self):
        return self._password_input

    @property
    def login_button(self):
        return self._login_button

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def login_with_invalid_details(self, username='', password=''):
        if username:
            self.username_input.fill(username)
        if password:
            self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        return self.get_element_by_data_test('error')
