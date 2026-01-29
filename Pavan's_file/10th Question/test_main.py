from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_employee():
    response = client.post("/employees", json={
        "name": "Pavan",
        "address": "Hyderabad",
        "salary": 50000,
        "age": 25
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Pavan"

def test_get_employees():
    response = client.get("/employees")
    assert response.status_code == 200

def test_get_employee_not_found():
    response = client.get("/employees/999")
    assert response.status_code == 404
