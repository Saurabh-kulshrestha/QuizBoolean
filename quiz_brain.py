# quiz_brain.py — Handles the logic and flow of the QuizBoolean game.
from art import logo,line,clr

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0            # Tracks current question number
        self.question_list = q_list         # List of Question objects
        self.score = 0                      # Stores the user's current score

    def still_has_questions(self):
        # Returns True if there are more questions left in the quiz
        return self.question_number < len(self.question_list)

    def next_question(self):
        print(line)     # Print a line separator for better display

        # Get the current question and ask the user
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")

        # Check if the user's answer is correct
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        # Compare user input with the correct answer (case-insensitive)
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")

        # Show the correct answer and current score
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print(line)
        print(clr)