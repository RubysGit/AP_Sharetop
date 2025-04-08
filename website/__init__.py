from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:i43oz_bhkijn2@localhost/webpage'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

import routes
