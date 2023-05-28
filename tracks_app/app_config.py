import sqlite3
from flask import Flask, render_template, url_for

app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect('tracks.db')
    connection.row_factory = sqlite3.Row
    return connection

@app.route('/')
def main():
        return f"""
            <a href="{url_for('names')}">Count of unique artists</a><br>
            <a href="{url_for('tracks')}">All tracks</a><br>
            <a href="{url_for('tracks_by_genre', genre='Rock')}">Tracks by genre</a><br>
            <a href="{url_for('tracks_sec')}">Tracks` duration</a><br>
            <a href="{url_for('tracks_statistics')}">Tracks` avg and total duration</a><br>
            """

@app.route('/names/')
def names():
    connection = get_db_connection()
    count = connection.execute('SELECT COUNT(DISTINCT artist) FROM tracks').fetchone()[0]
    return render_template('names.html', count=count)

@app.route('/tracks/')
def tracks():
    connection = get_db_connection()
    count = connection.execute('SELECT COUNT(*) FROM tracks').fetchone()[0]
    return render_template('tracks.html', count=count)

@app.route('/tracks/<genre>')
def tracks_by_genre(genre):
    connection = get_db_connection()
    count = connection.execute(f'SELECT COUNT(genre) FROM tracks WHERE genre="{genre}"').fetchone()[0]
    tracks_g = connection.execute(f'SELECT * FROM tracks WHERE genre="{genre}"').fetchall()
    return render_template('by_genre.html', tracks=tracks_g, genre=genre, count=count)

@app.route('/tracks-sec/')
def tracks_sec():
    connection = get_db_connection()
    tracks_s = connection.execute('SELECT * FROM tracks')
    return render_template('title_len.html', tracks=tracks_s)

@app.route('/tracks-sec/statistics/')
def tracks_statistics():
    connection = get_db_connection()
    tracks_st = connection.execute('SELECT AVG(length), SUM(length) FROM tracks').fetchone()
    return render_template('statistics.html', avg=tracks_st[0], sum=tracks_st[1])

if __name__ == '__main__':
    app.run(debug=True)
