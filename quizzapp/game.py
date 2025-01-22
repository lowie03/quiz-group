import requests
import random

class QuizGame:
    def __init__(self):
        self.questions = []

    def fetch_questions(self):
        response = requests.get("https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple")
        if response.status_code == 200:
            self.questions = response.json().get('results', [])
            self.format_questions()

    def format_questions(self):
        formatted_questions = []
        for question in self.questions:
            choices = question['incorrect_answers'] + [question['correct_answer']]
            random.shuffle(choices)
            formatted_question = {
                'question': question['question'],
                'answer': question['correct_answer'],
                'choices': choices
            }
            formatted_questions.append(formatted_question)
        self.questions = formatted_questions