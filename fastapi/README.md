# FastAPI Todo API
A RESTful todo API built with **FastAPI** and **SQLAlchemy**. It provides CRUD operations for managing tasks and uses SQLite as its default database.

## Features
- Create, read, update, and delete todo items
- Search todos by task name
- Filter todo operations by item ID
- Interactive API documentation with Swagger UI
- SQLAlchemy ORM database integration
- Automatic SQLite database and table creation

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite

## Project Structure
```text
fastapi/
|-- db/
|   |-- db_config.py
|   |-- models.py
|   `-- schema.py
|-- .env.example
|-- main.py
|-- requirements.txt
`-- todo.db
```

## Getting Started

### Prerequisites
- Python 3.9 or newer
- `pip`

### Installation
From the repository root:
```bash
cd fastapi
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

On Windows, activate the virtual environment with:
```powershell
.venv\Scripts\activate
```

### Run the API
```bash
fastapi dev main.py
```

The API will be available at `http://127.0.0.1:8000`.

Interactive documentation is available at:
- Swagger UI: `http://127.0.0.1:8000/docs`

## API Endpoints
| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Get all todo items |
| `GET` | `/{id}` | Get a todo item by ID |
| `POST` | `/add` | Create a todo item |
| `PUT` | `/edit/{id}` | Update a todo item |
| `DELETE` | `/delete/{id}` | Delete a todo item |
| `GET` | `/search/?task=<text>` | Search todo items by task text |

## Request Examples
- Create a todo:
```bash
curl -X POST "http://127.0.0.1:8000/add" \
  -H "Content-Type: application/json" \
  -d '{
    "task": "Learn FastAPI",
    "description": "Build and document a REST API",
    "done": false
  }'
```

- Get all todos:
```bash
curl "http://127.0.0.1:8000/"
```

- Update a todo:
```bash
curl -X PUT "http://127.0.0.1:8000/edit/1" \
  -H "Content-Type: application/json" \
  -d '{
    "task": "Learn FastAPI",
    "description": "Completed the REST API",
    "done": true
  }'
```

- Delete a todo:
```bash
curl -X DELETE "http://127.0.0.1:8000/delete/1"
```

- Search todos:
```bash
curl "http://127.0.0.1:8000/search/?task=Learn"
```

## Todo Data Model
```json
{
  "id": 1,
  "task": "Learn FastAPI",
  "description": "Build and document a REST API",
  "done": false
}
```

## Database
The application uses SQLite and stores data in `todo.db` by default. SQLAlchemy creates the database and `items` table automatically when `main.py` starts.
