from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Taofeek'}
    posts = [
        {
            'author': {'username': 'Tobi'},
            'body': 'You guys eat too much eba'
        },
        {
            'author': {'username': 'Bolu'},
            'body': 'kuku whatever'
        }
    ]
    return render_template('index.html',title='Home', user=user, posts=posts)