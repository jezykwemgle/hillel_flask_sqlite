import sqlite3

connection = sqlite3.connect('tracks.db')

with open('schema.sql') as file:
    connection.executescript(file.read())

cursor = connection.cursor()

with open('tracks.sql') as info:
    cursor.executescript(info.read())

connection.commit()
connection.close()
