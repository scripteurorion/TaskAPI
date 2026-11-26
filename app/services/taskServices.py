from shema.schema import Task, CreateTask, UpdateTask
from exceptions.exceptions import TaskEnd, TaskNotFound

class ServicesTasks:
    def __init__(self):
        self._task : dict[int, Task] = {}
        self.new_id = 1

    def create_task(self, data : CreateTask):
        task = Task(id=self.new_id, **data.model_dump())
        self._task[self.new_id] = task
        self.new_id += 1
        return task

    def list_tasks(self):
        tasks = list(self._task.values())
        return [t for t in tasks]

    def get_task(self, task_id):
        task = self._task.get(task_id)
        if task_id not in self._task:
            raise TaskNotFound(task_id)
        return task

    def edit_task(self, task_id, data : CreateTask):
        current = self.get_task(task_id)
        updated_data = current.model_copy(update=data.model_dump(exclude_unset=True))
        self._task[task_id] = updated_data
        return updated_data

    def replace_task(self, task_id, data : CreateTask):
        self.get_task(task_id)
        new_task = Task(id=task_id, **data.model_dump())
        self._task[task_id] = new_task
        return new_task

    def end_task(self, task_id):
        task = self.get_task(task_id)
        if task.end == True:
            raise TaskEnd(task_id)
        task.end = True
        return task

    def delete_task(self, task_id):
        d_task = self.get_task(task_id)
        del self._task[task_id]
        return d_task

service = ServicesTasks()