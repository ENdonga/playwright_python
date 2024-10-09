from playwright.sync_api import Page

from src.models.base import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._products_header = page.get_by_text("Products")
        self._menu_button = page.locator('#react-burger-menu-btn')
        self._logout_out_menu = page.get_by_text('Logout')
        self._add_to_cart_button = page.get_by_text('Add to cart')
        self._remove_from_cart_button = page.get_by_text('Remove')
        self._shopping_cart_badge = page.locator('.shopping_cart_badge')

    # Getters
    @property
    def products_header(self):
        return self._products_header

    @property
    def shopping_cart_badge(self):
        return self._shopping_cart_badge

    def get_cart_button(self):
        return self.get_element_by_data_test('shopping-cart-link')

    def logout_application(self):
        self._menu_button.click()
        self._logout_out_menu.click()

    def add_item_to_cart(self):
        self._add_to_cart_button.first.click()

    def remove_item_from_cart(self):
        self.add_item_to_cart()
        self._remove_from_cart_button.first.click()
