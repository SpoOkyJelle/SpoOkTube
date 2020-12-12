from flask import Flask, flash, render_template, request, redirect, url_for, session
from flaskext.mysql import MySQL
from datetime import time, timedelta
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.secret_key = "youtubeclone"
app.permanent_session_lifetime = timedelta(days=5)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'python_youtubeclone'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


# [ ] rework css
#   [x] login page style
#   [ ] add dark theme
# [ ] comments
#   [x] view comments
#   [ ] add comments
#   [ ] react to comments
# [ ] make dark theme toggelable
# [ ] video upload
# [x] rework sql query's
# [x] login
# [x] login bad password
# [x] account view (logout and stuff)


@app.route("/")
def home():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM `videos` INNER JOIN `channels` ON `videos`.`channel_id` = `channels`.`id`")
    data = cursor.fetchall()
    
    
    userinfo=None
    if "user" in session:
        sql = "SELECT * FROM `channels` WHERE `channel_name` = %s"
        cursor.execute(sql, (session['user'],))
        userinfo = cursor.fetchall()
    else:
        userinfo=None

    return render_template('homepage.html', data=data, userinf=userinfo)


@app.route("/channel/<channel>")
def channel(channel):
    conn = mysql.connect()
    cursor = conn.cursor()

    query = "SELECT * from `channels` WHERE `channel_name` = %s"
    cursor.execute(query, (channel,))
    
    data = cursor.fetchall()
    
    id = 0
    for row in data:
        id = row[0]
    
    videoquery = "SELECT * from `videos` WHERE `channel_id` = %s ORDER BY `created_at` DESC"
    cursor.execute(videoquery, (id,))

    videos = cursor.fetchall()
    
    userinfo=None
    if "user" in session:
        sql = "SELECT * FROM `channels` WHERE `channel_name` = %s"
        cursor.execute(sql, (session['user'],))
        userinfo = cursor.fetchall()
    else:
        userinfo=None
    
    return render_template('channel.html', data=data, videos = videos, userinf=userinfo)


@app.route("/search", methods = ['POST'])
def search():
    conn = mysql.connect()
    cursor = conn.cursor()

    query = request.form['search']
    searchString = '%' + query + '%'

    sql = "SELECT * FROM `videos`  INNER JOIN `channels` ON `videos`.`channel_id` = `channels`.`id` WHERE `video_title` LIKE %s OR `video_desc` LIKE %s OR `video_url` LIKE %s"
    cursor.execute(sql, (searchString, searchString, searchString,))

    data = cursor.fetchall()
    
    userinfo=None
    if "user" in session:
        sql = "SELECT * FROM `channels` WHERE `channel_name` = %s"
        cursor.execute(sql, (session['user'],))
        userinfo = cursor.fetchall()
    else:
        userinfo=None
    return render_template('searchpage.html', data=data, userinf=userinfo)


@app.route("/video/<id>", methods=['GET'])
def videoPage(id):
    conn = mysql.connect()
    cursor = conn.cursor()

    sql = "SELECT * FROM `videos` INNER JOIN `channels` ON `videos`.`channel_id` = `channels`.`id` WHERE `videos`.`id` = %s"
    cursor.execute(sql, (id,))
    data = cursor.fetchall()
    
    videosql = "SELECT * FROM `comments` INNER JOIN `channels` ON `comments`.`channel_id` = `channels`.`id` WHERE `video_id` = %s"
    cursor.execute(videosql, (id,))
    comments = cursor.fetchall()
    
    videoid=0
    for video in data:
        videoid=video[0]
        
    viewcount = "UPDATE `videos` SET `video_views` = `video_views` + 1 WHERE `id` = %s"
    cursor.execute(viewcount, (videoid,))
    
    userinfo=None
    if "user" in session:
        sql = "SELECT * FROM `channels` WHERE `channel_name` = %s"
        cursor.execute(sql, (session['user'],))
        userinfo = cursor.fetchall()
    else:
        userinfo=None

    return render_template('videopage.html', data=data, userinf=userinfo, comments=comments)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        conn = mysql.connect()
        cursor = conn.cursor()
        session.permanent = True

        channelname = request.form['channel_name']
        channelpass = request.form['channel_pass']

        channelquery = "SELECT * from `channels` WHERE `channel_name` = %s"
        cursor.execute(channelquery, (channelname,))
        databasepass = cursor.fetchall()

        if not databasepass:
            flash('Wrong username or password')
            return redirect(url_for('login'))
        else:
            if sha256_crypt.verify(channelpass, databasepass[0][2]):
                session["user"] = channelname
                return redirect(url_for('channel', channel=channelname))
            else:
                flash('Wrong username or password')
                return redirect(url_for('login'))
    else:
        if "user" in session:
            return redirect(url_for('channel', channel=channelname))
        
        return render_template('login.html')


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
