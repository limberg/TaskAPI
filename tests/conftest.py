from datetime import date, timedelta

from fastapi.testclient import TestClient
import pytest

from api.main import app


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def crear_tarea(client):

    response = client.post(
        "/tasks",
        json={
            "titulo": "FastAPI",
            "contenido": "Crear fixture para crear tarea",
            "deadline": (date.today() + timedelta(days=1)).isoformat()
        }
    )

    print(response.json())
    assert response.status_code == 201

    return response.json()