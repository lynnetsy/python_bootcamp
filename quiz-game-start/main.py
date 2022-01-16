from data import question_data
from question_model import Question
from quiz_brain import Quiz
# Goal: Create a question bank, a list of questions from question_data


quiz = Quiz()

for q in question_data:
    question = Question(q["text"], q["answer"])
    quiz.add_question(question)

for q in quiz.questions:
    print("=============================================================================")
    print(q.question)
    user_answer = input("True or False\n")
    user_answer = user_answer == "True"
    print(".............................................................................")
    if q.is_correct(user_answer):
        print("La respuesta es correcta")
    else:
        print("Valiste vrg")

print("-----------------------------------------------------------------------------")
print(f"Tu calificación es de {quiz.qualification()}")