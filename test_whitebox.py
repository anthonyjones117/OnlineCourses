import pytest

import databaseAPI.Quiz
import getHintMutants

#Test 1: Statement coverage for the getFeedback() method
def testAnswerFeedback():
    assertCourse = databaseAPI.Quiz.Quiz()
    assert assertCourse.getFeedback('Python','Maybe?',1) == ('Wrong! 1 tries used')
    assert assertCourse.getFeedback('Python','Maybe?',2) == ('Wrong! 2 tries used')
    assert assertCourse.getFeedback('Python','Maybe?',3) == ('You are out of tries')
    assert assertCourse.getFeedback('Python','No',1) == ('Correct!')



#Test 2: Mutation testing for the getHint() method
#Only the inputs where the methods had a different output than expected are executed here
def testHintMutants():
    quiz = databaseAPI.Quiz.Quiz()
    quiz.hintAlreadyGiven = False #global class variable initialized
    assert getHintMutants.getHintMutant1(quiz,'Python', 'Y') != 'Have you ever used Semicolons?'
    quiz.hintAlreadyGiven = True #changing this to true should mean that a hint was already given
    assert getHintMutants.getHintMutant1(quiz,'Python', 'Y') != 'You already got your hint'
    assert getHintMutants.getHintMutant2(quiz,'Python', 'N') != ''
    assert getHintMutants.getHintMutant2(quiz,'Python', 'Y') != 'You already got your hint'
    quiz.hintAlreadyGiven = False #changed back for more tests
    #assert getHintMutants.getHintMutant2(quiz,'Python', 'N') != ''
    assert getHintMutants.getHintMutant3(quiz,'Python', 'Y') != 'Have you ever used Semicolons?'
    assert getHintMutants.getHintMutant3(quiz,'Python', 'N') != ''
    assert getHintMutants.getHintMutant4(quiz,'Python', 'Y') != 'Have you ever used Semicolons?'
    assert getHintMutants.getHintMutant5(quiz,'Python', 'Y') != 'Have you ever used Semicolons?'
  
