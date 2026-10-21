from flask import render_template, flash, redirect
from app import app         # Imported app module from app package
from app.forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Bob'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in New York!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Backrooms movie was very cool!'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
