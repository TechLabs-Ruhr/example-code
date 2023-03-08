# Backend FastAPI Example

## Getting started
Open a terminal and navigate into this directory. Your command like should say something like `..../example-code/backend/`.

`python3 -m venv venv && source venv/bin/activate`

`pip3 install -r requirements.txt`

#### start python application

either via VSCode or via `python3 main.py`

Open http://127.0.0.1:8000/api/docs


## Structure
- Models -> Database Models ( SQLAlchemy )
- Schemas -> Serialization Schemas ( Pydantic )
- Routers -> Definition of API Endpoints
- crud -> Definition of Business Logic
