import http

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_hello_world_endpoint():
    response = client.get("/")
    assert response.ok
    assert response.json() == "Hello World!"


def test_add_bad():
    """Fastapi automatically provides input validation based on type hints"""
    response = client.get("/add", params=dict(x="a", y="b"))

    assert not response.ok
    assert response.status_code == http.HTTPStatus.UNPROCESSABLE_ENTITY
    assert "value is not a valid float" in response.json()["detail"][0]["msg"]
