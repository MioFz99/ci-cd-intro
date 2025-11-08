# TSP Solver

A minimal **Traveling Salesman Problem (TSP)** playground with a simple **web interface** and a **FastAPI backend**.  
You can place points on an interactive map, submit them to the backend, and receive a computed TSP route.

---

## Run the Application

### 1) Install dependencies
```bash
pip install -r requirements.txt
```
### 2) Start the backend
`uvicorn app.main:app --reload`
### 3) Open the UI
Navigate to http://localhost:8000/
### API docs
OpenAPI / Swagger UI is available at: http://localhost:8000/docs

## Tests
To run the test suite: `pytest`