# 1 default constructor
class default():
  def __init__(self):
    self.hello = "This is default constructor"
  def print(self):
    print(self.hello)

# driver code
obj1 = default()
obj1.print()





# 2 paramaterized constructor
class paramaterized():
  def __init__(self,f,s):
    self.first = f
    self.second = s
  def sum(self):
    self.answer = self.first + self.second
  def print(self):
    print("The first num is " + str(self.first))
    print("The second num is " + str(self.second))
    print("The answer is " + str(self.answer))

#driver code
obj1 = paramaterized(2,3)
obj1.sum()
obj1.print()
