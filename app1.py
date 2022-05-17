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
    if request.method == 'GET':
        con = sqlite3.connect('/home/branka/test1/bets.db')
        cur = con.cursor()
        cur.execute(
            '''
            select 'All' as col1
            union
            select distinct col1 from test_table 
            ''')
        drop_down_list_fetched = cur.fetchall()

        col1_value = request.args.get('col1')

        if col1_value is None:
            col1_value = 'All'

        cur.execute(
            '''
            select * from test_table where col1 = (?) or 'All' = (?)
            ''',
            (col1_value, col1_value) )

        rows_fetched= cur.fetchall()
        return render_template('show_db.html', ddl=drop_down_list_fetched, rows=rows_fetched, c=col1_value)
    else:
        con = sqlite3.connect('/home/branka/test1/bets.db')
        cur = con.cursor()
        cur.execute(
            '''
            select distinct col1 from test_table 
            ''')
        drop_down_list_fetched = cur.fetchall()

        cur.execute(
            '''
            select * from test_table
            ''')
        rows_fetched= cur.fetchall()
    return render_template('show_db.html', ddl=drop_down_list_fetched, rows=rows_fetched)

if __name__ == "__main__":
    app.run(debug=True) #ako zovemo program iz komande linije da ukljuci debug mode