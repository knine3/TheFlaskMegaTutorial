from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Knine3'}
    return render_template('index.html', title='Home', user=user)


@app.route('/posts')
def posts():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful Evening in Karachi'
        },
        {
            'author': {'username': 'Fazeel'},
            'body': 'Clash Royale is so cool, yo!'
        }
    ]
    return render_template('posts.html', title='Posts', posts=posts)
