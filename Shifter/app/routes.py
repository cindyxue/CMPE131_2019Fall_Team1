from app import Shifter 
from app.forms import LoginForm, EmployeeForm, LogoutForm
from flask import render_template,flash, redirect, url_for

Shifter.config['SECRET_KEY'] = 'some-key'


@Shifter.route("/")
def home():
    title = "Shifter Scheduling Application"
    formLogin = LoginForm()
    formLogout = LogoutForm()
    return render_template('index.html', title=title, formLogin=formLogin, formLogout=formLogout)


@Shifter.route("/addemployee")
def addemployee():
    title = "Add employee to Shifter"
    form = EmployeeForm()
    return render_template("addemployee.html", title=title, form=form)
@Shifter.route("/choose")

def choose():
    title = "Edit "

if __name__ == '__main__':
    Shifter.run()