from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_raise_error_when_item_has_no_company_name():
    response = client.post("/items/")

    assert response.status_code == 400
