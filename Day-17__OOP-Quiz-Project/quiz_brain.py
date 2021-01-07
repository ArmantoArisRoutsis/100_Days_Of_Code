class QuizBrain:
  def __init__(self,list_bank):
    self.score = 0
    self.q_num = 0
    self.list_bank = list_bank
  
  def next_question(self):
    current_question = self.list_bank[self.q_num]
    self.q_num+=1
    choice =input(f"Q.{self.q_num} {current_question.text}(True/False)?")
    self.evaluate(choice)
    self.still_has_questions()

  def still_has_questions(self):
    while len(self.list_bank) > self.q_num:
      self.next_question()
  
  def evaluate(self,choice):
    if self.list_bank[self.q_num-1].answ.lower() == choice.lower():
      self.score+=1
      print(f"You were right!\nCurrent score:{self.score}/{self.q_num}\n")
    else:
      print(f"You were wrong :(\nCurrent score:{self.score}/{self.q_num}\n")