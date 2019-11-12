from app import Shifter 
from app import db
from app.forms import LoginForm, EmployeeForm, LogoutForm, EditViewForm, RegisterForm, ResetPasswordForm, ContactForm
from app.models import Organization, Employee, Question
from flask import render_template, flash, redirect, url_for
from flask import request
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse
from flask_mail import Message, Mail

mail = Mail()

@Shifter.route('/', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated and current_user.manager==True:
        return redirect(url_for('chooseToDo'))
    formLogin = LoginForm()
    if formLogin.Register.data and formLogin.is_submitted():
        return redirect(url_for('register'))
    elif formLogin.ResetPassword.data and formLogin.is_submitted():
        return redirect(url_for('reset'))

    elif formLogin.validate_on_submit():
        user = Employee.query.filter_by(email=formLogin.Username.data).first()
        if user is None or not user.check_password(formLogin.Password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        elif user.manager == True:
            login_user(user, remember=formLogin.RememberMe.data)
        # return to page before user got asked to login
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('chooseToDo')
            return redirect(next_page)
    title = "Shifter Scheduling Application"
    return render_template('login.html', title=title, formLogin=formLogin)
#@Shifter.route('/resetpassword', methods = ['POST', 'GET'])
#def reset():
 #   return redirect(url_for('login'))
@Shifter.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@Shifter.route("/addemployee")
@login_required
def addemployee():
    title = "Add employee to Shifter"
    formEmployee = EmployeeForm()
    formLogout = LogoutForm()
    return render_template("addemployee.html", title=title, formEmployee=formEmployee, formLogout=formLogout)


@Shifter.route("/contact", methods=['GET','POST'])
def contact():
    title = "Contact Us"
    formContact = ContactForm()

    if request.method == 'POST':
        if formContact.validate() == False:
            flash('All fields are required.')
            return render_template('Contact.html', formContact=formContact, title=title)
        else:
            msg = Message(formContact.subject.data, sender='contact@example.com', recipients=['CMPE131Shifter@gmail.com'])
            msg.body = f"""
                  From:              {formContact.name.data} 
                  Email:             {formContact.email.data} 
                  Phone Number:      {formContact.phone_number.data} 
                  Subject:           {formContact.subject.data} 
                  Message:           {formContact.message.data}
                  """
            mail.send(msg)

            return render_template('Contact.html',title=title, success = True)

    elif request.method == 'GET':
        return render_template("Contact.html", title=title, formContact=formContact)
Shifter.config["MAIL_SERVER"] = "smtp.gmail.com"
Shifter.config["MAIL_PORT"] = 465
Shifter.config["MAIL_USE_SSL"] = True
Shifter.config["MAIL_USERNAME"] = 'CMPE131Shifter@gmail.com'
Shifter.config["MAIL_PASSWORD"] = 'Password131'

mail.init_app(Shifter)

@Shifter.route("/about")
def about():
    title = "About Shifter"
    return render_template("About.html", title=title)


@Shifter.route("/choose", methods=['POST', 'GET'])
def chooseToDo():
    title = "ChooseToDo"
    formLogout = LogoutForm()
    formEditView = EditViewForm()

    if formLogout.Logout.data and formLogout.is_submitted():
        flash('Logged out')
        return redirect(url_for('logout'))
    elif formEditView.AddEmpl.data and formEditView.is_submitted():
        return redirect(url_for('addemployee'))

    return render_template("choose.html", title = title, formLogout = formLogout, formEditView = formEditView)
@Shifter.route("/register", methods = ['GET', 'POST'])
def register():
    title = "Register Organization"
    formRegister = RegisterForm()
    if formRegister.validate_on_submit():
        organization = Organization(name=formRegister.name_company.data, 
                                    email=formRegister.email.data,
                                    typeofbusiness=formRegister.type_company.data,
                                    address=formRegister.address.data,
                                    phone_number=formRegister.business_phone_number.data
                                    )
        db.session.add(organization)
        db.session.commit()
        
        employee = Employee(fname = formRegister.manager_namef.data,
                            lname = formRegister.manager_namel.data,
                            email = formRegister.email.data,
                            phone_number=formRegister.manager_phone_number.data,
                            manager = True,
                            organization_id = organization.id
                            )
        employee.set_password(formRegister.enter_password.data)
        db.session.add(employee)
        db.session.commit()
        flash('New Organization has been added')
        return redirect(url_for('login'))
    return render_template("register.html", title=title, formRegister=formRegister)

@Shifter.route('/resetpassword', methods = ['GET', 'POST'])
def reset():
    resetform = ResetPasswordForm()
    title = 'Reset Your Password'
    render_template('reset.html', title = title, resetform = resetform)
if __name__ == '__main__':
    Shifter.run()
