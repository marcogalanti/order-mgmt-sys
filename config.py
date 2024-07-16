from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Inizializza l'app Flask
app = Flask(__name__)

# Configurazione del database
db_user = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{db_user}:{db_password}@cloud-services.demos.mulesoft.com:32692/sedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inizializza SQLAlchemy
db = SQLAlchemy(app)

# Inizializza Marshmallow
ma = Marshmallow(app)
