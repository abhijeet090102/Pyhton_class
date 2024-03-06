from abc import abstractmethod

class Pet():
   @abstractmethod
   def makesound(self):
      pass

class Cat(Pet):
   def __init__(self, name):
       self.name = name

   def makesound(self):
      return "Meow!"

cat = Cat("Max")
print (f"I like to say {cat.makesound()}")
