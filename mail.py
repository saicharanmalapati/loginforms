from flask import Flask
from flask_mail import Mail, Message
app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587,
app.config['MAIL_USE_TLS'] = True,
app.config['MAIL_USE_SSL'] = False,
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_SSL'] = True
#app.config['MAIL_USE_TLS'] = 1
app.config['MAIL_USERNAME'] = 'saicharan1309@gmail.com'
app.config['MAIL_PASSWORD'] = 'madhavi1213'

mail = Mail(app)


@app.route('/')
def index():
    msg = Message('Hello', sender='saicharan1309@gmail.com',
                  recipients=['saicharan1213@gmail.com'])
    mail.send(msg)
    return 'Message Sent'

if __name__ == '__main':
    app.run()
