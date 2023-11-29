import pytest

import databaseAPI.Users, databaseAPI.Course, databaseAPI.Lessons, databaseAPI.Payments, databaseAPI.Quiz
import courseFunctionality

#To test with PyTest : "pytest test_pytest.py" in terminal
#testCourseSearch and testPayment are not included here, but are in blackboxTest.py

'''
def testRegistration():
    #May need to change username here each time when running for pass, to ensure there is no conflict of name entries in the db
    user = databaseAPI.Users.Users()
    assert databaseAPI.Users.Users.register(user,'anthony4', 'anthony@gmail.com', 'abc123') == 'Registration Successful'
    assert databaseAPI.Users.Users.register(user,'bobsmith2001', 'bobbysmith3@hotmail.com', 'mypassword') == 'Unique username only'
'''
    
def testLogin():
    user = databaseAPI.Users.Users()
    assert databaseAPI.Users.Users.login(user,'bobsmith2001', 'password123') == 'Login Successful'
    assert databaseAPI.Users.Users.login(user,'xxx', 'xxx') == 'Login Failed'


def testCourseRegistration():
    user = databaseAPI.Users.Users()
    assert databaseAPI.Users.Users.registerCourse(user, 'bobsmith2001', 'Python', 'Y') == 'You have been registered in Python'
    assert databaseAPI.Users.Users.registerCourse(user, 'bobsmith2001', 'Python', 'N') == ''


def testSettings():
    assert courseFunctionality.settings("E") == "Language chosen successfully"
    assert courseFunctionality.settings("D") == "Languages supported: English, please type 'E"

def testDiscussionPost():
    course = databaseAPI.Course.Course()
    assert course.discussionPost('C++', 'Does anyone know the answer to the quiz question?') == ("Post Succeessful")
    assert course.discussionPost('JavaScript', '') == ("Post Failed")


def testLessonContent():
    lesson = databaseAPI.Lessons.Lessons()
    assert databaseAPI.Lessons.Lessons.displayLesson(lesson,'C++') == [('C++', 'Lesson 1: OOP', 'In this lesson we will cover OOP')]
    assert databaseAPI.Lessons.Lessons.displayLesson(lesson,'Python') == [('Python', 'The Basics', 'This lesson will cover the basics of Python')]


def testShowHint():
    quiz = databaseAPI.Quiz.Quiz()
    assert databaseAPI.Quiz.Quiz.getHint(quiz,'Python', 'Y', False) == 'Have you ever used Semicolons?'
    assert databaseAPI.Quiz.Quiz.getHint(quiz,'Python', 'N', False) == ''


def testAnswerFeedback():
    quiz = databaseAPI.Quiz.Quiz()
    assert databaseAPI.Quiz.Quiz.getFeedback(quiz,'Python', 'No', '0') == 'Correct!'
    assert databaseAPI.Quiz.Quiz.getFeedback(quiz,'Python', 'Yes', '0') == 'Wrong! 0 tries used'

    

def testCourseRecommendations():
    course = databaseAPI.Course.Course()
    recc = courseFunctionality.courseRecommendations(course, 'Python')
    assert recc == "reccomended course: Python"
    recc = courseFunctionality.courseRecommendations(course, 'JavaScript' )
    assert recc == False
    pass


def testQuiz():
    course = databaseAPI.Course.Course()
    quiz = databaseAPI.Quiz.Quiz()
    recc = courseFunctionality.startQuiz('Python', quiz)
    assert recc == 'You may now start your quiz'



