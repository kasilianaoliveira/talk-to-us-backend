from http import HTTPStatus

from fastapi.testclient import TestClient

from src.app import app


def test_homepage_should_return_ok_and_welcome_message():
    client = TestClient(app)

    response = client.get("/")  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {"message": "Welcome to the Home Page!"}


def test_app_import():
    assert app is not None
