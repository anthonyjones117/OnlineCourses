import sqlite3

#This class holds lesson information for a given Course
class Lessons:
    def __init__(self, db_name="SIMLearn.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.createTable()

    #This will create the initial table for Lessons
    def createTable(self):
        
        #Create Users Table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS lessons (
            courseTitle TEXT PRIMARY KEY,
            lessonName TEXT NOT NULL,
            lessonDescription TEXT NOT NULL
        );
        """
        create = self.cursor.execute(create_table_query)
        if create is None:
            #Table 'lessons' existed so do None
            pass
        else:
            #Table has now been created, add init values
            self.createLesson('C++', 'Lesson 1: OOP', 'In this lesson we will cover OOP')
            self.createLesson('Python','The Basics','This lesson will cover the basics of Python')
            self.createLesson('How to Make Your First Website','Developing the Front End','This section will teach you how to start with HTML')
            
        
        self.conn.commit()
    #This function will create some initial Lesson values
    def createLesson(self, courseTitle, lessonName, lessonDescription):
        initQuery = "INSERT OR IGNORE INTO lessons (courseTitle, lessonName, lessonDescription) VALUES (?, ?, ?);"
        initExec = self.cursor.execute(initQuery, (courseTitle, lessonName, lessonDescription))
        self.conn.commit()
        return
    
    #This method allows a user to view Lesson information of a given Course
    def displayLesson(self, courseName):
        query = "SELECT * FROM lessons WHERE courseTitle = ?;"
        self.cursor.execute(query, (courseName,))
        return(self.cursor.fetchall())
    def close(self):
        self.conn.close()

    # Usage example
if __name__ == "__main__":
    lesson = Lessons()
    output = (lesson.displayLesson("Python"))
    print(output)
