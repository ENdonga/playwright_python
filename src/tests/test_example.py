import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title(re.compile("Swag Labs"))


def test_login_form_displayed(page: Page):
    page.goto("https://www.saucedemo.com")
    expect(page.get_by_text("Login")).to_be_visible()
