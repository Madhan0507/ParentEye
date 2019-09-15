# parentEye - Employee Manage

Installing Modules 

#Install flask Module
1. pip install flask

#install Flask Bootstrap
2. pip install flask-bootstrap

#Install flask_sqlalchemy
3. pip install flask_sqlalchemy
 
 create app.py file
 
import modules
 
from flask import *
from flask_bootstrap import Bootstrap 
from flask_sqlalchemy import SQLAlchemy
 
Create flask object
app = Flask(__name__)
 
Routing
@app.route('/')
  return "Hello world";

@app.route('home')
  return render_template('home.html', emp = emplyee) #Create Folder in root directory named 'templates' save home.html and index.html in template folder


bootstrap = Bootstrap(app) #Bootstrap object

{% code %} - for use build in functions loop or statements
{{ code }} - print values 

While use bootstrap it will refered all bootstrap csss and js index.html.
for example when use " {% extends "bootstrap/base.hmtl" %} " it invoke bootstrap.css,,,bootrstrap.js and jquery also,


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/parenteye' #Database URI

db = SQLAlchemy(app) #SQL Object


