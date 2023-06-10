import re
import sys
import datetime



# after input program has to get input in order to choose what what to do next. User should be able to choose one of these solutions: 
    # Adding questions.
    # Statistics viewing.
    # Disable/enable questions.
    # Practice mode.
    # Test mode.
    # (Bonus) Profile Select
# Ask for input and test it if it is in library.     
   

# Adding questions mode: 
# use class to describe question mode 
    # def quiz questions 
        #abc type. User decides input Questions and 3 answers A B C 
    #def free-from questions 
        # user give input Questions and Answer
        # input stored in file 
    # Questions should be saved on separate file so that once the program is close and opened again the questions remain same 
    # user has to input 5 questions before moving forward. 
    # use try len(questions) < 5: 
    # Need to determine how file are stored 
        

# Statistics viewing mode: 
    # This mode should print out questions which are in the system. 
    # Each questions should have: 
        # ID number 
        # Active questions or not
        # The question text
        # The number of times is was shown during practise or test 
        # The percentage of time is was shoen correct
s
# Disable/Enable questions mode: 
    # If user inputs questions ID code: 
        # prompt message with  question and answer with question if this one should be enablad or disabled. 
        # if disable it should not be used in practise or test stages 
        # enable/disable should be stored in main file 

# Practise mode: 
    # the mode there questions are given non-stop till hard stop
    # the questions are chosen in such a way that the questions that answered should apear less likely. 
    # This info should be stored in file with correct answered questions counted 

# Test mode: 
    # The mode there knowledge is tested 
    # Number of questions is sellected with no more than current questions number. 
    # Questions are sellected randomly, Only once 
    # Result of test are shown with score 
    # Results are stored in separate file results.txt with date and time added next to score 

    
        
# def main: 
    # Ask what solutions should proceed with input
    # Check if input is in library 
        # if answer is A: 
            # try: 
                # add questions
            # except ctrl + c: 
                # if lenght (questions) > 5 
                    #sys.exit 
                # else:
                    # print message 
                    # add questions
    
        # if answer is B: 
            # statistics_viewing()
        
        # if answer is C: 
            # disable_enable mode()
    
        # if answer is D: 
            # practise_mode ()
    
        # if answer is E: 
            # test_mode()
    
        
# Technical requirements:
    # use regular expresion
    # use classes 
    # use file i/o
    # write 3 unit tests
    # store output files in github 

            
    