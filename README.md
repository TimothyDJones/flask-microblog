# Flask Microblog

Files for the [Flask Mega-Tutorial series](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

To configure environment, in the root directory, run the following at the command prompt:
```console
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```
Then run the following to create/populate the **development** SQLite database via the [Flask-Migrate](https://github.com/miguelgrinberg/flask-migrate) database migrations:
```console
flask db upgrade
```

To run the application, run the following at command prompt:
```console
export FLASK_APP=microblog.py
flask run
```
