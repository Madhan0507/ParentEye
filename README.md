# parentEye

parentEye - Employee Manage
Installing Modules

#Install flask Module

pip install flask
#install Flask Bootstrap 2. pip install flask-bootstrap

#Install flask_sqlalchemy 3. pip install flask_sqlalchemy

create app.py file


BOOTSTRAP

from flask import * from flask_bootstrap import Bootstrap from flask_sqlalchemy import SQLAlchemy

Create flask object app = Flask(name)

Routing @app.route('/') return "Hello world";

@app.route('home') return render_template('home.html', emp = emplyee) #Create Folder in root directory named 'templates' save home.html and index.html in template folder

bootstrap = Bootstrap(app) #Bootstrap object

{% code %} - for use build in functions loop or statements {{ code }} - print values

While use bootstrap it will refered all bootstrap csss and js index.html. 

for example when use " {% extends "bootstrap/base.hmtl" %} " it invoke bootstrap.css,bootrstrap.js and jquery also.

add custom css 
{% block styles %}
{{ super() }} # used for keep previos defined css

<link rel="stylesheet" href="{{url_for('.static', filename='css/style.css')}}">

{% endblock %}

add body :

{% block body %}

{% endblock %}

add custom scripts 

{% block scripts %}
{{ super() }} # used for keep previos defined js

<script type="text/javascript" src="{{url_for('.static', filename='js/app.js')}}"></script>
{% endblock %}

MYSQL DATABASE 
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


SQLALCHEMY:

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/parenteye' #Database URI

db = SQLAlchemy(app) #SQL Object

create Employee Model

class Employee(db.Model):
    __tablename__ = "employees"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(80))
    designation = db.Column('designation', db.String(20))
    address = db.Column('address', db.String(100))
    phone = db.Column('phone', db.String(10))

    def add(self, name, designation, address, phone):
	    self.name = name
	    self.designation = designation
	    self.address = address
	    self.phone = phone


Create Employee object employee = Employee().

Retrive data from Table : Employee().query.all().

Insert Data:
	employee.add(name, designation, address, phone)
    db.session.add(employee)
    db.session.commit()

Delete Data:
	employee = Employee().query.filter(Employee.id == emp_id, Employee.name == emp_name).first()
    db.session.delete(employee)
    db.session.commit()
    

Run : py app.py (python 3.6)
