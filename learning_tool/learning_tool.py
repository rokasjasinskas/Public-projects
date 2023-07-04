import csv
import re
import datetime
import random


class Question:
    def __init__(self, question_text, answer, question_type):
        self.id = id
        self.question_type = question_type
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
        percentage = (
            self.correct_count / self.show_count * 100 if self.show_count != 0 else 0
        )
        print(f"ID: {self.id}")
        print(f"Question: {self.question_text}")
        print(f"Answer: {self.answer}")
        print(f"Active: {'Yes' if self.active else 'No'}")
        print(f"Times Shown: {self.show_count}")
        print(f"Percentage Correct: {percentage:.2f}%\n")


class QuizQuestion(Question):
    def __init__(self, question_text, answer, options, question_type):
        super().__init__(question_text, answer, question_type)
        self.options = options

    def display_question(self):
        print(f"Question: {self.question_text}")
        for index, option in enumerate(self.options):
            print(f"{chr(65 + index)}. {option}")
        print()

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()


class FreeFormQuestion(Question):
    def display_question(self):
        print(f"Question: {self.question_text}\n")

    def check_answer(self, user_answer):
        return user_answer.strip().lower() == self.answer.strip().lower()


class InteractiveLearningTool:
    def __init__(self):
        self.questions = []
        self.load_questions()

    def load_questions(self):
        try:
            with open("questions.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Question Type"].lower() == "quiz":
                        question = QuizQuestion(
                            row["Question Text"],
                            row["Answer"],
                            row["Options"].split(";"),
                            row["Question Type"],
                        )
                    elif row["Question Type"].lower() == "freeform":
                        question = FreeFormQuestion(
                            row["Question Text"], row["Answer"], row["Question Type"]
                        )
                    else:
                        continue

                    question.id = row["ID"]
                    question.active = row["Active"].lower() == "true"
                    question.show_count = int(row["Show Count"])
                    question.correct_count = int(row["Correct Count"])

                    self.questions.append(question)
        except FileNotFoundError:
            pass

    def save_questions(self):
        fieldnames = [
            "ID",
            "Question Type",
            "Question Text",
            "Answer",
            "Options",
            "Active",
            "Show Count",
            "Correct Count",
        ]
        with open("questions.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for question in self.questions:
                row = {
                    "ID": question.id,
                    "Question Type": question.question_type,
                    "Question Text": question.question_text,
                    "Answer": question.answer,
                    "Options": ";".join(question.options)
                    if isinstance(question, QuizQuestion)
                    else "",
                    "Active": "True" if question.active else "False",
                    "Show Count": question.show_count,
                    "Correct Count": question.correct_count,
                }
                writer.writerow(row)

    def add_question(self):
        question_type = input("Select question type (quiz/freeform): ")
        question_text = input("Enter the question: ")
        answer = input("Enter the answer: ")

        if  not re.match(r'^[a-zA-ZO9\s]+$', answer):
            print ("Invalid answer format. Only alphanumeric characters and space are allowed")
            return 
        

        if question_type.lower() == "quiz":
            options = []
            for i in range(3):
                option = input(f"Enter option {chr(65 + i)}: ")
                options.append(option)
            question = QuizQuestion(question_text, answer, options, question_type)
        elif question_type.lower() == "freeform":
            question = FreeFormQuestion(question_text, answer, question_type)
        else:
            print("Invalid question type.")
            return

        question.id = str(random.randrange(100, 999))
        self.questions.append(question)
        self.save_questions()
        print("Question added successfully.")

    def statistics_viewing(self):
        for i, question in enumerate(self.questions):
            print(f"Question {i + 1}:")
            question.display_statistics()

    def disable_enable_mode(self):
        question_id = input("Enter the question ID: ")
        try:
            question_id = int(question_id)
            question = None
            for q in self.questions:
                if int(q.id) == question_id:
                    question = q
                    break
            if question is not None:
                print("Question details:")
                question.display_question()
                action = input("disable or enable the question (d/e):")
                if action.lower() == "d":
                    question.disable()
                    self.save_questions()
                    print("Question disabled.")
                elif action.lower() == "e":
                    question.enable()
                    self.save_questions()
                    print("Question enabled.")
                else:
                    print("Invalid choice.")
            else:
                print("Invalid question ID.")
        except ValueError:
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