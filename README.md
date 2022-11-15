# Bank security console

It's connects to Database and display info about visitors in storage: name, duration, who in storage now, etc.

How to install
------

Python3 should already be installed. Use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
    pip install -r requirements.txt
```

For using you need your `SECRET KEY` for Database.

You should use environment variables. Create file name `.env` and next variables in the root directory.
In file `.env` only one line:

```
SECRET_KEY='here is your SECRET KEY'
DEBUG=True or False
DB_HOST='...'
DB_PORT='...'
DB_NAME='...'
DB_USER='...'
DB_PASSWORD='...'
ALLOWED_HOSTS=''
```
Where `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` - your database settings.

`ALLOWED_HOSTS` - set according to [documentation](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts). Default value `localhost`.

If the code starting on the local computer: 

Command line command:
```
$ python manage.py runserver
```
The result can be viewed [here](http://127.0.0.1:8000/)

Project Goals
------
This code was written for educational purposes as part of an online course for web developers at dvmn.org.



