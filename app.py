import os
from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "Are you thinking what I'm thinking"
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)


class User(db.Model):
    login = db.Column(db.String(64), primary_key=True)
    surname = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    patronymic = db.Column(db.String(64), nullable=True)
    email = db.Column(db.String(64), nullable=False)
    contact1_name = db.Column(db.String(64), nullable=True)
    contact1_value = db.Column(db.String(64), nullable=True)
    contact2_name = db.Column(db.String(64), nullable=True)
    contact2_value = db.Column(db.String(64), nullable=True)
    contact3_name = db.Column(db.String(64), nullable=True)
    contact3_value = db.Column(db.String(64), nullable=True)
    about = db.Column(db.Text, nullable=True)
    growth_area = db.Column(db.Text, nullable=True)
    tags = db.Column(db.Text, nullable=False)
    # projects_links = db.Column(db.Text)
    education = db.Column(db.Text, nullable=True)
    courses = db.Column(db.Text, nullable=True)
    projects =db.Column(db.Text, nullable=True)
    job_experience = db.Column(db.Text, nullable=True)
    hard_skills = db.Column(db.Text, nullable=True)
    soft_skills = db.Column(db.Text, nullable=True)


@app.route('/')
def index():  # put application's code here
    return render_template('privatecab.html')


@app.route('/user/<login>')
def user_page(login):
    user = User.query.filter_by(login=login).first()
    if user:
        user_dict = user.__dict__
        del user_dict['_sa_instance_state']
        return render_template('privatecab.html', **user_dict)


if __name__ == '__main__':
    app.run()
