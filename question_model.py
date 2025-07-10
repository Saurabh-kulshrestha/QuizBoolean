# question_model.py — Defines the Question class to store question text and its correct answer.

class Question:
    def __init__(self, text, answer):
        # Store the question text
        self.text = text
        # Store the correct answer (True/False)
        self.answer = answer
