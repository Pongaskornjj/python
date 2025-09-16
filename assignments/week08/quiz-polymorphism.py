"""
Demonstrate polymorphism by creating:

    A base class Animal with method move()
    Three derived classes: Fish, Bird, Dog with different implementations of move()
        fish swims, bird flies, dog runs
    A function that takes any animal and calls its move() method
"""

class Animal:
    def move(self):
        pass

class Fish(Animal):
    def move(self):
        print("Fish swims")

class Bird(Animal):
    def move(self):
        print("Bird flies")

class Dog(Animal):
    def move(self):
        print("Dog runs")

def animal_move(animal):
    animal.move()

# Example usage
if __name__ == "__main__":
    animals = [Fish(), Bird(), Dog()]
    for a in animals:
        animal_move(a)