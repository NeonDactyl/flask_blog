from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '2c3a45257b7f8b4ec29e643edaf65451'

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

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
