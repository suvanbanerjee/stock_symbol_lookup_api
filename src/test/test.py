from starlette.testclient import TestClient
from app.main import app
import json

client = TestClient(app)



def test_read_item():
    response = client.get('/Apple')
    assert response.status_code == 200
    assert response.json() == {'stock_symbol': 'AAPL'}