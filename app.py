# import modules
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField

import env_variable
import main

app = Flask(__name__)

app.config['SECRET_KEY'] = env_variable.app_security_key


class TextForm(FlaskForm):
    text = TextAreaField('Text')
    submit = SubmitField('Send')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TextForm()
    if form.validate_on_submit():  # Check if form is submitted
        session['text'] = form.text.data
        return redirect(url_for("moderator"))
    return render_template('home.html', form=form)


@app.route('/moderator')
def moderator():
    text = session['text']
    result = main.content_moderator(text)
    return render_template('moderator.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
