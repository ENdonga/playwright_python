import pytest
from playwright.sync_api import sync_playwright

from src.config import API_BASE_URL

RESOURCE_URL = "products"


@pytest.fixture(scope="function")
def api_context(playwright: sync_playwright):
    context = playwright.request.new_context()
    yield context
    context.dispose()


def get_all_product_data(context: sync_playwright):
    response = context.get(f"{API_BASE_URL}/{RESOURCE_URL}")
    data = response.json()
    return response, data


def get_product_data(context: sync_playwright, product_id: int):
    response = context.get(f"{API_BASE_URL}/{RESOURCE_URL}/{product_id}")
    data = response.json()
    return response, data
