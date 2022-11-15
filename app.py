import os

# import mongoengine

import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from flask import Flask
# from flask_mongoengine import MongoEngine #ModuleNotFoundError: No module named 'flask_mongoengine' = (venv) C:\flaskmyproject>pip install flask-mongoengine 

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "umer"
# app.config['MONGODB_SETTINGS'] = {
#     'db': 'crud',
#     'host': 'localhost',
#     'port': 27017
# }
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = {'jpg', 'jpeg','png','JPG','JPEG','PNG','svg','pdf'}
# db = MongoEngine()
# db.init_app(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('index.html')


# class User(db.Document):
#     profile_pic = db.StringField()


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # usersave = User( profile_pic=file.filename)
        # usersave.save()
        print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        o=url_for('static', filename='uploads/' + filename)
        l = 'https://myupla.herokuapp.com/'+url_for('static', filename='uploads/' + filename)
        print('url is',l)

        return redirect(url_for('static', filename='uploads/' + filename), code=301)
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)




if __name__ == "__main__":
    app.run(port=5000, debug=True,use_reloader=False)