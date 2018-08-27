#from app import db
from forms import RegistrationForm
from flask import Flask, render_template

# ...
app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/index')
def index():
    # ...
    return render_template("index.html", title='Home Page', posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    # if current_user.is_authenticated:
    #     return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run()
