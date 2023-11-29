'''
OVERAL PROGRAM INTENTION
This program was designed for CISC/CMPE 327 Assignment 5, November 2023
by Anthony Jones, Akash Singh, and Zarrin Tasnim. 

The program outlines an e-learning wesbite we called SIMLearn, with various functionalities from basic login
to searching courses and viewing lessons. This is version of the website now includes some backend functionality 
by integrating SQLite. 

INPUT AND OUTPUT INFO
To test this code, most of the input values from Assignment 1 may be used, and similar corresponding output values
from Assignment 1 will be printed as expected. However, some adjustments have been made to the original test cases
to better test our current code model. This includes removal of some test cases, addition of new test cases,
and alterations to some of the original test cases inputs and outputs.

To see documentation the test cases that were covered, please see the TestCaseResults.pdf from Assignment 3.
To see the results of test coverage, please run the testing scripts

HOW THE PROGRAM IS MEANT TO BE RUN
The program is intended to be run with a collection of the following key files:
main.py
Course.py
Lessons.py
Payments.py
Quiz.py
Users.py
courseFunctionality.py
getHintMutants.py
test_whitebox.py

Most of the methods are contained in the class files, but a few additional functions are in courseFunctionality.py. 

Please then execute the script using "python main.py" and follow the command-prompts in the terminal. You will notice
that several .db files are generated that contain relevant data. If using VSCode, please download the extension 
"SQLite Viewer by Florian Klampfer" to view the values in the databases. You may need to click "Open Anyway" and select
"SQLite Viewer". 

To execute the tests, please run 'pytest test_whitebox.py' 

Hint: use "bobsmith2001" and "password123" to login :)
'''


#Import statements
from databaseAPI.Users import Users
import courseFunctionality
from databaseAPI.Course import Course
from databaseAPI.Payments import Payments

print('Welcome to SIMLearn\nPlease type "login" for Login or "register" for Register')
choice = input("login/register: ").lower()
#Give user choice to login/register
while (1):
    user = Users()
    course = Course()
    payment = Payments()
    if (choice=='login'):
        while True:
            print('Enter login credentials\n')
            usernameGiven = input("username: ")
            passwordGiven = input('password: ')
            loginOutput = user.login(usernameGiven, passwordGiven)
            if (loginOutput == 'Login Successful'):
                userId= user.username
                print(loginOutput)
                break
            else:
                print(loginOutput)
                continue
        break
    if (choice=='register'):
        while True:
            print('Please enter your credentials\n')
            usernameGiven = input("username: ")
            emailGiven = input("email: ")
            passwordGiven = input('password: ')
            registrationOutput = user.register(usernameGiven, emailGiven, passwordGiven)
            if(registrationOutput == 'Registration Successful'):
                userId = user.username
                print(registrationOutput)
                print("What is your cardnumber and billing address?")
                while True:
                    cardNumberGiven = input("Enter card number (with spaces): [xxxx xxxx xxxxx]")
                    
                    billingAddressGiven = input("Billing Address: ")

                    paymentOutput = payment.takePayment(usernameGiven, cardNumberGiven, billingAddressGiven)
                    print(paymentOutput)
                    if (paymentOutput == 'Payment method entered successfully'):
                        break
                    
                choice='login'
                break
            else:
                print(registrationOutput)
                continue
    else:
        choice = input("Please choose to login or register: ")
print('Welcome')

print('If you would like to see course reccommendations, please enter a keyword of interest. If you do not need to see reccommendations, type "skip"\
      \nFor settings type "settings"')
seeRecs = input()
if (seeRecs!='skip' and seeRecs!='settings'):
    courseFunctionality.courseRecommendations(course, seeRecs)
#Settings option
if(seeRecs=="settings" and seeRecs!='skip'):
    print("Language Settings \n Type 'E' for English or 'O' for Other languages")
    while True:
        lang = input()
        setting = courseFunctionality.settings(lang)
        print(setting)
        if setting!="Language chosen successfully":
            continue
        else:
            break
        

searchInput = input("Please search for a course: ")
print('Results:\n')
searchResult = Course.courseSearch(course, searchInput)
if searchResult == (str(searchInput + ' found!')) : 
    print(searchResult)
else: print(searchResult)
while True:
    print('Please type out the full course name of your choice among these options:\n')
    print(Course.getAllCourses(course))
    selectInput = input()

    print(Course.courseSearch(course, selectInput))
    if (Course.courseSearch(course, selectInput) != 'No such course found'):
        courseFunctionality.openCoursePage(selectInput)




