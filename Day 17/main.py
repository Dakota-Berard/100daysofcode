from question_model import Question
from data import question_data
from quiz_brain import QuestionBank
question_list = []

# for i in range(0, len(question_data)):
#     question_list.append(Question(question_data[i].get('text'), question_data[i].get('answer')))
#     print(question_list[i].text)

for question in question_data:
    question_list.append(Question(question['text'], question['answer']))

question_bank = QuestionBank(question_list)

while question_bank.still_has_questions():
    question_bank.next_question()

print("You've completed the quiz")
print(f"Your final score was: {question_bank.score}/{question_bank.question_number}")