## Context

<br>

**Jellyfish_case_Backend** is a case study for Back End recruitment for an internship. The challenge is to create a simple cryptocurrency notification app using the [CoinAPI](https://docs.coinapi.io/). I tried it without any knowledge in how to create an API. Indeed, after a DataScience bootcamp, we learn how to use an api to get data but, we dont learn how to create it. Thats why, even if the challenge is not finished on time before job interview, it was really rewarding to try to complete it.

<br>

## Tools Used

👉 [FastAPI](https://fastapi.tiangolo.com/) web framework with swagger.UI platform

👉 [SQLalchemy](https://www.sqlalchemy.org/) data management

👉 [Tortoise-ORM](https://tortoise.github.io/) data management


<br>

## Summary

1. Initialize my [Repository Github for Jellyfish_Case_Backend](https://github.com/jbguerin13/jellyfish_case_backend)
2. Watching Tutorials and Reading documentation
3. Initialize app_user_auth directory
4. Create a crud for user with authentification by JWTtokens
5. Initialize app_DB_work directory trying to connect a db to the api
6. Create a Docker container and push it in production with GCP
7. Going further 👉 finish the project trying to use an other web framework (flaskAPI, django etc)


<br>

# 1️⃣ Challenge Setup 🛠

##  Jellyfish_Case_Backend directory

I've created my working environment diagrammed by this tree directory

```bash
.
├── app_DB_work                     # crud user with database
│   ├── config.py                   # config the db
│   ├── crud.py                     # define crud
│   ├── main.py                     # run app
│   ├── model.py                    # define db table
│   ├── router.py                   # define routes
│   └── schema.py                   # define schema BaseModel
├── app_user_auth                   # crud user with authentification
│   ├── auth                        # manage JWT files and functions
│   │   ├── jwt_bearer.py           # verify JWT
│   │   └── jwt_handler.py          # signing JWT
│   ├── database.py                 # Trying manage data without ORM
│   ├── init_db.py                  # Crush db
│   ├── mains.py                    # Define route, crud and run app
│   ├── models.py
│   └── schemas.py                  # Define Schema BaseModel
├── coin_api.py                     # request the value of BTC in $ from CoinAPI.io
├── database.sql                    # database
├── README.md                       # Describe the challenge
├── requirements.txt                # all the dependencies I need to run
```
<br>

# 2️⃣  Trying to creat a crud for user with authentification JWT


<br>

For this part, I tried to create a secure app with authentification.
After this step where the result was providing, I tried to connect with a db and applied migration without good results.
I didnt understand yet how to use correctly a database-ORM. Thats why I tried  an "old school" technic with using a bd diagram
defining tables and foreign keys and try to link the export to the app with sqlite.
But the queries transfert to each crud was hard i'm currently try to debug it.
<br>

# 3️⃣ Trying to creat a simple crud for user with a database-ORM (SQLalchemy)

Frustrated by the part above and having failed to connect a database to my crud, I decided to create a new app with the db-ORM system, following a very precise tutorial on youtube and trying to replace the example with my own case.


# Conclusion

I'm aware that my work isn't finished in its current state before the interview, but I'd like to highlight that I've learned many notions in a very short space of time, and that it's important for me to try and come to terms with it over the next few days.


# Readme

## Getting started

### Prerequisites
Install poetry and pyenv:
```bash
curl -sSL https://install.python-poetry.org | python3 -
poetry config virtualenvs.in-project true

brew install pyenv make
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

Install python 3.11.0 and ask poetry to use it
```bash
pyenv install 3.11.0
pyenv local 3.11.0
poetry env use 3.11.0
```

### Install dependencies
```bash
poetry install
```

### Add a new package
```bash
poetry add package_name
```

### Run tests
```bash
poetry run pytest
```
or by watching file changes
```bash
poetry run pytest-watch
```

### Run linter
```bash
poetry run black src
poetry run pylint src
poetry run mypy src
```

### Run
```bash
poetry run uvicorn api.entrypoint:app --reload
```
