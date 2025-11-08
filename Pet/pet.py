class Pet:
    def __init__(self,name,species,age):
        self._name=name
        self._species=species
        self._age=age
    def describe(self):
        print(f"{self._name} is a {self._age}-year-old {self._species}")