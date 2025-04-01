# Space Infinity Intern Startup School

## [Precondition]
PostgreSQL (database system) needs to be installed. The following page shows how to install it on your local environment:
https://www.w3schools.com/postgresql/postgresql_install.php



## [Setup]
### .env

Create the `.env` file in the `frontend` and `backend` directory with the following contents:

`frontend/.env`
```
FRONTEND_ORIGIN = "http://0.0.0.0:5001"
BACKEND_ORIGIN = "http://127.0.0.1:8000"
```

`backend/.env`
```
DATABASE_URL="postgresql://postgres:postgres@localhost:5432/space_infinity_intern_startup_school"
```

Note that the following variable should be changed to match your local setup:
- `DATABASE_URL`: postgresql://<user>:<password>@localhost:<port>/<dbname>?schema=schema


### Install packages

Execute the following commands:

frontend
```
cd frontend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate
python3 api/main.py
```

backend
```
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate
python3 -m api.app
```
