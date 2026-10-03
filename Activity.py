from abc import ABC, abstractmethod


class species(ABC):
    def __init__(self, name, habitat):
        self.name=name
        self.habitat=habitat

    @abstractmethod
    def speak():
        pass

class dog(species):
    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)
        self.breed=breed

    def speak(self):
        print("The dog says: hello!")

    def __del__(self):
        print(f"{self.name} has been deleted")

class crow(species):
    def __init__(self, name, habitat, color):
        super().__init__(name, habitat)
        self.color=color

    def speak(self):
        print("The crow says: hello!")

    def __del__(self):
            print(f"{self.name} has been deleted")

class koalas(species):
    def __init__(self, name, habitat, status):
        super().__init__(name, habitat)
        self.status=status

    def speak(self):
        print("The koala says: hello!")

    def __del__(self):
            print(f"{self.name} has been deleted")

d=dog("Attila", "India", "Newfoundland")
d.speak()

c=crow("Will", "Forests", "black")
c.speak()

k=koalas("Percy", "Jungles", "Endangered")
k.speak()

print("\n")
