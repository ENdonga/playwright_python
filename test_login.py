from playwright.sync_api import Page, expect

from models.login import LoginPage

USERNAME = "standard_user"
LOCKED_USERNAME = "locked_out_user"
PASSWORD = "secret_sauce"


def test_successful_login(login_page: LoginPage, page: Page):
    login_page.navigate()
    login_page.login(USERNAME, PASSWORD)
    expect(page.get_by_text("Products")).to_contain_text("Products")


def test_unsuccessful_login(login_page: LoginPage):
    login_page.navigate()
    login_page.login_button.click()
    expect(login_page.get_error_message()).to_have_text("Epic sadface: Username is required")


def test_login_without_username(login_page: LoginPage):
    login_page.navigate()
    login_page.login_with_invalid_details(password=PASSWORD)
    expect(login_page.get_error_message()).to_have_text("Epic sadface: Username is required")


def test_login_without_password(login_page: LoginPage):
    login_page.navigate()
    login_page.login_with_invalid_details(username=USERNAME)
    expect(login_page.get_error_message()).to_have_text("Epic sadface: Password is required")


def test_login_with_locked_user(login_page: LoginPage):
    login_page.navigate()
    login_page.login_with_invalid_details(username=LOCKED_USERNAME, password=PASSWORD)
    expect(login_page.get_error_message()).to_have_text("Epic sadface: Sorry, this user has been locked out.")
