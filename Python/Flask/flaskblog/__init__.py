import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "main_routes.login"
login_manager.login_message_category = "info"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "kumaradoss.py@gmail.com"
print(app.config['MAIL_USERNAME'])
app.config['MAIL_PASSWORD'] = "bloj mxxt fdxa plpn"       #os.environ.get('EMAIL_PASS')
mail = Mail(app)

from flaskblog.routes import main_routes  # Adjust import path if needed
app.register_blueprint(main_routes)


