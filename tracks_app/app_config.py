import os
import sqlite3
from flask import Flask


app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect('tracks.db')
    connection.row_factory = sqlite3.Row
    return connection

@app.route('/')
def first():
    pass
