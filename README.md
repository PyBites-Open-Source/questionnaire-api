<p align="center">
  <img src="./logo/opentrivia.png" width="220">
</p>

[![Open Issues](https://img.shields.io/github/issues/PyBites-Open-Source/questionnaire-api?style=for-the-badge)](https://github.com/PyBites-Open-Source/questionnaire-api/issues) [![Forks](https://img.shields.io/github/forks/PyBites-Open-Source/questionnaire-api?style=for-the-badge)](https://github.com/PyBites-Open-Source/questionnaire-api/network/members) [![Stars](https://img.shields.io/github/stars/PyBites-Open-Source/questionnaire-api?style=for-the-badge)](https://github.com/PyBites-Open-Source/questionnaire-api/stargazers) ![Build](https://img.shields.io/travis/PyBites-Open-Source/questionnaire-api?style=for-the-badge) ![Maintained](https://img.shields.io/maintenance/yes/2019?style=for-the-badge&logo=github)  ![Made with Python](https://img.shields.io/badge/Made%20with-Python-blueviolet?style=for-the-badge&logo=python)  ![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%99%A5-red?style=for-the-badge&logo=open-source-initiative)  ![Built with Love](https://img.shields.io/badge/Built%20With-%E2%99%A5-critical?style=for-the-badge&logo=ko-fi) [![PyBites/Opentrivia](https://img.shields.io/badge/PyBites%2FOpentrivia-Chat-success?logo=slack&style=for-the-badge)](https://app.slack.com/client/T4SJVFM8C/CMYR582R4)

`THIS PROJECT IS UNDER ACTIVE DEVELOPMENT, README MAY CHANGE EVERY ONCE IN A WHILE`


## Index

- [Index](#index)
- [About](#about)
- [Usage](#usage)
  - [Installation](#installation)
- [File Structure](#file-structure)
- [Guideline](#guideline)
- [Gallery](#gallery)
- [Endpoints](#endpoints)
- [Credit/Acknowledgment](#creditacknowledgment)
- [License](#license)

## About
This will be a free to use, open sourced questions database which has an API implemented in Python3 & Flask using PostgresSQL database, also this will be a source for a minimal quizzing website which will also let contributors add new questions in multiple categories and as MCQ or T/F types. 

## Usage
To use this project.

### Installation

**Development**

If you want just to do a simple test run of the application, you can install and use it 
with development config.

- Clone the repository

```bash
$ git clone https://github.com/PyBites-Open-Source/questionnaire-api.git
```

- Create the virtualenv and activate it

```bash
$ cd questionnaire-api
$ python -m venv virtualenv
$ source virtualenv/bin/activate # unix
$ .\virtualenv\Scripts\activate  # windows
```

- Instal requirements

```bash
$ pip3 install -r requirements.txt
```
- Create database and apply migrations

```
$ flask db upgrade
```  

- Run the application

```bash
$ flask run
```
**Production**

In order to use postgresql database ready for production, you need to use docker and to add some additional environment variables. 

- Setup database 

```bash
# create .env file with the following environment variables. 
POSTGRES_USER="trivia"
POSTGRES_PASSWORD="trivia"
POSTGRES_DB_PROD="opentrivia_prod"
POSTGRES_DB_TEST="opentrivia_test"
DB_PORT="5432"
DB_HOST="localhost"

# if you want to change these settings you have to change also the init.sql file 
# from db folder. 
```

- Run the application

```bash
$ docker-compose up
```

## File Structure
- Add a file structure here with the basic details about files, below is an example.

```
.
├── app
│   ├── api
│   │   ├── __init__.py
│   │   └── resources.py
│   ├── __init__.py
│   ├── models.py
│   ├── static
│   │   └── swagger.json
│   ├── templates
│   │   ├── base.html
│   │   ├── developer.html
│   │   └── home.html
│   └── views.py
├── config.py
├── _config.yml
├── CONTRIBUTING.md
├── db
│   └── init.sql
├── docker
│   ├── api-server
│   │   └── Dockerfile
│   └── db-server
│       └── Dockerfile
├── docker-compose.yml
├── instance
│   └── dev_opentrivia.db
├── LICENSE
├── logo
│   └── opentrivia.png
├── manage.py
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── d3595c7e8e54_.py
├── README.md
├── requirements.txt
├── run.py
└── tests
    ├── __init__.py
    └── test_opentrivia.py

13 directories, 30 files
```

| No | File Name  | Details 
|----|------------|-------|
| 1  | app\/\_\_init\_\_.py | home for `create_app()` function definition which wraps creation of new flask object and all API endpoints.
| 2  | app\/models.py | home for models used in `OpenTrivia`. 
| 3  | app\/views.py | This module will contain the routes to our app interface.
| 4  | run.py | entry point to start our app.
| 5  | test_opentrivia.py | home for unit tests for our API.

## Guideline

- __Code Style__

In order to maintain the code style consistency across entire project we use a code formatter. Therefore, we kindly suggest you to do the same whenever you push commits to this project. 

The python code formatter we chose is called black. Black is a great tool and it can be installed quickly by running 

`pip install black`.  

or

`python3.6 -m pip install black`

It requires Python 3.6.0+ to run.

- __Usage__

`black {source_file_or_directory}`

For more details and available options, please check the [GitHub project](https://github.com/psf/black).

- __Close Issues__

Close issues using keywords: [how to ?](https://help.github.com/en/articles/closing-issues-using-keywords)

## Gallery
`Todo`

## Endpoints

`Available Views`
- [x] http://127.0.0.1:5000/            #Home Page
- [x] http://127.0.0.1:5000/developer   #Developer Page
- [x] http://127.0.0.1:5000/swagger/    #Swagger UI

`Todo`
- [ ] Add a question 
- [ ] Add answer(s) to a question
- [ ] Update a question
- [ ] Update answer(s)
- [ ] Delete a question (along with its answers)
- [ ] Delete an answer
- [ ] Get question(s)
- [ ] Get all question(s) & their answer(s)
- [ ] Get question category
- [ ] Get question level (easy \| medium \| hard )
- [ ] Get type of question (MCQ \| T/F)



feel free to add more functionalities
endpoint url structure:  **/api/v1/. . .**

## Credit/Acknowledgment
[![Contributors](https://img.shields.io/github/contributors/PyBites-Open-Source/questionnaire-api?style=for-the-badge)](https://github.com/PyBites-Open-Source/questionnaire-api/graphs/contributors)

## License
[![License](https://img.shields.io/github/license/PyBites-Open-Source/questionnaire-api?style=for-the-badge)](https://github.com/PyBites-Open-Source/questionnaire-api/blob/master/LICENSE)
