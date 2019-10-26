from app import Shifter 
from app import db
from app.forms import LoginForm, EmployeeForm, LogoutForm, EditViewForm, RegisterForm
from app.models import Organization, Employee
from flask import render_template, flash, redirect, url_for
from flask import request
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse


Shifter.config['SECRET_KEY'] = 'some-key'

@Shifter.route('/')
@Shifter.route("/login", methods = ["GET", "POST"])
def login():
    formLogin = LoginForm()
    if formLogin.validate_on_submit():
        user = Employee.query.filter_by(Email=formLogin.Username.data).first()
        if user is None or not user.check_password(formLogin.Password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=formLogin.RememberMe.data)
        # return to page before user got asked to login
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('choose')

        return redirect(next_page)
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
@Shifter.route("/register")
def register():
    title = "Register Organization"
    formRegister = RegisterForm()
    formLogout = LogoutForm()
    return render_template("register.html", title=title, formRegister=formRegister, formLogout=formLogout)

if __name__ == '__main__':
    Shifter.run()