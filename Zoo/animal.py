from abc import ABC, abstractmethod

class Animal(ABC):  # Abstraction
    def __init__(self, name):
        self._name = name  # Encapsulation

    @abstractmethod
    def make_sound(self):  # Polymorphism
        pass

class Lion(Animal):  # Inheritance
    def make_sound(self):
        return "Roar!"

class Pet(Animal):
    name=""
    species=""
    def __init__(self,name,species):
        self._name,self._species=name,species
        pass
    def make_sound(self):
        return "Bark!"
    def speak(self):
        return "Bau Bau"
