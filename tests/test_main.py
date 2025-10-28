from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello" in response.json()["message"]


def test_predict():
    response = client.get("/predict?x=3")
    assert response.status_code == 200
    assert response.json()["prediction"] == 7
