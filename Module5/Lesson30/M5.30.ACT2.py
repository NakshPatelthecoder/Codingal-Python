from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move (self):
        print("I can walk and run.I am very intelligent.")

class Snake(Animal):
    def move(self):
        print("I can crawl.I can be venomous.")

class Dog(Animal):
    def move(self):
        print("I can bark.I can fetch an object.")

class Lion(Animal):
    def move(self):
        print("I can roar very loadly.")


R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()