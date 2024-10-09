from playwright.sync_api import Page

from src.models.base import BasePage
from src.models.inventory import InventoryPage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._continue_shopping_button = page.get_by_text('Continue shopping')
        self._checkout_button = page.get_by_text('Checkout')
        self._cart_items = page.locator('.cart_item')
        self._cart_header_text = page.get_by_text('Your Cart')
        self._shopping_cart_badge = page.locator('.shopping_cart_badge')

    @property
    def continue_shopping_button(self):
        return self._continue_shopping_button

    @property
    def checkout_button(self):
        return self._checkout_button

    @property
    def cart_header_text(self):
        return self._cart_header_text

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/cart.html")

    def click_continue_shopping_button(self):
        self._continue_shopping_button.click()
        return InventoryPage(self.page)

    def validate_cart_items(self):
        items = self._cart_items.all()
        items_count = 0
        for item in items:
            items_count += 1
        return items_count

    def get_shopping_cart_badge_count(self):
        return self._shopping_cart_badge
