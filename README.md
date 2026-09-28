# Student CRUD Application

## Description

This project is a Student CRUD REST API
built using FastAPI.

## Features

- Create Student
- Get All Students
- Get Student by ID
- Update Student
- Delete Student

## Technologies

- Python
- FastAPI
- Uvicorn
- Pydantic

## Storage

The project uses local in-memory storage.
No database is used.

## Installation

Install the required libraries:

pip install -r requirements.txt

## Run Application

uvicorn main:app --reload

## Swagger Documentation

Open:

http://127.0.0.1:8000/docs