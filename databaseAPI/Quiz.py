import sqlite3

#This class holds information for a quiz object, which is a child class of a specific Course
class Quiz:
    #Initilization function
    def __init__(self, dbName="SIMLearn.db"):
        self.dbName = dbName
        self.conn = sqlite3.connect(dbName)
        self.cursor = self.conn.cursor()
        self.hintAlreadyGiven = False
        self.createTable()

    #This function creates an initial table to hold quiz data 
    def createTable(self):
        
        #Create Users Table if it doesn't exist
        createTableQuery = """
        CREATE TABLE IF NOT EXISTS quiz (
            courseTitle PRIMARY KEY,
            questionGiven NOT NULL,
            hintGiven NOT NULL,
            quizAnswer NOT NULL
        );
        """
        create = self.cursor.execute(createTableQuery)
        if create is None:
            #Table 'quiz' existed so do None
            pass
        else:
            #Table has now been created, add init values
            self.initializeQuiz('Python', "Does Python require semicolons [';']?", "Have you ever used Semicolons?","No")
            self.initializeQuiz('C++',"Is C++ an Object Oriented Language?", "Does C++ support object oriented modual programming?", "Yes")
            self.initializeQuiz('How to Make Your First Website',"Is HTML a programming or markup language?", "can you write logins/algorithm on HTML?", "Markup")
            
        self.conn.commit()

    #This function is used to help intiialize some values into the quiz table
    def initializeQuiz(self, courseTitle, questionGiven, hintGiven, quizAnswer):
        initQuery = "INSERT OR IGNORE INTO quiz (courseTitle, questionGiven, hintGiven, quizAnswer) VALUES (?, ?, ?, ?);"
        self.cursor.execute(initQuery, (courseTitle, questionGiven, hintGiven, quizAnswer))
        self.conn.commit()

    #Allow a user to request a hint
    def getHint(self, courseTitle, choice):

        if (self.hintAlreadyGiven == True and choice == 'Y'):
            return 'You already got your hint'
        if (choice == 'Y' and self.hintAlreadyGiven == False):
            query = "SELECT hintGiven FROM quiz WHERE courseTitle = ?;"
            self.cursor.execute(query, (courseTitle,),)
            hintGiven = self.cursor.fetchone()
            hintGiven = (list(hintGiven))[0]
            self.hintAlreadyGiven = True
            return hintGiven
        else:
            return ''

        
    def getFeedback(self, courseTitle, ansGiven, tries):
        query = "SELECT quizAnswer FROM quiz WHERE courseTitle = ?;"
        self.cursor.execute(query, (courseTitle,),)
        quizAnswer = self.cursor.fetchone()
        quizAnswer = (list(quizAnswer))[0]
        if (int(tries)<3):
            if (int(tries)==2):
                print('The next try will be your last try!')
            if (ansGiven == quizAnswer):
                return 'Correct!'          
            else:
                wrongOutput = 'Wrong! ' + str(tries) + ' tries used'
                return wrongOutput
        else:
            return 'You are out of tries'


    #This method allows a user to go through the actions of a quiz. Questions and Answers are retrieved from the database
    def doQuiz(self, courseTitle):

        query = "SELECT questionGiven FROM quiz WHERE courseTitle = ?;"
        self.cursor.execute(query, (courseTitle,),)
        questions = self.cursor.fetchone()
        questions = (list(questions))[0]
        

        if (questions):
            print('You may now start your quiz')
            tries=1
            while True:
                print("\n\nThis is your question: ")
                print(questions)

               
                print("Do you need a hint [Y/N]")
                choice = input()
                if (choice == 'Y'):
                    hintOutput = self.getHint(courseTitle, choice)
                    print(hintOutput)
                else:
                    hintOutput = self.getHint(courseTitle,  choice)
                    print(hintOutput)


                ans = input("Answer: ")
                feedback = self.getFeedback(courseTitle, ans, tries)
                print(feedback)
                if (feedback == 'Correct!'):
                    break
                if (feedback == 'You are out of tries'):
                    break
                else:
                    tries+=1
                    continue
   
        else:
            print('No quiz found')

    def close(self):
        self.conn.close()

# Usage example
if __name__ == "__main__":
    courseManager = Quiz()
    courseManager.doQuiz("Python")
    courseManager.close()
