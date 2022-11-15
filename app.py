from flask import Flask
from flask_mongoengine import MongoEngine #ModuleNotFoundError: No module named 'flask_mongoengine' = (venv) C:\flaskmyproject>pip install flask-mongoengine 

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "umer"
app.config['MONGODB_SETTINGS'] = {
    'db': 'crud',
    'host': 'localhost',
    'port': 27017
}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024