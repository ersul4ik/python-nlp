from fastapi.testclient import TestClient

from main import app
from services import get_words

client = TestClient(app)


def test_raise_error_when_item_has_no_company_name():
    response = client.post("/items/")

    assert response.status_code == 400


def test_should_tokenize_given_data():
    words = get_words('The simple, sentence.')

    assert words == ['The', 'simple', 'sentence']
