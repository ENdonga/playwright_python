from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def get_element_by_data_test(self, test_id: str):
        return self.page.locator(f'[data-test="{test_id}"]')
