import pytest
from playwright.sync_api import Page

from src.ui.models.cart import CartPage
from src.ui.models.inventory import InventoryPage
from src.ui.models.login import LoginPage

credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
URL = "https://www.saucedemo.com"


@pytest.fixture(scope="function")
def setup(page: Page) -> Page:
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto(URL)
    yield page


@pytest.fixture(scope="function")
def authenticate(setup: Page):
    login_page = LoginPage(setup)
    login_page.login(credentials['username'], credentials['password'])
    yield setup


@pytest.fixture(scope="function")
def login_page(setup):
    return LoginPage(setup)


@pytest.fixture(scope="function")
def inventory_page(authenticate: Page):
    return InventoryPage(authenticate)


@pytest.fixture(scope="function")
def cart_page(authenticate: Page):
    return CartPage(authenticate)
