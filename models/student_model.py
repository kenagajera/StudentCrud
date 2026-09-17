from pydantic import BaseModel, EmailStr


class Student(BaseModel):

    id: int | None = None

    name: str

    email: EmailStr

    course: str

    semester: int