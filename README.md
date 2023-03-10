# django-social
Social Network Web App built by Django framework

App Home: https://django-social-ckmc.herokuapp.com/
<img width="1440" alt="social" src="https://user-images.githubusercontent.com/46878585/217751915-63256f25-25c1-4f49-b74c-ff23e0c1a7e1.png">

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/clementckmc/django-social.git
$ cd django-social
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
