# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework, implementing CRUD operations, data validation, and API documentation for a simple task management system.

## 📝 Tasks

### 🛠️ Setup FastAPI Application

#### Description

Create a basic FastAPI application with proper project structure and install the necessary dependencies.

#### Requirements

Completed program should:

- Install FastAPI and Uvicorn using pip
- Create a main FastAPI application instance
- Include a basic health check endpoint at `/health`
- Run the server on localhost port 8000
- Display automatic API documentation at `/docs`

### 🛠️ Task Model and Data Validation

#### Description

Define a Pydantic model for tasks and implement data validation for API requests and responses.

#### Requirements

Completed program should:

- Create a Task model with fields: id, title, description, completed (boolean), created_at
- Use Pydantic for automatic data validation
- Include proper type hints for all fields
- Set default values where appropriate
- Example task structure:

  ```json
  {
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Complete the FastAPI tutorial",
    "completed": false,
    "created_at": "2025-10-24T10:30:00"
  }
  ```

### 🛠️ CRUD Operations

#### Description

Implement Create, Read, Update, and Delete operations for tasks using proper HTTP methods and status codes.

#### Requirements

Completed program should:

- GET `/tasks` - Return all tasks
- GET `/tasks/{task_id}` - Return a specific task by ID
- POST `/tasks` - Create a new task
- PUT `/tasks/{task_id}` - Update an existing task
- DELETE `/tasks/{task_id}` - Delete a task
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Handle errors gracefully with proper error messages
- Use in-memory storage (list or dictionary) for data persistence

### 🛠️ API Testing and Documentation

#### Description

Test your API endpoints and explore the automatically generated documentation.

#### Requirements

Completed program should:

- Test all endpoints using the interactive documentation at `/docs`
- Verify that POST requests create new tasks correctly
- Confirm that GET requests return the expected data
- Test error scenarios (e.g., requesting non-existent task IDs)
- Include at least 3 sample tasks in your initial data

