from abc import ABC, abstractmethod


class instruments(ABC):
    def __init__(self, name, sound):
        self.name=name
        self.sound=sound

    @abstractmethod
    def make_sound():
        pass

class piano(instruments):
    def __init__(self, name, sound):
        super().__init__(name, sound)

    def make_sound(self):
        print(f"The {self.name} makes a {self.sound} sound!")

    def __del__(self):
        print(f"{self.name} has been deleted")

class guitar(instruments):
    def __init__(self, name, sound):
        super().__init__(name, sound)

    def make_sound(self):
        print(f"The {self.name} makes a {self.sound} sound!")

    def __del__(self):
        print(f"{self.name} has been deleted")

class violin(instruments):
    def __init__(self, name, sound):
        super().__init__(name, sound)

    def make_sound(self):
        print(f"The {self.name} makes a {self.sound} sound!")

    def __del__(self):
        print(f"{self.name} has been deleted")

p=piano("piano", "pling")
p.make_sound()

g=guitar("guitar", "twang")
g.make_sound()

v=violin("violin", "screech")
v.make_sound()

print("\n")
