# import modules
import main, env_variable
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField

app = Flask(__name__)

app.config['SECRET_KEY'] = env_variable.app_security_key

# load model, labels and functions
moderator = main.content_moderator


class TextForm(FlaskForm):
    text = TextAreaField('Text')
    submit = SubmitField('Send')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TextForm()
    session['text'] = form.text.data

    return redirect(url_for("moderator"))

    return render_template('home.html', form=form)


@app.route('/moderator')
def moderator():
    text = session['text']
    result = moderator(text)
    return render_template('moderator.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
