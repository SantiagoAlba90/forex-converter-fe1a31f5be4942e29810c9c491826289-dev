import pytest
from currency_converter import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_valid_conversion(client):
    response = client.post('/', data={
        'from_currency': 'USD',
        'amount': '100',
        'to_currency': 'EUR'
    })
    assert b"is equal to" in response.data

def test_invalid_conversion_currency(client):
    response = client.post('/', data={
        'from_currency': 'USD',
        'amount': '100',
        'to_currency': 'XYZ'
    })
    assert b"Invalid currency codes" in response.data

def test_invalid_amount(client):
    response = client.post('/', data={
        'from_currency': 'USD',
        'amount': 'invalid_number',
        'to_currency': 'EUR'
    })
    assert b"Invalid amount input" in response data
