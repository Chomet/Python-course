from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    questionobj = Question(question["text"], question["answer"])
    question_bank.append(questionobj)

brain = QuizBrain(question_bank)

cont = True
while brain.still_has_questions() and cont:
    answer = brain.next_question()
    cont = brain.check_answer(answer)
print(f"Quiz is over! Final score: {brain.question_number}/{len(question_bank)}")