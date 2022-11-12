# Bank security console

It's connects to Database and display info about visitors in storage: name, duration, who in storage now, etc.

How to install
------

Python3 should already be installed. Use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
    pip install -r requirements.txt
```

For using you need your `SECRET KEY` for Database.

You should use environment variables. Create file name `.env` and variables `SECRET_KEY` in the root directory.
In file `.env` only one line:

```
SECRET_KEY='here is your SECRET KEY'
```
If the code starting on the local computer: 

Command line command:
```
$ python manage.py runserver
```
The result can be viewed [here](http://127.0.0.1:8000/)

Project Goals
------
This code was written for educational purposes as part of an online course for web developers at dvmn.org.



