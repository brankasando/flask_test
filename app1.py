# pip3 install flask-sqlachemy in terminal

from flask import Flask, render_template, request, redirect #iz flask biblioteke importujemo flask objekat
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3

app = Flask(__name__) #zovemo flask konsturktor, ovo __name__ referencuje ovaj fajl

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///post.db'
db = SQLAlchemy(app)

@app.route('/')
def print_hello():
    return 'Hello'

@app.route('/show_db', methods=['GET','POST'])
def get_dropdown_():
    con = sqlite3.connect('/home/branka/test1/bets.db')
    cur = con.cursor()
    cur.execute(
        '''
        select distinct col1 from test_table
        ''')
    drop_down_list = cur.fetchall()
    return render_template('show_db.html', ddl=drop_down_list)


if __name__ == "__main__":
    app.run(debug=True) #ako zovemo program iz komande linije da ukljuci debug mode