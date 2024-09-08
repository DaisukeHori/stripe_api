from fastapi.testclient import TestClient
from app.main import app
import pytest
from unittest.mock import patch

client = TestClient(app)

@pytest.fixture
def mock_stripe_customer():
    return {
        "id": "cus_123",
        "email": "test@example.com",
        "name": "Test User"
    }

def test_get_customers(mock_stripe_customer):
    with patch('app.services.stripe_service.stripe.Customer.list') as mock_list:
        mock_list.return_value.auto_paging_iter.return_value = [mock_stripe_customer]
        response = client.get("/api/customers/test@example.com")
        assert response.status_code == 200
        assert response.json() == {"customers": [mock_stripe_customer]}

# 他のエンドポイントに対するテストも同様に実装