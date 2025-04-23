from uvicorn import Config, Server

from src.app import app


def test_server_initialization(mock_server):
    config = Config("app:app", port=5000, log_level="info", reload=True)
    server = Server(config)

    server.run()
    mock_server.assert_called_once()


def test_app_import():
    assert app is not None
