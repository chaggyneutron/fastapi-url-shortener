from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_shorten():
    payload = {"target_url": "https://google.com"}
    response = client.post("/shorten", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "short_code" in data
    assert data["target_url"] in ["https://google.com", "https://google.com/"]
    assert data["click_count"] == 0

