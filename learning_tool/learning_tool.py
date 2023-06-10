import random
import datetime

class Question:
    def __init__(self, question_id, question_text, is_active):
        self.question_id = question_id
        self.question_text = question_text
        self.is_active = is_active
        self.num_shown = 0
        self.num_correct = 0
    
    def show_question(self):
        self.num_shown += 1
    
    def check_answer(self, user_answer):
        pass

class QuizQuestion(Question):
    def __init__(self, question_id, question_text, is_active, answer_options, correct_answer):
        super().__init__(question_id, question_text, is_active)
        self.answer_options = answer_options
        self.correct_answer = correct_answer
    
    def show_question(self):
        super().show_question()
        # Display question and answer options to the user
        pass
    
    def check_answer(self, user_answer):
        is_correct = user_answer == self.correct_answer
        if is_correct:
            self.num_correct += 1
        return is_correct

class FreeFormQuestion(Question):
    def __init__(self, question_id, question_text, is_active, expected_answer):
        super().__init__(question_id, question_text, is_active)
        self.expected_answer = expected_answer
    
    def show_question(self):
        super().show_question()
        # Display question to the user
        pass
    
    def check_answer(self, user_answer):
        is_correct = user_answer == self.expected_answer
        if is_correct:
            self.num_correct += 1
        return is_correct

class Profile:
    def __init__(self, profile_name):
        self.profile_name = profile_name
        self.question_stats = {}
    
    def update_question_stats(self, question_id, is_correct):
        if question_id not in self.question_stats:
            self.question_stats[question_id] = {'num_shown': 0, 'num_correct': 0}
        self.question_stats[question_id]['num_shown'] += 1
        if is_correct:
            self.question_stats[question_id]['num_correct'] += 1

class LearningTool:
    def __init__(self):
        self.questions = {}
        self.profiles = {}
        self.current_profile = None
    
    def add_question(self, question):
        self.questions[question.question_id] = question
    
    def disable_question(self, question_id):
        if question_id in self.questions:
            self.questions[question_id].is_active = False
    
    def enable_question(self, question_id):
        if question_id in self.questions:
            self.questions[question_id].is_active = True
    
    def create_profile(self, profile_name):
        if profile_name not in self.profiles:
            self.profiles[profile_name] = Profile(profile_name)
    
    def select_profile(self, profile_name):
        if profile_name in self.profiles:
            self.current_profile = self.profiles[profile_name]
    
    def practice_mode(self):
        if len(self.questions) < 5:
            print("At least 5 questions are required to enter practice mode.")
            return
        
        while True:
            # Choose a question using weighted random selection
            question = random.choices(list(self.questions.values()), weights=[q.num_shown for q in self.questions.values()])[0]
            question.show_question()
            user_answer = input("Your answer: ")
            is_correct = question.check_answer(user_answer)
            if self.current_profile:
                self.current_profile.update_question_stats(question.question_id, is_correct)
            print("Correct!" if is_correct else "Incorrect!")
            if input("Continue practicing? (y/n): ").lower() != "y":
                break
    
    def test_mode(self, num_questions):
        if num_questions > len(self.questions):
            print("Insufficient number of questions.")
            return
        
        test_questions = random.sample(list(self.questions.values()), num_questions)
        score = 0
        
        for question in test_questions:
            question.show_question()
            user_answer = input("Your answer: ")
            is_correct = question.check_answer(user_answer)
            if self.current_profile:
                self.current_profile.update_question_stats(question.question_id, is_correct)
            if is_correct:
                score += 1
        
        print("Test completed.")
        print("Score:", score)
        self.save_test_result(score)
    
    def save_test_result(self, score):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = f"{timestamp}: {self.current_profile.profile_name} - Score: {score}\n"
        with open("results.txt", "a") as file:
            file.write(result)

# Usage example
learning_tool = LearningTool()

# Adding questions
quiz_question = QuizQuestion(1, "What is the capital of France?", True, ["Paris", "London", "Madrid"], "Paris")
learning_tool.add_question(quiz_question)

freeform_question = FreeFormQuestion(2, "What is the full form of CPU?", True, "Central Processing Unit")
learning_tool.add_question(freeform_question)

# Disable/Enable questions
learning_tool.disable_question(2)

# Statistics viewing
for question in learning_tool.questions.values():
    print("Question ID:", question.question_id)
    print("Active:", question.is_active)
    print("Question Text:", question.question_text)
    print("Number of times shown:", question.num_shown)
    print("Percentage of correct answers:", (question.num_correct / question.num_shown) * 100)

# Practice mode
learning_tool.practice_mode()

# Test mode
learning_tool.test_mode(3)

# Profile Select
learning_tool.create_profile("Profile1")
learning_tool.create_profile("Profile2")
learning_tool.select_profile("Profile1")
learning_tool.practice_mode()
learning_tool.select_profile("Profile2")
learning_tool.test_mode(2)
