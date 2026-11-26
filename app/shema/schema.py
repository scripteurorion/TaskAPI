from pydantic import BaseModel, Field, field_validator

class CreateTask(BaseModel):
    title : str | None = Field(min_length=3, max_length=100)
    description : str | None = Field(min_length=3, max_length=100)
    prority : int | None = Field(default=1, ge=1, le=5)

    @classmethod
    @field_validator("title")
    def title_validator(cls, value: str | None) -> str | None:
        if value.strip() == "":
            raise ValueError("title must not be empty")
        return value
    @classmethod
    @field_validator("description")
    def description_validator(cls, value: str | None) -> str | None:
        if value.strip() == "":
            raise ValueError("description must not be empty")
        return value

class Task(CreateTask):
    id : int
    end : bool | None = Field(default=False)

class UpdateTask(BaseModel):
    title : str | None = None
    description : str | None = None
    prority : int | None = Field(default=1, ge=1, le=5)
    end : bool | None = Field(default=False)

    @classmethod
    @field_validator("title")
    def title_validator(cls, value: str | None) -> str | None:
        if value.strip() == "":
            raise ValueError("title must not be empty")
        return value
    @classmethod
    @field_validator("description")
    def description_validator(cls, value: str | None) -> str | None:
        if value.strip() == "":
            raise ValueError("description must not be empty")
        return value