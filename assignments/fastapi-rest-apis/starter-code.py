# Starter Code for FastAPI REST APIs Assignment

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# TODO: Create FastAPI application instance
# app = FastAPI(...)

# TODO: Define Task model using Pydantic BaseModel
# class Task(BaseModel):
#     id: int
#     title: str
#     description: str
#     completed: bool = False
#     created_at: datetime

# TODO: In-memory storage for tasks
# tasks_db: List[Task] = []

# Sample data - uncomment and modify as needed
# sample_tasks = [
#     {"id": 1, "title": "Learn FastAPI", "description": "Complete FastAPI tutorial", "completed": False, "created_at": "2025-10-24T10:30:00"},
#     {"id": 2, "title": "Build REST API", "description": "Create a task management API", "completed": False, "created_at": "2025-10-24T11:00:00"},
#     {"id": 3, "title": "Test API endpoints", "description": "Test all CRUD operations", "completed": False, "created_at": "2025-10-24T11:30:00"}
# ]

# TODO: Health check endpoint
# @app.get("/health")
# async def health_check():
#     return {"status": "healthy"}

# TODO: GET /tasks - Get all tasks
# @app.get("/tasks", response_model=List[Task])
# async def get_tasks():
#     return tasks_db

# TODO: GET /tasks/{task_id} - Get specific task
# @app.get("/tasks/{task_id}", response_model=Task)
# async def get_task(task_id: int):
#     # Find task by ID
#     # Raise HTTPException(404) if not found
#     pass

# TODO: POST /tasks - Create new task
# @app.post("/tasks", response_model=Task, status_code=201)
# async def create_task(task: Task):
#     # Add task to tasks_db
#     # Generate new ID
#     pass

# TODO: PUT /tasks/{task_id} - Update existing task
# @app.put("/tasks/{task_id}", response_model=Task)
# async def update_task(task_id: int, updated_task: Task):
#     # Find and update task
#     # Raise HTTPException(404) if not found
#     pass

# TODO: DELETE /tasks/{task_id} - Delete task
# @app.delete("/tasks/{task_id}")
# async def delete_task(task_id: int):
#     # Find and remove task
#     # Raise HTTPException(404) if not found
#     # Return success message
#     pass

# TODO: Run the application
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)