from app import Shifter 
from app import db
from app.forms import LoginForm, EmployeeForm, LogoutForm, EditViewForm, RegisterForm, ResetPasswordForm, ContactForm, ChangeWeekForm, managerhomepageForm
from app.models import Organization, Employee, Schedule
from flask import render_template, flash, redirect, url_for
from flask import request
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse
from flask_mail import Message, Mail
from datetime import *
from datetime import date, time
import calendar
import datetime
from calendar import monthrange

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
        elif user.manager == False and user.firsttimelogin == False:
            login_user(user, remember=formLogin.RememberMe.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('emphomepage')
            return redirect(next_page)
        
    title = "Shifter Scheduling Application"
    return render_template('login.html', title=title, formLogin=formLogin)

@Shifter.route("/emphomepage", methods = ['POST', 'GET'])
@login_required
def emphomepage():
    formLogout = LogoutForm()
    formchangeweek = ChangeWeekForm()
    title = current_user.fname + ' ' + current_user.lname + ' Homepage'
    if formLogout.Logout.data and formLogout.is_submitted():
        return redirect(url_for('logout'))

        
    startdate = date.today().replace(day=1)
    monthlength = monthrange(startdate.year, startdate.month)
    enddate = startdate + timedelta(days= monthlength[1]-1) 

    if formchangeweek.nextMonth.data and formchangeweek.is_submitted:
        startdate+=timedelta(days= monthlength[1]) 
        monthlength = monthrange(startdate.year, startdate.month)
        enddate = startdate + timedelta(days= monthlength[1]-1) 
    if formchangeweek.previous.data and formchangeweek.is_submitted:
        startdate-=timedelta(days= monthlength[1]-1) 
        monthlength = monthrange(startdate.year, startdate.month)
        enddate = startdate + timedelta(days= monthlength[1]-1) 
        
    array = getWeeklySchedule(startdate,enddate)
    dates = monthlength[1]+1
    schedulestarts = {}
    schedulesends = {}
    for i in range(1, monthlength[1]+1):
        schedulestarts[i]=[]
        schedulesends[i]=[]
    for j in range(1,monthlength[1]+1):
        for i in range(0, len(array)):
            if j==array[i].thedates.day:
                schedulestarts[j].append((array[i].starttime).strftime( '%H:%M '))
                schedulesends[j].append((array[i].endtime).strftime('%H:%M'))

    
    return render_template('emphomepage.html', title = title, formLogout=formLogout, formchangeweek = formchangeweek, startdate = startdate, enddate = enddate, dates = dates, 
    starttimes = schedulestarts, endtimes = schedulesends, len = dates)

def getWeeklySchedule(startdate, enddate):
    s = Schedule.query.filter_by(emp_id = current_user.id).filter(Schedule.thedates>=startdate).filter(Schedule.thedates<=enddate).order_by(Schedule.thedates).all()
    return s
        
@Shifter.route('/logout')
def logout():
    logout_user()
    flash('Logged out')
    return redirect(url_for('login'))


@Shifter.route("/addemployee", methods = ['GET', 'POST'])
@login_required
def addemployee():
    title = "Add employee to Shifter"
    formEmployee = EmployeeForm()
    formLogout = LogoutForm()
    if formLogout.Logout.data and formLogout.is_submitted():
        return redirect(url_for('logout'))

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

    return render_template("addemployee.html", title=title, formEmployee=formEmployee, formLogout=formLogout)

@Shifter.route("/account")
def displayMyAccount():
    title = "My Account"
    formRegister = RegisterForm()
    formLogout = LogoutForm()
    return render_template("account.html", title=title, formRegister=formRegister, formLogout=formLogout)

@Shifter.route("/contact", methods=['GET','POST'])
def contact():
    if (current_user.is_authenticated):
        title = "Contact Us By User"
    else:
        title = "Contact Us"
    formLogout = LogoutForm()

    formContact = ContactForm()
    if formLogout.Logout.data and formLogout.is_submitted():
        return redirect(url_for('logout'))
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
        return render_template("Contact.html", title=title, formContact=formContact, formLogout=formLogout)
Shifter.config["MAIL_SERVER"] = "smtp.gmail.com"
Shifter.config["MAIL_PORT"] = 465
Shifter.config["MAIL_USE_SSL"] = True
Shifter.config["MAIL_USERNAME"] = 'CMPE131Shifter@gmail.com'
Shifter.config["MAIL_PASSWORD"] = 'Password131'

mail.init_app(Shifter)

@Shifter.route("/about", methods = ['POST', 'GET'])
def about():
    if (current_user.is_authenticated):
        title = "About Shifter By User"
    else:
        title = "About Shifter"
    formLogout = LogoutForm()
    if formLogout.Logout.data and formLogout.is_submitted():
        return redirect(url_for('logout'))
    return render_template("About.html", title=title, formLogout = formLogout)


@Shifter.route("/choose", methods=['POST', 'GET'])
@login_required
def chooseToDo():
    title = "ChooseToDo"
    formLogout = LogoutForm()
    formEditView = EditViewForm()
    if current_user.manager==False:
        return redirect(url_for('emphomepage'))
    if formLogout.Logout.data and formLogout.is_submitted():
        return redirect(url_for('logout'))
    elif formEditView.AddEmpl.data and formEditView.is_submitted():
        return redirect(url_for('addemployee'))
    elif formEditView.View.data and formEditView.is_submitted:
        return redirect(url_for('managerview'))
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
    if current_user.is_authenticated:
        title = 'First Login password change'
        email = current_user.email
    else:
        email = ''
        title = 'Reset Your Password'
    resetform = ResetPasswordForm()
    formLogout = LogoutForm()
    if formLogout.Logout.data and formLogout.is_submitted():
        return redirect(url_for('logout'))
        
    if resetform.submit.data and resetform.is_submitted:
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
                    flash('New password has been set successfully!')
                    return redirect(url_for('login'))



            return redirect(url_for('login'))
    #resetform.question1.choices = [(Employee.id) for question1 in question1.query.filter_by(question1='Whichcity').all()]
    return render_template('reset.html', title = title, resetform = resetform, formLogout = formLogout, email = email)

@Shifter.route("/managerview", methods = ['GET', 'POST'])
@login_required
def managerview():
    title = "Employee Schedules"
    formLogout = LogoutForm()
    
    if current_user.manager==False:
        return redirect(url_for('emphomepage'))
    elif formLogout.Logout.data and formLogout.is_submitted():
        return redirect(url_for('logout'))
    
    scheduleform = managerhomepageForm()
    todaysdate = date.today()
    
    schedules = Schedule.query.filter_by(org_id=current_user.organization_id).all()
    employees = Employee.query.filter_by(organization_id=current_user.organization_id).all()
    employee_list = []
    for i in employees:
        employee_list.append((i.fname, i.fname +' '+ i.lname))
    print(employee_list)
    scheduleform.employees.choices = employee_list
    schedule_starts = [] # List of Strings with format 'HH:MM'
    schedule_ends = []
    schedule_days = [] # List of Strings with format 'YY-MM-DD'
    employee_names = []
    #ts = time(12,30)
    #te = time(16,30)
    #d = date(2019,12,2)
    #S = Schedule(id = 200,thedates = d, starttime = ts, endtime = te, emp_id = 2, org_id = 1 )
    #db.session.add(S)
    #db.session.commit()
    for i in range(0, len(schedules)):
        schedule_starts.append(schedules[i].starttime.strftime('%H:%M'))
        schedule_ends.append(schedules[i].endtime.strftime('%H:%M'))
        schedule_days.append(str(schedules[i].thedates))
        employee_id = (schedules[i].emp_id)
        employee_names.append(Employee.query.get(employee_id).fname)
    print(schedule_days)
    print(schedule_ends)
    print(schedule_starts)
    print(employee_names)
    return render_template("managerviewsch.html",
                           title=title,
                           formLogout=formLogout,
                           schedule_starts=schedule_starts,
                           schedule_ends=schedule_ends,
                           schedule_days=schedule_days,
                           employee_names=employee_names,
                           scheduleform = scheduleform,
                           todaysdate = todaysdate)
    
    

    
if __name__ == '__main__':
    Shifter.run()
