# bank_app_project
bank_app_project

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/felooh/bank_app_project.git
$ cd bank_account
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies run the following command
```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```

Once `migrations` have finished:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.


## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test account
```
BY FELIX G
# bank_app_project
