## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Features](#features)
* [Setup](#setup)

## General info
A social media platform for penguins. 

## Screenshots
Login page
![Pogin page screenshot](/Screenshots/login-page.png?raw=true "Login page")

Feed
![Feed screenshot](/Screenshots/feed.png?raw=true "Feed page")

## Features
Register/ login

Add friends

Make posts

Like posts

Comment posts

View personal profile pages

Infinity scroller through post feed
	
## Technologies
Project is created with:
* Python 3.8
* Flask 1.1.2
* Pymongo 3.11.2
* HTML
* CSS
* Javascript
* Jquery
* Bootstrap 3
	
## Setup
To run this project ...


## Build from sources - to be updated.....

```bash
$ # Clone the sources
$ git clone https://github.com/VictorOlof/penguin_community.git
$ cd ...
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install requirements
$ pip3 install -r requirements.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Run the Jinja Template
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the UI in browser: http://127.0.0.1:5000/
```

<br />
