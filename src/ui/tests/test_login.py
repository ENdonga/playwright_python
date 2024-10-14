from playwright.sync_api import expect

from src.ui.models.inventory import InventoryPage
from src.ui.models.login import LoginPage

credentials = {'username': 'standard_user', 'locked_username': 'locked_out_user', 'password': 'secret_sauce'}


def test_successful_login(authenticate):
    page = authenticate
    expect(page.get_by_text("Products")).to_contain_text("Products")


def test_unsuccessful_login(login_page: LoginPage):
    login_page.login_button.click()
    expect(login_page.get_error_message()).to_have_text("Epic sadface: Username is required")


def test_login_without_username(login_page: LoginPage):
    login_page.login_with_invalid_details(password=credentials.get('password'))
    expect(login_page.get_error_message()).to_have_text("Epic sadface: Username is required")


def test_login_without_password(login_page: LoginPage):
    login_page.login_with_invalid_details(username=credentials.get('username'))
    expect(login_page.get_error_message()).to_have_text("Epic sadface: Password is required")


def test_login_with_locked_user(login_page: LoginPage):
    login_page.login_with_invalid_details(username=credentials.get('locked_username'),
                                          password=credentials.get('password'))
    expect(login_page.get_error_message()).to_have_text("Epic sadface: Sorry, this user has been locked out.")


def test_successful_application_logout(inventory_page: InventoryPage, login_page: LoginPage):
    inventory_page.logout_application()
    expect(login_page.login_button).to_be_visible()
