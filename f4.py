# pip3 install flask-sqlachemy in terminal

from flask import Flask, render_template #iz flask biblioteke importujemo flask objekat
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bets.db' #govorimo aplikaciji gde je baza smestena
db = SQLAlchemy(app) #incijalizuje bazu sa setingsom aplikacije?


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)