from databaseAPI.Quiz import Quiz

#Original function for reference
def getHintOriginal(quiz, courseTitle, choice):

    if (quiz.hintAlreadyGiven == True and choice == 'Y'):
        return 'You already got your hint'
    if (choice == 'Y' and quiz.hintAlreadyGiven == False):
        query = "SELECT hintGiven FROM quiz WHERE courseTitle = ?;"
        quiz.cursor.execute(query, (courseTitle,),)
        hintGiven = quiz.cursor.fetchone()
        hintGiven = (list(hintGiven))[0]
        quiz.hintAlreadyGiven = True
        return hintGiven
    else:
        return ''

#Mutation: == changed to != in first 'if', first condition
def getHintMutant1(quiz, courseTitle, choice):

    if (quiz.hintAlreadyGiven != True and choice == 'Y'):
        return 'You already got your hint'
    if (choice == 'Y' and quiz.hintAlreadyGiven == False):
        query = "SELECT hintGiven FROM quiz WHERE courseTitle = ?;"
        quiz.cursor.execute(query, (courseTitle,),)
        hintGiven = quiz.cursor.fetchone()
        hintGiven = (list(hintGiven))[0]
        quiz.hintAlreadyGiven = True
        return hintGiven
    else:
        return ''
    
#Mutation: == changed to != in first 'if', second condition  
def getHintMutant2(quiz, courseTitle, choice):
    if (quiz.hintAlreadyGiven == True and choice != 'Y'):
        return 'You already got your hint'
    if (choice == 'Y' and quiz.hintAlreadyGiven == False):
        query = "SELECT hintGiven FROM quiz WHERE courseTitle = ?;"
        quiz.cursor.execute(query, (courseTitle,),)
        hintGiven = quiz.cursor.fetchone()
        hintGiven = (list(hintGiven))[0]
        quiz.hintAlreadyGiven = True
        return hintGiven
    else:
        return ''

#Mutation: == changed to != in second 'if'
def getHintMutant3(quiz, courseTitle, choice):

    if (quiz.hintAlreadyGiven == True and choice == 'Y'):
        return 'You already got your hint'
    if (choice != 'Y' and quiz.hintAlreadyGiven == False):
        query = "SELECT hintGiven FROM quiz WHERE courseTitle = ?;"
        quiz.cursor.execute(query, (courseTitle,),)
        hintGiven = quiz.cursor.fetchone()
        hintGiven = (list(hintGiven))[0]
        quiz.hintAlreadyGiven = True
        return hintGiven
    else:
        return ''

#Mutation: hintAlreadyGiven reassignment line moved to after first 'if'
def getHintMutant4(quiz, courseTitle, choice):

    if (quiz.hintAlreadyGiven == True and choice == 'Y'):
        return 'You already got your hint'
    quiz.hintAlreadyGiven = True
    if (choice == 'Y' and quiz.hintAlreadyGiven == False):
        query = "SELECT hintGiven FROM quiz WHERE courseTitle = ?;"
        quiz.cursor.execute(query, (courseTitle,),)
        hintGiven = quiz.cursor.fetchone()
        hintGiven = (list(hintGiven))[0]

        return hintGiven
    else:
        return ''
    
#Mutation: hintAlreadyGiven reassignment line moved to top
def getHintMutant5(quiz, courseTitle, choice):
    quiz.hintAlreadyGiven = True
    if (quiz.hintAlreadyGiven == True and choice == 'Y'):
        return 'You already got your hint'
    if (choice == 'Y' and quiz.hintAlreadyGiven == False):
        query = "SELECT hintGiven FROM quiz WHERE courseTitle = ?;"
        quiz.cursor.execute(query, (courseTitle,),)
        hintGiven = quiz.cursor.fetchone()
        hintGiven = (list(hintGiven))[0]
        return hintGiven
    else:
        return ''


if __name__ == "__main__":
    courseManager = Quiz()
    courseManager.hintAlreadyGiven =  False
    print(getHintOriginal(courseManager, "Python", "Y"))
    print(getHintMutant4(courseManager, "Python", "Y"))
   

    courseManager.close()
