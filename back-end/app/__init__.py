from flask import Flask
from config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# App initialization with configurations
app = Flask(__name__)
app.config.from_object(Config)

# initialization
db = SQLAlchemy(app)
migrate = Migrate(app, db)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


from app import routes, models