import os
from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
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
    education = db.Column(db.Text, nullable=True)
    courses = db.Column(db.Text, nullable=True)
    projects =db.Column(db.Text, nullable=True)
    job_experience = db.Column(db.Text, nullable=True)
    hard_skills = db.Column(db.Text, nullable=True)
    soft_skills = db.Column(db.Text, nullable=True)


def validate_login(form, fields):
    login = fields.data
    if is_login_in_db(login):
        raise ValidationError('Логин занят')

def is_login_in_db(login):
    return User.query.filter_by(login=login).first() is not None
class RegisterForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    patronymic = StringField('Отчество')
    email = StringField('Email', validators=[DataRequired()])
    contact1_name = StringField('Название контакта 1')
    contact1_value = StringField('Значение контакта 1')
    contact2_name = StringField('Название контакта 2')
    contact2_value = StringField('Значение контакта 3')
    contact3_name = StringField('Название контакта 3')
    contact3_value = StringField('Значение контакта 3')
    about = TextAreaField('Обо мне')
    growth_area = TextAreaField('Области развития')
    tags = TextAreaField('Тэги')
    education = TextAreaField('Образование')
    courses = TextAreaField('Пройденные курсы')
    projects = TextAreaField('Проекты')
    job_experience = TextAreaField('Опыт работы')
    hard_skills = TextAreaField('Hard skills')
    soft_skills = TextAreaField('Soft skills')


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


@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('regist.html', form=form)

@app.route('/register_post', methods=['GET', 'POST'])
def handle_register_post():
    form = RegisterForm()

    if form.validate_on_submit():
        if is_login_in_db(form.login.data):
            return render_template('login_taken.html')

        db_dict = {f.name: f.data for f in form if f.name != 'csrf_token'}
        new_user = User(**db_dict)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('user_page', login=new_user.login))






if __name__ == '__main__':
    app.run()
