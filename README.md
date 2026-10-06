# Task Management API

API REST para la gestión de tareas desarrollada con FastAPI.

## Instalación

### 1. Crear entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar la aplicación

Puedes usar cualquiera de estos comandos:

```bash
# Opción 1: Comando moderno de FastAPI (recomendado)
fastapi dev main.py

# Opción 2: Uvicorn tradicional
uvicorn main:app --reload
```

La API estará disponible en `http://localhost:8000`

## Endpoints

- `GET /` - Información de la API

    ### Response
    ```json 
        {
            "message": "Task Management API"
        }
    ```

- `POST /tasks/` - Crear una nueva tarea
    
    ### Request
    *** Codigo: 200 Ok ***

    ```json 
    {
        "titulo": "Cambiar dolares",
        "contenido": "Ir al banco para cambiar Euros",
        "deadline": "2026-10-04"
    }
    ```
    ### Reponse
    *** Codigo: 201 Created ***

    ```json
        {
        "id": 1,
        "titulo": "Cambiar dolares",
        "contenido": "Ir al banco para cambiar Euros",
        "deadline": "2026-10-04",
        "completada": false,
        "fecha_creacion": "2026-10-02T20:15:00"
        }
    ```

    ### Errores
    400 : El deadline no puede estar en el pasado
    422 : Invalidos datos de entrada

- `GET /tasks/{task_id}` - Obtener una tarea por ID

    ### Parametros
    Nombre: task_id
    Tipo: int
    Descripcion: Identificador de la tarea

    ### Reponse
    *** Codigo: 200 Ok ***

    ```json
        {
        "id": 1,
        "titulo": "Cambiar dolares",
        "contenido": "Ir al banco para cambiar Euros",
        "deadline": "2026-10-04",
        "completada": true,
        "fecha_creacion": "2026-10-02T20:15:00"
        }
    ```

    ### Errores
    404 : Tarea no encontrada


- `PUT /tasks/{task_id}/completar` - Marcar una tarea como completada

    ### Request
    ```json
        {
        "completada": true
        }
    ```
    ### Response
    *** Codigo: 200 Ok ***

    ```json
        {
        "id": 1,
        "titulo": "Cambiar dolares",
        "contenido": "Ir al banco para cambiar Euros",
        "deadline": "2026-10-04",
        "completada": false,
        "fecha_creacion": "2026-10-02T20:15:00"
        }
    ```
    ### Errores
    404 : Tarea no encontrada

- `GET /tasks/caducadas` - Obtener lista de tareas caducadas

    ### Response
    *** Codigo: 200 Ok ***

    ```json
        {
        "id": 1,
        "titulo": "Impuestos",
        "contenido": "Llenar y entragar formulario de impuestos",
        "deadline": "2026-09-14",
        "completada": false,
        "fecha_creacion": "2026-09-02T22:19:00"
        }
    ```

- `DELETE /tasks/{task_id}/eliminar` - Eliminar tarea

    ### Parametros
    Nombre: task_id
    Tipo: int
    Descripcion: Identificador de la tarea

    ### Reponse
    *** Codigo: 200 Ok ***

    ```json
        {
        "id": 2,
        "titulo": "Compras",
        "contenido": "Ir al mercado",
        "deadline": "2025-11-04",
        "completada": false,
        "fecha_creacion": "2025-11-02T20:15:00"
        }
    ```
    ### Errores
    404 : Tarea no encontrada

## Ejecutar tests

```bash
python test_api.py
```

## Documentación interactiva

Una vez ejecutando la aplicación, puedes acceder a:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
