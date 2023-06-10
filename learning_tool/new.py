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
    print("Adding questions mode:")

    while len(self.questions) < 5:
        question_type = input("Enter the question type (quiz/freeform): ")
        if question_type.lower() == "quiz":
            question_text = input("Enter the quiz question: ")
            options = []
            for i in range(3):
                option = input(f"Enter option {i+1}: ")
                options.append(option)
            correct_answer = input("Enter the correct option (A/B/C): ")

            question = QuizQuestion(question_text, options, correct_answer)
            self.questions.append(question)
            print("Question added.")

        elif question_type.lower() == "freeform":
            question_text = input("Enter the freeform question: ")
            correct_answer = input("Enter the correct answer: ")

            question = FreeformQuestion(question_text, correct_answer)
            self.questions.append(question)
            print("Question added.")

        else:
            print("Invalid question type.")

    print("Minimum question limit reached. Exiting the 'Adding questions' mode.")


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
