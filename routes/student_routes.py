from fastapi import APIRouter, Response

from models.student_model import Student

from controllers.student_controllers import (
    create_student_controller,
    get_student_controller,
    get_student_controller_id,
    update_student_controller,
    delete_student_controller
)


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# CREATE
@router.post("/")
def create_student(
    student: Student,
    response: Response
):

    return create_student_controller(
        student,
        response
    )


# GET ALL
@router.get("/")
def get_students(
    response: Response
):

    return get_student_controller(
        response
    )


# GET BY ID
@router.get("/{studentid}")
def get_student_by_id(
    studentid: int,
    response: Response
):

    return get_student_controller_id(
        studentid,
        response
    )


# UPDATE
@router.put("/{studentid}")
def update_student(
    studentid: int,
    student: Student,
    response: Response
):

    return update_student_controller(
        studentid,
        student,
        response
    )


# DELETE
@router.delete("/{studentid}")
def delete_student(
    studentid: int,
    response: Response
):

    return delete_student_controller(
        studentid,
        response
    )