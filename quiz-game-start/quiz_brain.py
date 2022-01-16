#CREATE A CLASS WHO'S GONNA ASKING THE QUESTIONS
#CHECKING IF THE ANSWER WAS CORRECT
#CHECKING IF WE'RE THE END OF THE QUIZ
import question_model


class Quiz:
    def __init__(self):
        self.questions = []
        self.max_qualification = 10


    def add_question(self, question):
        self.questions.append(question)

    def qualification(self):
        return (self.max_qualification / len(self.questions)) * self.correct_answers()

    def correct_answers(self):
        total = 0
        for q in self.questions:
            if q.correct:
                total += 1
        return total