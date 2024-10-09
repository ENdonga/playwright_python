from playwright.sync_api import expect


def test_cart_button_display(inventory_page):
    expect(inventory_page.get_cart_button()).to_be_visible()
    expect(inventory_page.products_header).to_contain_text("Products")


def test_adding_item_to_cart(inventory_page):
    inventory_page.add_item_to_cart()
    expect(inventory_page.shopping_cart_badge).to_be_visible()


def test_removing_item_from_cart(inventory_page):
    inventory_page.remove_item_from_cart()
    expect(inventory_page.shopping_cart_badge).not_to_be_visible()
