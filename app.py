from flask import Flask, render_template, request, flash
from forms import LoginForm
app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/', methods=['GET'])
def index():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/signin', methods=['POST'])
def signin():
    # form = request.LoginForm()

    # import ipdb
    # ipdb.set_trace()

    email = request.form["email"]

    return render_template('user.html', email=email)

if __name__ == '__main__':
    app.run()
