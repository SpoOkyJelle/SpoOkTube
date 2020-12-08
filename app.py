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
# [ ] add dark theme
# [ ] make dark theme toggelable
# [x] login
# [x] login bad password
# [ ] account view (logout and stuff)
# [ ] video upload


@app.route("/")
def home():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM `videos` INNER JOIN `channels` ON `videos`.`channel_id` = `channels`.`id`")
    data = cursor.fetchall()

    return render_template('homepage.html', data=data)


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
    return render_template('channel.html', data=data, videos = videos)


@app.route("/search", methods = ['POST'])
def search():
    conn = mysql.connect()
    cursor = conn.cursor()
    
    query = request.form['search']
    searchString = '%' + query + '%'

    sql = "SELECT * FROM `videos` where video_title LIKE %s OR video_desc LIKE %s OR video_url LIKE %s"
    cursor.execute(sql, (searchString, searchString, searchString,))

    data = cursor.fetchall()
    return render_template('searchpage.html', data=data)


@app.route("/video/<id>", methods=['GET'])
def videoPage(id):
    conn = mysql.connect()
    cursor = conn.cursor()

    query = "SELECT * from `videos` WHERE `id` = %s"
    cursor.execute(query, (id,))
    
    data = cursor.fetchall()
    
    channelid=0
    videoid=0
    for video in data:
        channelid = video[1]
        videoid=video[0]
        
    channelquery = "SELECT * from `channels` WHERE `id` = %s"
    cursor.execute(channelquery, (channelid,))
    channel = cursor.fetchall()
    
    viewcount = "UPDATE `videos` SET `video_views` = `video_views` + 1 WHERE `id` = %s"
    cursor.execute(viewcount, (videoid,))

    return render_template('videopage.html', data=data, channel=channel)


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
        
        if sha256_crypt.verify(channelpass, databasepass[0][2]):
            session["user"] = channelname
            return redirect(url_for('channel', channel=channelname))
        else:
            flash('wrong password')
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
