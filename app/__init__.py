from flask import Flask                     # Imported Flask class from flask package
from config import Config                   # Imported Config class from config module
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models