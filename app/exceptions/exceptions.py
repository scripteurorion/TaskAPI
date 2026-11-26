class ErreurMetier(Exception):
    ...

class TaskNotFound(ErreurMetier):
    def __init__(self, task_id):
        super().__init__(f"Task {task_id} not found")
        self.task_id = task_id

class TaskEnd(ErreurMetier):
    def __init__(self, task_id):
        super().__init__(f"Task {task_id} always done")
        self.task_id = task_id