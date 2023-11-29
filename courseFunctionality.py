from databaseAPI.Course import Course
from databaseAPI.Lessons import Lessons
from databaseAPI.Users import Users
from databaseAPI.Quiz import Quiz
#Allow the user to search for a course in the database 
'''
def courseSearch(course, searchInput):
    if(Course.courseSearch(searchInput)==True):
        print(searchInput + " found!")
    else:
        print('No courses of that name found')
'''

#Allow the user to search a topic and see if there are any relevant courses
'''def courseRecommendations(course, searchInput):
    print('Here are reccommended courses for', searchInput)

    if(Course.courseSearch(course, searchInput)==True):
        print("reccomended course: ", searchInput)   
        return
    else:
        print('No such field or interests as, showing all results')
        for i in Course.getAllCourses(course): 
            print(i)    
        return
'''
#Allow the user to search a topic and see if there are any relevant courses
def courseRecommendations(course, searchInput):
    print('Here are reccommended courses for', searchInput)

    if(Course.courseSearch(course, searchInput)!='No such course found'):
        print("reccomended course: ", searchInput)   
        return ("reccomended course: "+ str(searchInput))
    else:
        print(searchInput)
        print(Course.courseSearch(course,searchInput))
        print(f'No such field or interests as {searchInput}, showing all results')
        for i in Course.getAllCourses(course): 
            print(i)    
        return False
        
#Choose a specific course and view potential options to interact with it including lessons, disucssion, or quizzes
def openCoursePage(selectInput):
    #Based on input ^ we pull from lessonsDB the lesson content
    currLesson = Lessons()
    course=Course()
    currUser = Users()
    currQuiz = Quiz()
    #Based on input ^ we pull from Quiz the quiz content
    #Based on input ^ we pull from Discussion the discussion content
    print("Welcome to the course for: "+ selectInput)

    print('Would you like to register in the course officially?')
    registerOfficial = input('Y/N: ')
    if (registerOfficial == 'Y'):
        if (currUser.registerCourse(currUser.username, selectInput, registerOfficial)==('You have been registered in ' +str(selectInput))):
            print('You have been registered in ', selectInput)
        
    choice= input("Please Choose What You'd Like To Do Today: \n Type 'L' for Course Lessons \n Type 'D' for Discussion Posts \n \
Type 'Q' for Quiz:\n Choose:")
    if (choice == 'L'):
        print("Lesson! For Course: "+ selectInput)
        print(currLesson.displayLesson(selectInput))
    elif (choice == 'D'):
        disc= input("Add discussion post: ")
        print(course.discussionPost(selectInput, disc))
    elif (choice == 'Q'):
        startQuiz(selectInput, currQuiz)
        currQuiz.doQuiz(selectInput)
    else:
        openCoursePage(selectInput)

def startQuiz(selectInput, currQuiz):
    return 'You may now start your quiz'

#Allow the user to choose language settings
def settings(lang):
    if (lang!="E"):
        return("Languages supported: English, please type 'E")
        
    else:
        return("Language chosen successfully")
            



#Test file      
if __name__ == "__main__":
    thisCourse = Course()
    #openCoursePage("Python")
    courseRecommendations(thisCourse, "abc")
    