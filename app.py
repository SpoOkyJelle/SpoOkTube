from flask import Flask, render_template, request, redirect, url_for, session
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'python_youtubeclone'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/")
def hello():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * from `videos`")
    data = cursor.fetchall()

    return render_template('homepage.html', data=data)


@app.route("/search", methods = ['POST' ])
def search():
    conn = mysql.connect()
    cursor = conn.cursor()
    
    query = request.form['search']
    searchString = '%' + query + '%'

    sql = "SELECT * FROM `videos` where video_title LIKE %s OR video_desc LIKE %s OR video_url LIKE %s OR video_creator LIKE %s"
    cursor.execute(sql, (searchString, searchString, searchString, searchString,))

    data = cursor.fetchall()
    return render_template('searchpage.html', data=data)


@app.route("/video/<id>", methods=['GET'])
def videoPage(id):
    conn = mysql.connect()
    cursor = conn.cursor()

    query = "SELECT * from `videos` WHERE `id` = %s"
    cursor.execute(query, (id,))

    data = cursor.fetchall()
    return render_template('videopage.html', data=data)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template('login.html')

    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
