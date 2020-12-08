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
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template('login.html')

    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
