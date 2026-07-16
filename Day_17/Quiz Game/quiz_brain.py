class QuizBrain:

    def __init__(self, question_list):
        self.questions = question_list
        self.question_no = 0
        self.score = 0

    def next_question(self):
        current_question = self.questions[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q. {self.question_no}. {current_question.question} (True/False): ").strip().lower()
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        return self.question_no < len(self.questions)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Wrong!")
        print("\nCorrect Answer is", correct_answer)
        print("Current Score is", self.score, "/", self.question_no)
        print(30*"-")

