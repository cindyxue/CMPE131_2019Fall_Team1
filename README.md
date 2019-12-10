[![Build Status](https://travis-ci.com/cindyxue/CMPE131_2019Fall_Team1.svg?branch=master)](https://travis-ci.com/cindyxue/CMPE131_2019Fall_Team1)

# CMPE131_2019Fall_Team1

# Submission Instructions
1.	Overall project deadline: Wed 12/4 11:59 PM
# a.	Submit in the textbox the hash commit of your app submission.
# b.	In the git project we expect to see a readme with a link to your live website on Heroku.
                                        > https://shift-er.herokuapp.com/ 
# c.	README should include icon to show whether tests are passing/failing.
# d.	README should state file location of test cases and how to run them.
					> CMPE131FALL_Team1>Shifterapp>tests
                                        > To run the test cases:
                                        > 1) Open command prompt
                                        > 2) Enter "pip install pytest" into command prompt
                                        > 3) Navigate to the the base directory of our app (CMPE131_2019Fall_Team1)
                                        > 4) Enter "pytest" into command prompt
# e.	README should show location of HTML file to view the sphinx documentation.
                                         >CMPE131FALL_Team1>Shifterapp>_build

# Shifter 
The project which our team is going to build is an Employee Scheduling app. The target audience for the app would be both employers and employees. It is going to be the handler of the schedule of multiple employees and the issues/changes surrounding the scheduling job such as availability, communications etc.
# Instructions on how to run the app
Clone the link into your Command Prompt 
On master branch, type "flask run"
....
#  Describes all 8 features and how to verify that they were implemented
## Feature 1: Login Page

The user enters email and password. The database will verify and login the user in if only it's a valid user.

## Feature 2: Register Org Page

Once you click on the button, it will take you to a register page. The register page registers an organization. It prompts the user to input company info and new manager's info. To verify it, open the database and see if the data is added to the database. 

## Feature 3: Logout Page

The user has to be logged in to be logged out. The page should be redirected to login page if a user is logged out successfully.

## Feature 4: Database (Login info)

There are two tables. One is for employee and the other is for organization. To verify, drop the file to the link and it will display the structure of the database.

Link: https://inloop.github.io/sqlite-viewer/

## Feature 5: Contact Page 

If the user needs customer support, they can write down the issue and it will send customer support an email. To verify it works, you could login to the email and check.

Email: CMPE131Shifter@gmail.com

Password: Password131

## Feature 6: My Account Page

My accound page displays basic info of a user. User can edit it's info. 

## Feature 7: Calender
The Calender now shows the schedule of the person logged in. Essentially being the employee homepage. 

## Feature 8: EditSchedule
The Manager can schedule the employees through this page. There is also a table showing the schedule on the right side. 

## Feature 9: Register Employee Page
This allows the manager to add an Employee under his own organization and select their role. 

...
