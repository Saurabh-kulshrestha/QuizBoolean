# main.py — Runs the QuizBoolean game using question data and logic from other modules.

from question_model import Question    # Importing the Question class
from data import question_data         # Importing the list of question dictionaries
from quiz_brain import QuizBrain       # Importing the quiz logic handler
from art import logo,line,clr          # Importing the quiz logic handler

# Display the game logo
print(logo)

# Create a list of Question objects from the question data
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize the quiz engine with the list of questions
quiz = QuizBrain(question_bank)

# Start the quiz and keep asking questions until finished
while quiz.still_has_questions():
    quiz.next_question()

# Show final message and score
print(line)
print(logo)
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
print(line)