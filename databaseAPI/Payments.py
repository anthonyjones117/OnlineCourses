import sqlite3

#This class manages a user's payment
class Payments:
    def __init__(self, db_name="SIMLearn.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.createTable()

    #This will create the payment table
    def createTable(self):
        #Create Payments Table if it doesn't exist
        createTableQuery = """
        CREATE TABLE IF NOT EXISTS payments (
            username TEXT PRIMARY KEY,
            cardNumber BIGINT NOT NULL,
            billingAddress TEXT NOT NULL
        );
        """
        self.cursor.execute(createTableQuery)
        doesExist = self.cursor.fetchone()
        if doesExist is not None:
            #Table 'Payments' existed so do None
            pass
        else:
            #Table has now been created, add init values
            self.takePayment("admin", "1111 1111 11111", "25 Union St")
            self.takePayment("bobsmith2001","3940 3598 27893", "32 John Street")
            self.takePayment('johnjones12',"4029 3093 43111","12 Johnny Apple Road")
            self.takePayment('craig502',"4045 3035 22284", "158 Union St")
        self.conn.commit()

    #This allows a user to set up some payment information
    def takePayment(self, username, cardNumber, billingAddress):
        if (len(cardNumber)!=15):
            return 'Length should be 15 [xxxx xxxx xxxxx]'
        if (billingAddress.count(' ')!=2):
            return 'Address not valid'
        insert_query = "INSERT OR IGNORE INTO payments (username, cardNumber, billingAddress) VALUES (?, ?, ?);"
        self.cursor.execute(insert_query, (username, cardNumber, billingAddress))
        self.conn.commit()
        return 'Payment method entered successfully'

    #This method lets a user check for payment information
    def checkPayment(self, username, cardNumber):
        query = "SELECT * FROM payments WHERE username = ? AND cardNumber = ?;"
        self.cursor.execute(query, (username, cardNumber))
        paymentDetail = self.cursor.fetchone()
        if paymentDetail:
            return True
        else:
            return False
   
    def close(self):
        self.conn.close()

# Usage example
if __name__ == "__main__":
    paymentManager = Payments()
    if paymentManager.takePayment("boweofhwe3005","4845 3598 27893", "42 John Street"):
        print("Payment successful")
    else:
        print("Payment failed")
    paymentManager.close()
