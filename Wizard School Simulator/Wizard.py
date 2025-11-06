from abc import ABC,abstractmethod
class Wizard(ABC):
    def __init__(self,name,speciality):
        self._name=name
        self._speciality=speciality
    @abstractmethod
    def cast_spell(self):
        pass
class FireWizard(Wizard):
    def __init__(self,name,speciality="🔥 Fireball!"):
        super().__init__(name,speciality)
    def cast_spell(self):
        return self._speciality
    
    def get_name(self):
        return self._name
class HealerWizard(Wizard):
    def __init__(self,name,speciality="💚 Healing Light!"):
        super().__init__(name,speciality)
    
    def cast_spell(self):
        return self._speciality
    def get_name(self):
        return self._name