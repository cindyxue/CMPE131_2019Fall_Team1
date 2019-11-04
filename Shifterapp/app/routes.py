from app import Shifter 
from app import db
from app.forms import LoginForm, EmployeeForm, LogoutForm, EditViewForm, RegisterForm
from app.models import Organization, Employee
from flask import render_template, flash, redirect, url_for
from flask import request
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse

@Shifter.route('/', methods = ['GET', 'POST'])
def login():
    formLogin = LoginForm()
    if formLogin.Register.data and formLogin.is_submitted():
        return redirect(url_for('register'))
    elif formLogin.ResetPassword.data and formLogin.is_submitted():
        return redirect(url_for('reset'))

    elif formLogin.is_submitted():
        user = Employee.query.filter_by(email=formLogin.Username.data).first()
        print(user)
        if user is None or not user.check_password(formLogin.Password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        elif user.Manager == True:
            return redirect(url_for('chooseToDo'))
        #login_user(user, remember=formLogin.RememberMe.data)
        # return to page before user got asked to login
        #next_page = request.args.get('next')
        #if not next_page or url_parse(next_page).netloc != '':
        #    next_page = url_for('choose')

        #return redirect(next_page)
    title = "Shifter Scheduling Application"
    return render_template('login.html', title=title, formLogin=formLogin)
@Shifter.route('/resetpassword', methods = ['POST', 'GET'])
def reset():
    return redirect(url_for('login'))

@Shifter.route("/addemployee")
def addemployee():
    title = "Add employee to Shifter"
    formEmployee = EmployeeForm()
    formLogout = LogoutForm()
    return render_template("addemployee.html", title=title, formEmployee=formEmployee, formLogout=formLogout)


@Shifter.route("/choose", methods = ['POST', 'GET'])
def chooseToDo():
    title = "ChooseToDo"
    formLogout = LogoutForm()
    if formLogout.is_submitted():
        flash('Logged out')
        return redirect(url_for('login'))
    formEditView = EditViewForm()

    return render_template("choose.html", title = title, formLogout = formLogout, formEditView = formEditView)
@Shifter.route("/register", methods = ['GET', 'POST'])
def register():
    title = "Register Organization"
    formRegister = RegisterForm()
    if formRegister.validate_on_submit():
        organization = Organization(Name=formRegister.name_company.data, 
                                    email=formRegister.email.data,
                                    typeofbusiness=formRegister.type_company.data,
                                    Address=formRegister.address.data,
                                    PhoneNumber=formRegister.Business_phone_number.data
                                    )
        db.session.add(organization)
        db.session.commit()
        
        employee = Employee(fname = formRegister.manager_namef.data,
                            lname = formRegister.manager_namel.data,
                            email = formRegister.email.data,
                            phone_number=formRegister.Manager_phone_number.data
                            )
        employee.set_manager(True)
        employee.set_password(formRegister.enter_password.data)
        employee.set_orgid(Organization.query.filter_by(email = formRegister.email.data).first().id)

        db.session.add(employee)
        db.session.commit()
        flash('New Organization has been added')
        return redirect(url_for('login'))
        
    return render_template("register.html", title=title, formRegister=formRegister)

if __name__ == '__main__':
    Shifter.run()
