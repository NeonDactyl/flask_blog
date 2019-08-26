from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Trey Westrich',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'posted_at': '2019-08-24'
    },
    {
        'author': 'Trey Westrich',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'posted_at': '2019-08-25'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')
