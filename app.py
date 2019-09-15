from flask import *
from flask_bootstrap import Bootstrap  # Bootstrap
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)  # creating Flask Class obj
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/parenteye'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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


@app.route('/')
def home():
    employees = Employee().query.all()
    return render_template('home.html', employees=employees)


@app.route('/add', methods=["GET", "POST"])
def add():
    employee = Employee()
    if request.form:
        name = request.form.get('name')
        designation = request.form.get('designation')
        address = request.form.get('address')
        phone = request.form.get('phone')
        employee.add(name, designation, address, phone)
        db.session.add(employee)
        db.session.commit()
    return redirect(url_for('home'))


@app.route('/delete', methods=["POST", "DELETE"])
def delete():
    if request.form:
        emp_id = request.form.get('id')
        emp_name = request.form.get('name')
        employee = Employee().query.filter(Employee.id == emp_id, Employee.name == emp_name).first()
        db.session.delete(employee)
        db.session.commit()

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host="192.168.43.48", port=3000)

