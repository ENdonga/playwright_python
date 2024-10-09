from playwright.sync_api import Page

from models.base import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._products_header = page.get_by_text("Products")

    # Getters
    @property
    def products_header(self):
        return self._products_header

    def get_cart_button(self):
        return self.get_element_by_data_test('shopping-cart-link')
