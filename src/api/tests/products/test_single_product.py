from src.api.tests.conftest import get_product_data


def test_get_single_product_with_valid_id(api_context):
    response, data = get_product_data(api_context, 1)
    assert response.ok
    assert response.status == 200
    assert response.headers["content-type"] == "application/json; charset=utf-8"
    assert data['title'] == "Essence Mascara Lash Princess"


def test_get_single_product_with_invalid_id(api_context):
    product_id = 200
    response, data = get_product_data(api_context, product_id)
    assert response.status == 404
    assert data['message'] == f"Product with id '{product_id}' not found"
