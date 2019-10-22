from app import Shifter 
from app import db
from app.forms import LoginForm, EmployeeForm, LogoutForm, EditViewForm, RegistrationForm
from app.models import Organization, Manager, Employee
from flask import render_template,flash, redirect, url_for
from flask import request
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse

Shifter.config['SECRET_KEY'] = 'some-key'

@Shifter.route('/')
@Shifter.route("/", methods = ["GET", "POST"])
def login():
    formLogin = LoginForm()
    if formLogin.validate_on_submit():
        if formLogin.ManagerEmployee.data=="Manager":
            user = Manager.query.filter_by(username=formLogin.Username.data).first()
            if user is None or not user.check_password(formLogin.Password.data):
                flash('Invalid username or password')
                return redirect(url_for('login'))
            login_user(user, remember = formLogin.remember_me.data)
            
        elif formLogin.ManagerEmployee.data =="Employee":
            user1 = Employee.query.filter_by(username=formLogin.Username.data).first()
            if user1 is None or not user1.check_password(formLogin.Password.data):
                flash('Invalid username or password')
                return redirect(url_for('login'))
            login_user(user1, remember = formLogin.remember_me.data)
            
    title = "Shifter Scheduling Application"
    formLogout = LogoutForm()
    return render_template('login.html', title=title, formLogin=formLogin, formLogout=formLogout)


@Shifter.route("/addemployee")
def addemployee():
    title = "Add employee to Shifter"
    formEmployee = EmployeeForm()
    formLogout = LogoutForm()
    return render_template("addemployee.html", title=title, formEmployee=formEmployee, formLogout=formLogout)


@Shifter.route("/choose")
def chooseToDo():
    title = "ChooseToDo"
    formLogout = LogoutForm()
    formEditView = EditViewForm()
    return render_template("choose.html", title = title, formLogout = formLogout, formEditView = formEditView)


if __name__ == '__main__':
    Shifter.run()