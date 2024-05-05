import pytest
from starlette.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_sanity_check(client):
    response = client.get("/")
    assert response.status_code == 404

def test_snp500(client):
    with open("snp500.csv", "r") as data_set:
        for line in data_set:
            symbol, name = line.strip().split(",")
            response = client.get(f"{symbol}")
            assert response.json()["stock_symbol"] == symbol

if __name__ == "__main__":
    # pytest.main(["-v", "test.py"])
    with open("snp500.csv", "r") as data_set:
        for line in data_set:
            symbol, name = line.strip().split(",")
            response = client.get(f"{symbol}")
            assert response.json()["stock_symbol"] == symbol