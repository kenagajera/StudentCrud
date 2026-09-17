from models.student_model import Student
from fastapi import Response


students = []

Id = 0


# CREATE STUDENT
def create_student_controller(
    student: Student,
    response: Response
):

    global Id

    try:

        Id += 1

        student.id = Id

        students.append(student)

        response.status_code = 201

        return {
            "isSuccess": True,
            "message": "Student created successfully",
            "student": student
        }

    except Exception as e:

        print(e)

        response.status_code = 500

        return {
            "message": "Error creating student",
            "isSuccess": False
        }


# GET ALL STUDENTS
def get_student_controller(response: Response):

    try:

        print("data -> ", students)

        response.status_code = 200

        return {
            "message": "Students get successfully!",
            "students": students,
            "isSuccess": True
        }

    except Exception as e:

        print(e)

        response.status_code = 500

        return {
            "message": "Error fetching students",
            "isSuccess": False
        }


# GET STUDENT BY ID
def get_student_controller_id(
    studentid: int,
    response: Response
):

    try:

        for student in students:

            if student.id == studentid:

                response.status_code = 200

                return {
                    "student": student,
                    "isSuccess": True
                }

        response.status_code = 404

        return {
            "message": "Student not found",
            "isSuccess": False
        }

    except Exception as e:

        print(e)

        response.status_code = 500

        return {
            "message": "Error fetching student",
            "isSuccess": False
        }


# UPDATE STUDENT
def update_student_controller(
    studentid: int,
    student: Student,
    response: Response
):

    try:

        for index, old_student in enumerate(students):

            if old_student.id == studentid:

                student.id = studentid

                students[index] = student

                response.status_code = 200

                return {
                    "message": "Student updated successfully",
                    "student": student,
                    "isSuccess": True
                }

        response.status_code = 404

        return {
            "message": "Student not found",
            "isSuccess": False
        }

    except Exception as e:

        print(e)

        response.status_code = 500

        return {
            "message": "Error updating student",
            "isSuccess": False
        }


# DELETE STUDENT
def delete_student_controller(
    studentid: int,
    response: Response
):

    try:

        for index, student in enumerate(students):

            if student.id == studentid:

                students.pop(index)

                response.status_code = 204

                return None

        response.status_code = 404

        return {
            "message": "Student not found",
            "isSuccess": False
        }

    except Exception as e:

        print(e)

        response.status_code = 500

        return {
            "message": "Error deleting student",
            "isSuccess": False
        }