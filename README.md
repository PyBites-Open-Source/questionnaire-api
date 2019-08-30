<p align="center">
  <img src="./logo/opentrivia.png" width="220">
</p>

[![Open Issues](https://img.shields.io/github/issues/code-monk08/opentrivia?style=for-the-badge)](https://github.com/code-monk08/opentrivia/issues) [![Forks](https://img.shields.io/github/forks/code-monk08/opentrivia?style=for-the-badge)](https://github.com/code-monk08/opentrivia/network/members) [![Stars](https://img.shields.io/github/stars/code-monk08/opentrivia?style=for-the-badge)](https://github.com/code-monk08/opentrivia/stargazers) 


## :ledger: Index

- [About](#beginner-about)
- [Usage](#zap-usage)
  - [Installation](#electric_plug-installation)
  - [Commands](#package-commands)
- [File Structure](#file_folder-file-structure)
- [Guideline](#exclamation-guideline)  
- [Resources](#page_facing_up-resources)
- [Gallery](#camera-gallery)
- [Endpoints](#busstop-Endpoints)
- [Credit/Acknowledgment](#star2-creditacknowledgment)
- [License](#lock-license)

##  :beginner: About
This will be a free to use, open sourced trivia questions database which has an API implemented in Python3 & Flask using PostgresSQL db.

## :zap: Usage
To use this project.

###  :electric_plug: Installation
- Install dependencies & export environment variables.

```bash
$ pip3 install -r requirements.txt
$ export FLASK_APP="run.py"
$ export FLASK_ENV=development
$ export APP_SETTINGS="development"
$ export DATABASE_URL="postgresql://localhost/flask_api"
```
###  :package: Commands
- Make sure to run this command before starting ```run.py```
```bash
$ sudo -i -u postgres
```
- Start project using
```bash
$ flask run.py
```

##  :file_folder: File Structure
- Add a file structure here with the basic details about files, below is an example.

```
.
├── app
│   ├── __init__.py
│   └── models.py
├── instance
│   ├── config.py
│   └── __init__.py
├── LICENSE
├── logo
│   └── opentrivia.png
├── manage.py
├── README.md
├── requirements.txt
├── run.py
└── test_opentrivia.py

```

| No | File Name | Details 
|----|------------|-------|
| 1  | app\/\_\_init\_\_.py | home for `create_app()` function definition which wraps creation of new flask object and all API endpoints.
| 2  | app\/models.py | home for `OpenTrivia` class which represents Trivia table.
| 3  | instance\/config.py | home for configuration (development, testing, staging, production) settings. 
| 4  | run.py | entry point to start our app.
| 5  | test_opentrivia.py | home for unit tests for our API.

##  :exclamation: Guideline

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

##  :page_facing_up: Resources
- [Flask-API](http://www.flaskapi.org/) : Flask API is a drop-in replacement for Flask that provides an implementation of browsable APIs similar to what [Django REST framework](http://www.django-rest-framework.org) provides.

##  :camera: Gallery
`Todo`

## :busstop: Endpoints
`Todo`

## :star2: Credit/Acknowledgment
[![Contributors](https://img.shields.io/github/contributors/code-monk08/opentrivia?style=for-the-badge)](https://github.com/code-monk08/opentrivia/graphs/contributors)

##  :lock: License
[![License](https://img.shields.io/github/license/code-monk08/opentrivia?style=for-the-badge)](https://github.com/code-monk08/opentrivia/blob/master/LICENSE)
