# Space Infinity Intern Startup School

## [Precondition]
Make sure PostgreSQL (a database system) is installed on your machine. You can find installation instructions here:
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

Note: Adjust the following variable to match your local setup:
- `DATABASE_URL`: postgresql://<user>:<password>@localhost:<port>/<dbname>


### Install packages

Run the following commands to install the necessary packages:

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
