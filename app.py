from flask import Flask, render_template, redirect, request, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATE_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mail.db'
app.config['SECRET_KEY'] = 'random_value'


db = SQLAlchemy(app)
Bootstrap(app)


class Mail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)

    def __init__(self, username, email, phone):
        self.username = username
        self.email = email
        self.phone = phone


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("request is post")
        if not request.form['username'] or not request.form['email'] or not request.form['phone']:
            flash('Please enter all the fields', 'error')
        else:
            mail1 = Mail(request.form['username'], request.form[
                'email'], request.form['phone'])
            db.session.add(mail1)
            db.session.commit()
            flash('Record was successfully added')

    return render_template('index.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
