class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        print(f"Q{self.question_number + 1}: {current_question.text}")
        return input("true or false? ").lower()

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer):
        current_question = self.question_list[self.question_number]
        if answer == current_question.answer.lower():
            self.question_number += 1
            print("Correct!")
            return True
        else:
            print(f"Wrong!")
            return False

