from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_login import LoginManager

app = Flask(__name__)

load_dotenv()

db_pw = os.environ.get("DB_PW")
db_user = os.environ.get("DB_USERNAME")
db_ip = os.environ.get("DB_IP")
db_name = os.environ.get("DB_NAME")
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_pw}@{db_ip}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['TESTING'] = False

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)

import routes

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

import structures as struct

@login_manager.user_loader
def load_user(entity_id):
    result = struct.User.query.filter_by(entity_id=int(entity_id)).first()
    return result
