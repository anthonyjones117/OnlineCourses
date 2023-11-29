import sqlite3

#This class allows management of Users for the website
class Users:
    def __init__(self, dbName="SIMLearn.db"):
        self.dbName = dbName
        self.conn = sqlite3.connect(dbName)
        self.cursor = self.conn.cursor()
        self.createTable()
        self.username = None
    def createTable(self):
        
        #Create Users Table if it doesn't exist
        createTableQuery = """
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            courseTitle TEXT
        );
        """
        create = self.cursor.execute(createTableQuery)
        if create is None:
            #Table 'users' existed so do None
            pass
        else:
            #Table has now been created, add init values
            self.register("admin", "admin@example.com", "admin_password")
            self.register("bobsmith2001","bobsmith@gmail.com","password123")
            self.register('johnjones12','johnjones@gmail.com','mypassword')
            self.register('craig502','craig502@gmail.com','thisIsMyPassword')
        
        self.conn.commit()

    #This method allows to register new users into the database
    def register(self, username, email, password):
        initQuery = "INSERT OR IGNORE INTO users (username, email, password) VALUES (?, ?, ?);"
        initExec = self.cursor.execute(initQuery, (username, email, password))
        self.conn.commit()
        self.username = username
        
        return 'Unique username only' if initExec.rowcount == 0 else 'Registration Successful'
    
    #This method will check login credentials against the user database to authenticate
    def login(self, username, password):
        query = "SELECT * FROM users WHERE username = ? AND password = ?;"
        self.cursor.execute(query, (username, password))
        user = self.cursor.fetchone()
        if user:
            self.username = username
            return 'Login Successful'
        else:
            return 'Login Failed'
    
    #This method let's a user register to a specific course
    def registerCourse(self, username, courseTitle, decision):
        if (decision == 'Y'):
            registerUserCourse = "INSERT OR IGNORE INTO users (courseTitle, username) VALUES (?, ?);"
            initExec = self.cursor.execute(registerUserCourse, (courseTitle, username))
            self.conn.commit()
            return ('You have been registered in ' + str(courseTitle))
        else:
            return ''
    def close(self):
        self.conn.close()

# Usage example
if __name__ == "__main__":
    userManager = Users()
    if userManager.login("bobsmith2001", "password123"):
        print("Login successful")
        print(userManager.username)
        userManager.registerCourse(userManager.username,"Python")
    else:
        print("Login failed")

    userM = Users()
    if userM.register("boith2001","bobsmh@gmail.com","password123"):
        print("Register again!")
    else:
        print("haha")
        print(userManager.username)

    userManager.close()
