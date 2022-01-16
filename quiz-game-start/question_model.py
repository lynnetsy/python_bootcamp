class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.correct = False

    def is_correct(self, user_answer):
        self.correct = self.answer == user_answer
        return self.correct

