import sqlite3

#This class contains overall Course information
class Course:
    def __init__(self, dbName="SIMLearn.db"):
        self.dbName = dbName
        self.conn = sqlite3.connect(dbName)
        self.cursor = self.conn.cursor()
        self.createTable()

    #This function will create the initial course Table
    def createTable(self):
        
        #Create Users Table if it doesn't exist
        createTableQuery = """
        CREATE TABLE IF NOT EXISTS course(
            courseTitle PRIMARY KEY,
            courseGenre NOT NULL,
            courseDifficulty NOT NULL,
            postContent TEXT
        );
        """
        create = self.cursor.execute(createTableQuery)
        if create is None:
            #Table 'course' existed so do None
            pass
        else:
            #Table has now been created, add init values
            self.initializeCourses('Python','Language','Beginner')
            self.initializeCourses('C++','Language','Intermediate')
            self.initializeCourses('How to Make Your First Website','Web Development','Intermediate')
            
        self.conn.commit()

    #This function will retrieve all course titles of available courses
    def getAllCourses(self):
        getQuery = "SELECT courseTitle FROM course;"
        self.cursor.execute(getQuery)
        courses = self.cursor.fetchall()
        courses = list(courses)
        return(courses)

    #This function will initialize some course information
    def initializeCourses(self, courseTitle, courseGenre, courseDifficulty):
        initQuery = "INSERT OR IGNORE INTO course (courseTitle, courseGenre, courseDifficulty) VALUES (?, ?, ?);"
        self.cursor.execute(initQuery, (courseTitle, courseGenre, courseDifficulty))
        self.conn.commit()

    #Search: return true if Course exists else false
    def courseSearch(self, searchInput):
        searchInput = '%'+searchInput+'%'
        query = "SELECT * FROM course WHERE courseTitle LIKE ? ;"
        self.cursor.execute(query, (searchInput,))
        course = self.cursor.fetchone()
        if course:
            return str(course[0]) + ' found!'
        else:
            return 'No such course found'
        
    #This function will allow a user to make a discussion post for a specific course
    def discussionPost(self, courseTitle, postContent):
        if (postContent!=""):
            insertQuery = """
            UPDATE course SET postContent = ? WHERE courseTitle = ?
            """
            self.cursor.execute(insertQuery, (postContent, courseTitle))
            self.conn.commit() 
            return ("Post Succeessful")
        else:
            return ("Post Failed")

    #This function will request a specific course information ********** do we need this one *********
    def getCourse(self, courseTitle):
        getQuery = "SELECT courseTitle FROM course;"
        self.cursor.execute(getQuery)
        return(self.cursor.fetchall())
    def close(self):
        self.conn.close()

# Usage example
if __name__ == "__main__":
    courseManager = Course("courses.db")
    #courseManager.discussionPost("Python","Hello")
    #print(courseManager.courseSearch("Python"))
    # courseManager.getAllCourses()
    # courseManager.close()
    print(courseManager.getAllCourses())
