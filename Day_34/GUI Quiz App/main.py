from ui import QuizInterface
from data import questions
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in questions:
    question_text = question["question"]
    question_answer  = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz_model = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz_model)

print("You've completed the quiz")
print(f"Your final score was: {quiz_model.score}/{quiz_model.question_no}")