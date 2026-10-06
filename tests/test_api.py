
import requests
from datetime import date, timedelta

BASE_URL = "http://localhost:8000"

def test_crear_tarea():
    print("\nProbando creación de tarea...")
    response = requests.post(f"{BASE_URL}/tasks/", json={
        "titulo": "Tarea de prueba",
        "contenido": "Contenido de la tarea de prueba",
        "deadline": (date.today() + timedelta(days=1)).isoformat()
    })

    if response.status_code == 201:
        data = response.json()

        print(f"Tarea creada exitosamente: {data}")
        
        if (
            data["titulo"] == "Tarea de prueba" and 
            data["contenido"] == "Contenido de la tarea de prueba" and 
            data["deadline"] == (date.today() + timedelta(days=1)).isoformat()
            ):
            print("Tarea creada con los datos correctos")
        else:
            print("Error: Los datos de la tarea creada no son los esperados")
    else:
        print(f"Error al crear la tarea: {response.status_code} - {response.text}")

def test_obtener_tarea():
    print("\nProbando obtención de tarea...")
    response = requests.get(f"{BASE_URL}/tasks/1")

    if response.status_code == 200:
        data = response.json()
        print(f"Tarea obtenida exitosamente: {data}")
        
        if data["id"] == 1:
            print("Tarea con ID 1 obtenida correctamente")
        else:
            print(f"Error: Se esperaba la tarea con ID 1, pero se obtuvo la tarea con ID {data['id']}")
    else:
        print(f"Error al obtener la tarea: {response.status_code} - {response.text}")

def test_marcar_completada():
    print("\nProbando marcar tarea como completada...")
    response = requests.put(f"{BASE_URL}/tasks/1/completar", json={
        "completada": True
    })

    if response.status_code == 200:
        print(f"Tarea {response.json()['id']} marcada como completada exitosamente")
    else:
        print(f"Error al marcar la tarea como completada: {response.status_code} - {response.text}")


def test_obtener_tareas_caducadas():
    print("\nProbando obtención de tareas caducadas...")
    response = requests.get(f"{BASE_URL}/tasks/caducadas")

    if response.status_code == 200:
        print(f"Tareas caducadas obtenidas exitosamente: {response.json()}")
    else:
        print(f"Error al obtener las tareas caducadas: {response.status_code} - {response.text}")


def test_datos_incorrectos():
    print("\nProbando creación de tarea con datos incorrectos (deadline en el pasado)...")
    response = requests.post(f"{BASE_URL}/tasks/", json={
            "titulo": "Tarea de prueba",
            "contenido": "Contenido de la tarea de prueba",
            "deadline": (date.today() - timedelta(days=1)).isoformat()
        })

    if response.status_code == 400:
        print(f"Datos incorrectos al crear la tarea: Codigo de respuesta {response.status_code} - {response.text}")
    else:
        print(f"Error inesperado: {response.status_code} - {response.text}")

if __name__ == "__main__":
    print("Ejecutando tests...")
    
    test_crear_tarea()
    test_obtener_tarea()
    test_marcar_completada()
    test_obtener_tareas_caducadas()
    test_datos_incorrectos()

    print("\nTests completados")
