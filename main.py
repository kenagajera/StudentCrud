from fastapi import FastAPI

from routes.student_routes import router


app = FastAPI(
    title="Student CRUD Application"
)


app.include_router(router)