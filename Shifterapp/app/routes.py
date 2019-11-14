from app import Shifter 
from app import db
from app.forms import LoginForm, EmployeeForm, LogoutForm, EditViewForm, RegisterForm, ResetPasswordForm, ContactForm
from app.models import Organization, Employee
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
        elif user.firsttimelogin == True:
            login_user(user, remember=formLogin.RememberMe.data)
            flash('Your password has expired. Setup the security questions and submit your answers')
            return redirect(url_for('reset'))
        elif user.manager == True and user.firsttimelogin == False:
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


@Shifter.route("/addemployee", methods = ['GET', 'POST'])
@login_required
def addemployee():
    title = "Add employee to Shifter"
    formEmployee = EmployeeForm()
    if (formEmployee.validate_on_submit()):
        user = Employee.query.filter_by(email = formEmployee.email.data).first()
        user1 = Employee.query.filter_by(phone_number=formEmployee.phone_number.data).first()
        if user is not None:
            flash('There is already an account registered under this email address.')
            return redirect(url_for('addemployee'))
        elif user1 is not None:
            flash('There is already an account registered under this phone number.')
            return redirect(url_for('addemployee'))
        else:
            employee = Employee(fname = formEmployee.first_name.data,
                            lname = formEmployee.last_name.data,
                            email = formEmployee.email.data,
                            phone_number=formEmployee.phone_number.data,
                            organization_id = current_user.organization_id,
                            firsttimelogin = True)
            employee.setManager(formEmployee.manager.data)
            employee.set_password(formEmployee.phone_number.data)
            db.session.add(employee)
            db.session.commit()


        return redirect(url_for('login'))
    formLogout = LogoutForm()

    return render_template("addemployee.html", title=title, formEmployee=formEmployee, formLogout=formLogout)

@Shifter.route("/account")
def displayMyAccount():
    title = "My Account"
    formRegister = RegisterForm()
    formLogout = LogoutForm()
    return render_template("account.html", title=title, formRegister=formRegister, formLogout=formLogout)

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
@login_required
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
                            organization_id = organization.id,
                            firsttimelogin = False,
                            question1=formRegister.question1.data,
                            answer1=formRegister.answer1.data,
                            question2=formRegister.question2.data,
                            answer2=formRegister.answer2.data,
                            )
        employee.set_password(formRegister.enter_password.data)
        db.session.add(employee)
        db.session.commit()
        flash('New Organization has been added')
        return redirect(url_for('login'))
    return render_template("register.html", title=title, formRegister=formRegister)

@Shifter.route("/resetpassword", methods = ['GET', 'POST'])
def reset():
    title = 'Reset Your Password'
    formLogout = LogoutForm()
    resetform = ResetPasswordForm()
    if resetform.validate_on_submit():
        if (current_user.is_authenticated):
            current_user.setfirstlogin(False)
            current_user.setQuestion(resetform.question1.data, resetform.question2.data)
            current_user.setAnswer(resetform.answer1.data, resetform.answer2.data)
            current_user.set_password(resetform.newPassword.data)
            db.session.commit()
            flash ('New password has been set for this account.')
            return redirect(url_for('login'))
        else:
            user = Employee.query.filter_by(email=resetform.email.data).first()
            if user is None:
                flash ('Invalid Email. Try Again')
                return redirect(url_for('reset'))
            else:
                answer1 = resetform.answer1.data
                answer2 = resetform.answer2.data
                question1 = resetform.question1.data
                question2 = resetform.question2.data
                user1 = Employee.query.filter_by(answer1=answer1, answer2=answer2,  question1=question1,  question2=question2).first()
                if user1 is None:
                    flash ('Invalid answers or wrong choice of questions')
                    return redirect(url_for('reset'))
                else:
                    user1.set_password(resetform.newPassword.data)
                    user1.setfirstlogin(False)
                    db.session.commit()
                    return redirect(url_for('login'))



            return redirect(url_for('login'))
    #resetform.question1.choices = [(Employee.id) for question1 in question1.query.filter_by(question1='Whichcity').all()]
    return render_template('reset.html', title = title, resetform = resetform, formLogout = formLogout)
    
if __name__ == '__main__':
    Shifter.run()
