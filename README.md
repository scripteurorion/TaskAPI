# TaskAPI

A simple REST API for managing tasks, built with FastAPI and Pydantic.

## Requirements

- Python 3.10 or newer
- FastAPI
- Pydantic

## Installation

Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install -r requirement.txt
```

## Run the API

From the `app` directory:

```powershell
cd app
fastapi dev main.py
```

Open:

- API docs: http://127.0.0.1:8000/docs
- Alternative docs: http://127.0.0.1:8000/redoc

## API routes

| Method | Route | Description |
|---|---|---|
| `GET` | `/tasks/` | List all tasks |
| `POST` | `/tasks/` | Create a task |
| `GET` | `/tasks/{task_id}` | Get a task |
| `PATCH` | `/tasks/{task_id}` | Partially update a task |
| `PUT` | `/tasks/{task_id}` | Replace a task |
| `POST` | `/tasks/{task_id}/end` | Mark a task as completed |
| `DELETE` | `/tasks/{task_id}` | Delete a task |

## Task model

```json
{
  "title": "Learn FastAPI",
  "description": "Build and test the TaskAPI",
  "prority": 1
}
```

The API stores tasks in memory. Restarting the server resets all task data.
