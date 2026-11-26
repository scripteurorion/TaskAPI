from fastapi import FastAPI, Request
from routers.taskRouter import router
from fastapi.responses import JSONResponse
from exceptions.exceptions import ErreurMetier, TaskEnd, TaskNotFound


app = FastAPI(title="My API for Task management")
app.include_router(router)

@app.exception_handler(TaskNotFound)
async def task_not_found_handler(request: Request, exc: TaskNotFound):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc)},
    )


@app.exception_handler(TaskEnd)
async def task_end_handler(request: Request, exc: TaskEnd):
    return JSONResponse(
        status_code=409,
        content={"detail": str(exc)},
    )