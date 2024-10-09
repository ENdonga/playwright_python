from playwright.sync_api import expect


def test_cart_continue_shopping_navigation(cart_page, inventory_page):
    cart_page.navigate()
    expect(cart_page.cart_header_text).to_contain_text('Your Cart')
    inventory_page = cart_page.click_continue_shopping_button()
    expect(inventory_page.products_header).to_contain_text('Products')


def test_cart_line_items(cart_page, inventory_page):
    inventory_page.add_item_to_cart()
    cart_page.navigate()
    item_count = cart_page.validate_cart_items()
    actual_count = int(cart_page.get_shopping_cart_badge_count().inner_text())
    assert item_count == actual_count
