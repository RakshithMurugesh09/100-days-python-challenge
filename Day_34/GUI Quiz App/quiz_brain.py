import html

class QuizBrain:
    def __init__(self, question_bank):
        self.questions_bank = question_bank
        self.question_no = 0
        self.score = 0
        self.current_question = None

    def still_has_questions(self):
        return self.question_no < len(self.questions_bank)

    def next_question(self):
        self.current_question = self.questions_bank[self.question_no]
        self.question_no += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_no}: {q_text}"

    def check_answer(self,user_input):
        correct_answer = self.current_question.answer
        if user_input == correct_answer:
            self.score += 1
            return True
        else:
            return False

