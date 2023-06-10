
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











import re
import sys
import datetime


class Question:
    def __init__(self, question_text, answer):
        self.question_text = question_text
        self.answer = answer
        self.active = True
        self.show_count = 0
        self.correct_count = 0

    def disable(self):
        self.active = False

    def enable(self):
        self.active = True

    def display_statistics(self):
        percentage = self.correct_count / self.show_count * 100 if self.show_count > 0 else 0
        print(f"Question: {self.question_text}")
        print(f"Active: {'Yes' if self.active else 'No'}")
        print(f"Times Shown: {self.show_count}")
        print(f"Percentage Correct: {percentage:.2f}%\n")


class QuizQuestion(Question):
    def __init__(self, question_text, answer, options):
        super().__init__(question_text, answer)
        self.options = options

    def display_question(self):
        print(f"Question: {self.question_text}")
        for i, option in enumerate(self.options):
            print(f"{chr(65 + i)}. {option}")
        print()

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()


class FreeFormQuestion(Question):
    def display_question(self):
        print(f"Question: {self.question_text}\n")

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()


class InteractiveLearningTool:
    def __init__(self):
        self.questions = []
        self.load_questions()

    def load_questions(self):
        try:
            with open("questions.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    question_data = line.strip().split(";")
                    if len(question_data) == 4:
                        question = QuizQuestion(question_data[0], question_data[1], question_data[2:])
                        question.active = question_data[3] == "True"
                    elif len(question_data) == 3:
                        question = FreeFormQuestion(question_data[0], question_data[1])
                        question.active = question_data[2] == "True"
                    else:
                        continue
                    self.questions.append(question)
        except FileNotFoundError:
            pass

    def save_questions(self):
        with open("questions.txt", "w") as file:
            for question in self.questions:
                if isinstance(question, QuizQuestion):
                    line = f"{question.question_text};{question.answer};{';'.join(question.options)};{question.active}\n"
                elif isinstance(question, FreeFormQuestion):
                    line = f"{question.question_text};{question.answer};{question.active}\n"
                else:
                    continue
                file.write(line)

    def add_question(self):
        question_type = input("Select question type (quiz/freeform): ")
        question_text = input("Enter the question: ")
        answer = input("Enter the answer: ")

        if question_type.lower() == "quiz":
            options = []
            for i in range(3):
                option = input(f"Enter option {chr(65 + i)}: ")
                options.append(option)
            question = QuizQuestion(question_text, answer, options)
        elif question_type.lower() == "freeform":
            question = FreeFormQuestion(question_text, answer)
        else:
            print("Invalid question type.")
            return

        self.questions.append(question)
        self.save_questions()
        print("Question added successfully.")

    def statistics_viewing(self):
        for i, question in enumerate(self.questions):
            print(f"Question {i+1}:")
            question.display_statistics()

    def disable_enable_mode(self):
        question_id = input("Enter the question ID: ")
        try:
            question_id = int(question_id)
            question = self.questions[question_id - 1]
            print("Question details:")
            question.display_question()
            action = input("Disable or enable the question (d/e): ")
            if action.lower() == "d":
                question.disable()
                print("Question disabled.")
            elif action.lower() == "e":
                question.enable()
                print("Question enabled.")
            else:
                print("Invalid choice.")
        except (ValueError, IndexError):
            print("Invalid question ID.")

    def practice_mode(self):
        active_questions = [q for q in self.questions if q.active]
        if len(active_questions) < 5:
            print("Please add at least 5 questions before entering practice mode.")
            return

        while True:
            question = self.get_weighted_random_question(active_questions)
            question.display_question()
            user_answer = input("Enter your answer (or 'q' to quit): ")
            if user_answer.lower() == "q":
                break

            if question.check_answer(user_answer):
                print("Correct answer!")
                question.correct_count += 1
            else:
                print("Incorrect answer.")
            question.show_count += 1

    def get_weighted_random_question(self, questions):
        weights = [1 / (q.show_count + 1) for q in questions]
        total_weight = sum(weights)
        probabilities = [weight / total_weight for weight in weights]
        return random.choices(questions, probabilities)[0]

    def test_mode(self):
        if len(self.questions) < 5:
            print("Please add at least 5 questions before entering test mode.")
            return

        num_questions = input("Enter the number of questions for the test: ")
        try:
            num_questions = int(num_questions)
            if num_questions <= 0 or num_questions > len(self.questions):
                print("Invalid number of questions.")
                return

            test_questions = random.sample(self.questions, num_questions)
            score = 0

            print("Test starting...")
            for question in test_questions:
                question.display_question()
                user_answer = input("Enter your answer: ")
                if question.check_answer(user_answer):
                    print("Correct answer!")
                    score += 1
                else:
                    print("Incorrect answer.")

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("results.txt", "a") as file:
                file.write(f"Score: {score}/{num_questions} ({timestamp})\n")

            print(f"\nTest finished. Score: {score}/{num_questions}")
        except ValueError:
            print("Invalid number of questions.")

    def main(self):
        while True:
            print("Select an option:")
            print("A. Adding questions")
            print("B. Statistics viewing")
            print("C. Disable/Enable questions")
            print("D. Practice mode")
            print("E. Test mode")
            print("Q. Quit")
            choice = input("Enter your choice: ")

            if choice.lower() == "a":
                self.add_question()
            elif choice.lower() == "b":
                self.statistics_viewing()
            elif choice.lower() == "c":
                self.disable_enable_mode()
            elif choice.lower() == "d":
                self.practice_mode()
            elif choice.lower() == "e":
                self.test_mode()
            elif choice.lower() == "q":
                break
            else:
                print("Invalid choice.")

        self.save_questions()


if __name__ == "__main__":
    tool = InteractiveLearningTool()
    tool.main()









NOTES:

            valid_options = [
                "Adding questions",
                "Statistics viewing",
                "Disable/enable",
                "Practice mode",
                "Test mode"
            	"Quit"
            ]
        try:
            choise = print(
        f"""
Select an option:
A. {valid_options[0]}
B. {valid_options[1]}
C. {valid_options[2]}
D. {valid_options[3]}
E. {valid_options[4]}
Q. {valid_options[5]}
        """
                )