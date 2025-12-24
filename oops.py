# ===============================
# 🔹 1. Class and Object
# ===============================
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Creating object
animal = Animal("Generic Animal")
animal.speak()  # Output: Generic Animal makes a sound

# ===============================
# 🔹 2. Encapsulation
# ===============================
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = Account("Yash", 1000)
acc.deposit(500)
print(f"Balance for {acc.owner}: {acc.get_balance()}")  # Output: 1500

# ===============================
# 🔹 3. Inheritance
# ===============================
class Dog(Animal):  # Inherits from Animal
    def speak(self):
        print(f"{self.name} barks")

dog = Dog("Tommy")
dog.speak()  # Output: Tommy barks

# ===============================
# 🔹 4. Polymorphism
# ===============================
class Cat:
    def speak(self):
        print("Meow")

class Duck:
    def speak(self):
        print("Quack")

animals = [Dog("Bruno"), Cat(), Duck()]

for a in animals:
    a.speak()  # Output: Bruno barks, Meow, Quack

# ===============================
# 🔹 5. Abstraction
# ===============================
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print(f"Area of circle: {circle.area()}")  # Output: 78.5
