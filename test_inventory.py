from playwright.sync_api import expect


def test_cart_button_display(inventory_page):
    expect(inventory_page.get_cart_button()).to_be_visible()
    expect(inventory_page.products_header).to_contain_text("Products")


def test_some_other_test(inventory_page):
    # some other assertions
    expect(inventory_page.products_header).to_contain_text("Products")
