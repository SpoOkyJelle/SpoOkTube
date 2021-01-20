# SpoOkTube
Video sharing

## Windows
Make sure you have pip and python installed, and a database server with the SQL file.

First download the project and extract it where you want it.
Then open a terminal.
To install the dependecies.

```bash
pip install -r requirements.txt 
```

```bash
python app.py
```

Then the server will be running on localhost:5000

## Linux

Make sure you have pip and python installed, and a database server with the SQL file.
 
First clone the file from github

```bash
git clone https://github.com/SpoOkyJelle/SpoOkTube.git
cd SpoOkTube
```

From here we need to activate the project.

```bash
python3 -m venv SpoOkTube
source SpoOkTube/bin/activate
```

After that we need to install install the dependencies to run the application.

```bash
pip install wheel
pip install gunicorn flask
```


Before we can run the app we need to tell the flask app that it can allow a connection from anywhere.
```bash
sudo nano app.py
```

Change the following code from:
```python
if __name__ == "__main__":
  app.run(debug=True)
```
To this:
```python
if __name__ == "__main__":
  app.run(host='0.0.0.0')
```


Be sure to change to the correct database. (SQL file included in repo).
Change the user, password and host. The database name should be the same as listed below.
```bash
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'python_youtubeclone'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
```


Then we will allow the port 5000 and run the app.

```bash
sudo ufw allow 5000
python app.py
```