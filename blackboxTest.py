import pytest
import databaseAPI.Course, databaseAPI.Payments


#This method is tested using the black box input coverage partitioning technique called 'Input Partition + Shotgun Testing' 
#Each partition is described in the comment headers

def testCourseSearch():
    course = databaseAPI.Course.Course()
    
    #Test for uppercase and lower case inputs
    assert databaseAPI.Course.Course.courseSearch(course,'Python') == 'Python found!'
    assert databaseAPI.Course.Course.courseSearch(course,'python') == 'Python found!'
    assert databaseAPI.Course.Course.courseSearch(course,'PYTHON') == 'Python found!'
    assert databaseAPI.Course.Course.courseSearch(course,'C++') == 'C++ found!'
    assert databaseAPI.Course.Course.courseSearch(course,'c++') == 'C++ found!'
    assert databaseAPI.Course.Course.courseSearch(course,'How to Make Your First Website') == 'How to Make Your First Website found!'
    assert databaseAPI.Course.Course.courseSearch(course,'how to make your first website') == 'How to Make Your First Website found!'
    assert databaseAPI.Course.Course.courseSearch(course,'HOW TO MAKE YOUR FIRST WEBSITE') == 'How to Make Your First Website found!'

    # Test for partial inputs.
    assert databaseAPI.Course.Course.courseSearch(course,'Pyth') == 'Python found!'
    assert databaseAPI.Course.Course.courseSearch(course,'C+') == 'C++ found!'
    assert databaseAPI.Course.Course.courseSearch(course,'how to make') == 'How to Make Your First Website found!'

    #Test for inputs that don't exist in the database
    assert databaseAPI.Course.Course.courseSearch(course,'Java') == 'No such course found'
    assert databaseAPI.Course.Course.courseSearch(course,'How to make your first Script') == 'No such course found'
    
    #Test for longer inputs
    assert databaseAPI.Course.Course.courseSearch(course,'Python3') == 'No such course found'
    assert databaseAPI.Course.Course.courseSearch(course,'C Language') == 'No such course found'
    assert databaseAPI.Course.Course.courseSearch(course,'Java21') == 'No such course found'
    

def testPayment():

    payment = databaseAPI.Payments.Payments()

    #Normal successful output
    assert databaseAPI.Payments.Payments.takePayment(payment,'bobsmith2001', '1234 5678 13456', '123 Main Street') == 'Payment method entered successfully'
    
    #Test for numbers shorter than 13
    assert databaseAPI.Payments.Payments.takePayment(payment,'bobsmith2001', '123 777', '54 Collingwood Street') == 'Length should be 15 [xxxx xxxx xxxxx]'
    
    #Test for wrong addresses
    assert databaseAPI.Payments.Payments.takePayment(payment,'bobsmith2001','1234 5678 13456', 'Main Street') == 'Address not valid'
    assert databaseAPI.Payments.Payments.takePayment(payment,'bobsmith2001','1234 5678 13456', '123') == 'Address not valid'
    
    #Test for numbers longer than 13
    assert databaseAPI.Payments.Payments.takePayment(payment,'bobsmith2001','1234 5678 13456 6789', '123 Main Street') == 'Length should be 15 [xxxx xxxx xxxxx]'
    
    #Test for numbers with no spaces; wrong format
    assert databaseAPI.Payments.Payments.takePayment(payment,'bobsmith2001','1234567813456', '123 Main Street') == 'Length should be 15 [xxxx xxxx xxxxx]'
    
    #Test for wrong format
    assert databaseAPI.Payments.Payments.takePayment(payment,'bobsmith2001','1234-5678-13456', '123 Main Street') == 'Payment method entered successfully'
