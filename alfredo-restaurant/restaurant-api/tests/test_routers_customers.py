from fastapi.testclient import TestClient


def test_get_customers(client: TestClient):
    response = client.get("/api/customers")
    assert response.status_code == 200
    customers = response.json()
    assert isinstance(customers, list)
    assert len(customers) > 0  # Ensure there's at least one customer loaded
    assert customers[0]["firstname"] == "Bart"  # Check a known customer's data


def test_get_customer_by_id(client: TestClient):
    response = client.get("/api/customers/1")
    assert response.status_code == 200
    customer = response.json()
    assert customer["firstname"] == "Bart"
    assert customer["email"] == "bart@simpson.com"


def test_create_customer(client: TestClient):
    new_customer = {
        "firstname": "Lisa",
        "lastname": "Simpson",
        "email": "lisa@simpson.com",
        "phone": "555-555-5559",
        "special": True,
        "card_digits": "1234",
        "external_id": "#5679",
        "street": "742 Evergreen Terrace",
        "city": "Springfield",
        "state": "IL",
        "zip": "62701",
        "country": "USA"
    }
    response = client.post("/api/customers", json=new_customer)
    assert response.status_code == 200
    created_customer = response.json()
    assert created_customer["firstname"] == "Lisa"
    assert created_customer["email"] == "lisa@simpson.com"

    # Verify that the customer was actually added to the database
    response = client.get(f"/api/customers/{created_customer['id']}")
    assert response.status_code == 200
    customer_from_db = response.json()
    assert customer_from_db["firstname"] == "Lisa"


def test_update_customer(client: TestClient):
    update_data = {
        "email": "bart_updated@simpson.com",
        "special": False
    }
    response = client.patch("/api/customers/1", json=update_data)
    assert response.status_code == 200
    updated_customer = response.json()
    assert updated_customer["email"] == "bart_updated@simpson.com"
    assert updated_customer["special"] is False

    # Verify that the update persisted
    response = client.get("/api/customers/1")
    assert response.status_code == 200
    customer_from_db = response.json()
    assert customer_from_db["email"] == "bart_updated@simpson.com"
    assert customer_from_db["special"] is False
