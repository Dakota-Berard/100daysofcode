# TODO question_number = 0
# TODO questions_list
# TODO Method Next Question

class QuestionBank:

    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list

    def next_question(self):
        x = input(f"Q.{self.question_number}: {self.questions_list[self.question_number].text} (True/False)?: ").lower()
        self.check_answer(x, self.questions_list[self.question_number].answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
