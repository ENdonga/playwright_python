import pytest
from playwright.sync_api import Page

from models.inventory import InventoryPage
from models.login import LoginPage

USERNAME = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture(scope="function")
def authenticate(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(USERNAME, PASSWORD)
    yield page


@pytest.fixture(scope="function")
def login_page(page: Page):
    return LoginPage(page)


@pytest.fixture(scope="function")
def inventory_page(authenticate: Page):
    return InventoryPage(authenticate)
