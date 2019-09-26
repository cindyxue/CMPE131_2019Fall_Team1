from app import Shifter 
from app.forms import LoginForm
from flask import render_template ,flash, redirect, url_for
Shifter.config['SECRET_KEY'] = 'some-key'
@Shifter.route("/")

def home():
    title = "Shifter Scheduling Application"
    formLogin = LoginForm()
    return render_template('index.html', title = title, formLogin = formLogin)

if __name__ == '__main__':
    Shifter.run()
    