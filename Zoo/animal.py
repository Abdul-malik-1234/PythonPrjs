from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    def __init__(self, name, age):
        self._name = name          # Encapsulation
        self._age = age

    @abstractmethod
    def make_sound(self):
        pass

    def info(self):
        return f"{self._name} is {self._age} years old."

# Subclasses with polymorphism
class Lion(Animal):
    def make_sound(self):
        return "Roar!"

class Elephant(Animal):
    def make_sound(self):
        return "Trumpet!"

class Monkey(Animal):
    def make_sound(self):
        return "Chatter!"
