from src.api.tests.conftest import get_all_product_data


def test_get_all_products(api_context):
    response, data = get_all_product_data(api_context)
    assert response.ok
    assert response.status == 200
    assert response.headers["content-type"] == "application/json; charset=utf-8"

    assert "products" in data
    assert isinstance(data["products"], list)
    assert len(data["products"]) > 0
    assert (data["total"]) == 194

    # first_product = data["products"][0]
    # print(first_product)
