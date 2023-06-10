import re
import sys
import datetime

class Question: 
    def __init__(self, question_text, answer, choice): 
        self.id = id
        self.question_type = question_type
        self.question_text = question_text
        self.answer = answer 
        self.active = True
        self.show_count = 0 
        self.correct_count = 0
        
    def question_type(self, choise):
        
        valid_options = [
            "Adding questions",
            "Statistics viewing",
            "Disable/enable",
            "Practice mode",
            "Test mode",
            "Quit"
        ]

        try: 
            if choice.lower() == "adding questions":
                return valid_options[0]
            elif choice.lower() == "statistics viewing":
                return valid_options[1]
            elif choice.lower() == "disable/enable":
                return valid_options[2]
            elif choice.lower() == "practice mode":
                return valid_options[3]
            elif choice.lower() == "test mode":
                return valid_options[4]
            elif choice.lower() == "quit":
                sys.exit()
        except KeyboardInterrupt: 
            sys.exit()
        
        
    def disable(self):
        self.active = False 

    def enable(self): 
        self.active = True 

    def id (self): 
        return random.randrange(100, 999)

    def display_statistics (self): 
        #has to be withou print 
        percentage = self.corrrect_count / self.show_count * 100 if self.show_count .0 else 0 
        print(f"ID: {self.id}")
        print(f"Question: {self.question_text}")  
        print(f"Answer: {self.answer}")
        print(f"Active: {'Yes' if self.active else 'No'}")
        print(f"Times Shown: {self.show_count}")
        print(f"Percentage Correct: {percentage:.2f}%\n")
            
class QuizQuestion (Question): 
    def __init__(self.question_text, answer, options):
        super().__init__ (self, question_text, answer): 
        self.options = options 

    def display_question (self): 
        print(f"Question: {self.question_text}")
        for index, option in enumerate.(self.options): 
            print(f"{chr(65 + index)}. {option}")
        print()
    
    def check_answer (self, user_answer):
        return user_answer.lower() == self.answer.lower()

class FreeFormQuestion(Question): 
    def display_question(self): 
        print (f"Question: {self.question_text}\n")
    
    def check_anwer(self, user_answer): 
        return user_answer.strip.lower() == self.answer.strip.lower()


class InteractiveLearninTool: 
    def __init__ (self): 
        #store questions in file
        self.questions = []
        self.load_questions()
            
    def load_questions(self):
        try: 
            with open("questions.txt", "r") as file: 
                lines = file.readlines()
                for line in lines: 
                        question_data = line.strip.split(;)
                        if len(question_data) == 4 