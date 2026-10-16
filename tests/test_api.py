
import pytest
import requests
from datetime import date, timedelta

BASE_URL = "http://localhost:8000"

def test_obtener_tareas(client):
    print("\nProbando obtención de tareas...")
    response = client.get(f"/tasks/")

    assert response.status_code == 200
    print(f"Tareas obtenidas exitosamente: {response.json()}")

def test_obtener_tareas_caducadas(client):
    print("\nProbando obtención de tareas caducadas...")
    response = client.get(f"/tasks/caducadas")

    assert response.status_code == 200
    print(f"Tareas caducadas obtenidas exitosamente: {response.json()}")


def test_obtener_tareas_caducadas(client):
    print("\nProbando obtención de tareas caducadas...")
    response = client.get(f"/tasks/caducadas")

    assert response.status_code == 200
    print(f"Tareas caducadas obtenidas exitosamente: {response.json()}")

def test_obtener_tarea(client, crear_tarea):
    print("\nProbando obtención de tarea...")

    task_id = crear_tarea["id"]  # Obtener el ID de la tarea creada en el test anterior

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    
    data = response.json()
    
    assert data["id"] == task_id
    assert data["titulo"] == "FastAPI"

def test_crear_tarea(client):
    print("\nProbando creación de tarea...")
    
    response = client.post(f"/tasks/", json={
        "titulo": "Tarea de prueba",
        "contenido": "Contenido de la tarea de prueba",
        "deadline": (date.today() + timedelta(days=1)).isoformat()
    })

    assert response.status_code == 201

    data = response.json()

    assert data["titulo"] == "Tarea de prueba"
    assert data["contenido"] == "Contenido de la tarea de prueba"
    assert data["deadline"] == (date.today() + timedelta(days=1)).isoformat()


def test_marcar_completada(client, crear_tarea):
    print("\nProbando marcar tarea como completada...")

    task_id = crear_tarea["id"]

    response = client.put(f"/tasks/{task_id}/completar", json={
        "completada": True
    })

    assert response.status_code == 200
    assert response.json()["completada"] == True

def test_eliminar_tarea(client, crear_tarea):
    print("\nProbando eliminación de tarea...")
    
    task_id = crear_tarea["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 204

def test_datos_incorrectos(client):
    print("\nProbando creación de tarea con datos incorrectos (deadline en el pasado)...")
    
    response = client.post(f"/tasks/", json={
            "titulo": "Tarea de prueba",
            "contenido": "Contenido de la tarea de prueba",
            "deadline": (date.today() - timedelta(days=1)).isoformat()
        })

    assert response.status_code == 400
    print(f"Datos incorrectos al crear la tarea: Codigo de respuesta {response.status_code} - {response.text}")

    
if __name__ == "__main__":
    print("Ejecutando tests...")
    
    test_crear_tarea()
    test_obtener_tarea()
    test_marcar_completada()
    test_obtener_tareas_caducadas()
    test_datos_incorrectos()
    test_eliminar_tarea()
    test_obtener_tareas()

    print("\nTests completados")
