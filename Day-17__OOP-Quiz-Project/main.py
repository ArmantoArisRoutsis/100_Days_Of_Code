from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for i in question_data:
  text = i["text"]
  answer = i["answer"]
  new_question = Question(text,answer)
  question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

print("This is the end of the quiz")
print(f"Your final score was {quiz.score}/{quiz.q_num}")