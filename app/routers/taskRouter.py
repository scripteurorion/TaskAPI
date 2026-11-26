from fastapi import APIRouter
from services.taskServices import service
from shema.schema import Task, CreateTask, UpdateTask

router = APIRouter(prefix="/tasks", tags=["Task"])

@router.get("/", response_model=list[Task])
def lists():
    return service.list_tasks()

@router.post("/", response_model=Task)
def create(data : CreateTask):
    return service.create_task(data)

@router.get("/{task_id}", response_model=Task)
def read_task(task_id: int):
    return service.get_task(task_id)

@router.patch("/{task_id}", response_model=Task)
def update_task(task_id: int, data : UpdateTask):
    return service.edit_task(task_id, data)

@router.post("/{task_id}/end", response_model=Task)
def end(task_id: int):
    return service.end_task(task_id)

@router.put("/{task_id}", response_model=Task)
def replace(task_id: int, data : CreateTask):
    return service.replace_task(task_id, data)

@router.delete("/{task_id}")
def delete(task_id: int):
    return service.delete_task(task_id)