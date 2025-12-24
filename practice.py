# # class Rectangle():
# #     def __init__(self,Length, Width):
# #         self.Width = Width
# #         self.Length = Length
# #     def Area(self):
# #         return self.Length*self.Width
# #     def Perimeter(self):
# #         return 2*(self.Length+self.Width)
# # r=Rectangle(10,12)
# # print(r.Area(),r.Perimeter())




# # class BankAccount:
# #     def __init__(self,account_holder,balance):
# #         self.account_holder = account_holder
# #         self.balance = balance
# #     def deposit(self):
# #         money=int(input("enter amount to be deposited "))
# #         self.balance = self.balance+money
# #         print(f"succesfull now balance is {self.balance}")
        
# #     def withdrawl(self):
# #         Taken=int(input("eneter amount to be withdrawn "))
# #         self.balance-=Taken
# #         print("succesfull") 
# #     def display_balance(self):
# #         print(self.balance) 
# # B= BankAccount("Yash",1000000)           
# # B.deposit()
# # B.withdrawl()
# # B.display_balance()



# class Student:
#     def __init__(self,name, roll_number,marks):
#         self.name =name
#         self.roll_number=roll_number
#         self.marks=marks
#     def Result(self):
#         if self.marks >= 90:
#             print(f"{self.name} got A grade")
#         elif self.marks >= 80:
#             print(f"{self.name} got B grade")
#         elif self.marks >= 70:
#             print(f"{self.name} got C grade")
#         else:
#             print(f"{self.name} got Failed")
# Students=[Student("Yash","N4",90),                 
# Student("luffy","N5",80),  
# Student("ace","N6",70),  
# Student("sabo","N7",60)]  
# for S in Students:

#     S.Result()



# # class Car:
# #     total_cars = 0
# #     def __init__(self, brand, model):
# #         self.brand = brand
# #         self.model = model
# #         Car.total_cars += 1 
# #     def start_engine(self):
# #         print(f"{self.brand} {self.model}'s engine started!")
# # car1 = Car("Toyota", "Corolla")
# # car2 = Car("Honda", "Civic")
# # car3 = Car("Tesla", "Model 3")
# # car1.start_engine()
# # car2.start_engine()
# # car3.start_engine()
# # print(f"Total cars created: {Car.total_cars}")



# # class Employee:
# #     def get_Role(self):
# #         print("im an employee")
# # class Manager(Employee):
# #     def get_Role(self):
# #         print("im manager")        
# # M=Manager()
# # E=Employee()
# # M.get_Role()
# # E.get_Role()



# # class Shopping_Cart:
# #     def __init__(self):
# #         self.Total=0
# #         self.Items={}
# #     def add_item(self):
# #         n=int(input("how many items "))
# #         for i in range(n):
# #             name=str(input("enter item "))
# #             price=int(input("enter price "))
# #             self.Items[name]=price
# #             self.Total+=price
# #         return self.Total
# #     def remove_item(self):
# #         Name=str(input("enter item to be removed "))
        
# #         if Name in self.Items:
# #             self.Total-=self.Items[Name]
# #             del self.Items[Name]
# #         else:
# #             print("item not found")
# #     def total_amount(self):
# #         print(f"total is {self.Total}")
# #         print(self.Items) 
# # S=Shopping_Cart()
# # S.add_item()
# # S.remove_item()
# # S.total_amount()



# # class Book:
# #     def __init__(self,price,title,author):
# #         self.price=price
# #         self.title=title
# #         self.author=author
# #     def __str__(self):
# #         return f"{self.title} by {self.author}"
# #     def __eq__(self,other):
# #         return self.title==other.title
# #     def __lt__(self,other):
# #         return self.price<=other.price 
# # B=Book(1000,"onepiece","oda")
# # B1=Book(1000,"onepiece 2","oda")
# # B2=Book(2000,"onepiece","oda")    
# # print(B)
# # print(B==B2)     
# # print(B<B2) 



# # class Book:
# #     def __init__(self, title, author):
# #         self.title = title
# #         self.author = author

# #     def __str__(self):
# #         return f"'{self.title}' by {self.author}"

# # class Library:
# #     def __init__(self):
# #         self.books = []

# #     def add_book(self):
# #         title = input("Enter book title: ")
# #         author = input("Enter author name: ")
# #         book = Book(title, author)  # Composition
# #         self.books.append(book)
# #         print(f"Added: {book}")

# #     def borrow_book(self):
# #         title = input("Enter book to borrow: ")
# #         for book in self.books:
# #             if book.title == title:
# #                 self.books.remove(book)
# #                 print(f"You borrowed: {book}")
# #                 return
# #         print("Book not found.")

# #     def return_book(self):
# #         title = input("Enter returned book title: ")
# #         author = input("Enter author name: ")
# #         book = Book(title, author)
# #         self.books.append(book)
# #         print(f"Returned: {book}")

# #     def show_books(self):
# #         if not self.books:
# #             print("No books in the library.")
# #         else:
# #             print("Books in library:")
# #             for book in self.books:
# #                 print(f"→ {book}")

# # L = Library()
# # L.add_book()
# # L.add_book()
# # L.show_books()
# # L.borrow_book()
# # L.show_books()
# # L.return_book()
# # L.show_books()



# # from abc import ABC, abstractmethod
# # class Shapes(ABC):
# #     @abstractmethod
# #     def area(self):
# #         pass
# #     def perimeter(self):
# #         pass
    
# # from abc import ABC, abstractmethod
# # import math


# # class Shape(ABC):
# #     @abstractmethod
# #     def area(self):
# #         pass

# #     @abstractmethod
# #     def perimeter(self):
# #         pass


# # class Rectangle(Shape):
# #     def __init__(self, length, breadth):
# #         self.length = length
# #         self.breadth = breadth

# #     def area(self):
# #         return self.length * self.breadth

# #     def perimeter(self):
# #         return 2 * (self.length + self.breadth)


# # class Square(Shape):
# #     def __init__(self, side):
# #         self.side = side

# #     def area(self):
# #         return self.side * self.side

# #     def perimeter(self):
# #         return 4 * self.side


# # class Circle(Shape):
# #     def __init__(self, radius):
# #         self.radius = radius

# #     def area(self):
# #         return math.pi * self.radius ** 2

# #     def perimeter(self):
# #         return 2 * math.pi * self.radius


# # class Triangle(Shape):
# #     def __init__(self, a, b, c):
# #         self.a = a
# #         self.b = b
# #         self.c = c

# #     def area(self):
# #         s = (self.a + self.b + self.c) / 2
# #         return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))  # Heron's formula

# #     def perimeter(self):
# #         return self.a + self.b + self.c

# # R = Rectangle(5, 3)
# # C = Circle(4)
# # S = Square(6)
# # T = Triangle(3, 4, 5)

# # print("Rectangle: ", R.area(), R.perimeter())
# # print("Circle: ", C.area(), C.perimeter())
# # print("Square: ", S.area(), S.perimeter())
# # print("Triangle: ", T.area(), T.perimeter())



# # import datetime
# # import functools

# # # Logger class
# # class Logger:
# #     def __init__(self, filename='log.txt'):
# #         self.filename = filename

# #     def log(self, func):
# #         """Decorator to log method calls with timestamps, args, and return values."""
# #         @functools.wraps(func)
# #         def wrapper(*args, **kwargs):
# #             timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# #             method_name = func.__name__

# #             # Call the actual method
# #             result = func(*args, **kwargs)

# #             # Prepare log entry
# #             log_entry = (f"[{timestamp}] Called method: {method_name} "
# #                          f"Args: {args[1:]}, Kwargs: {kwargs}, Returned: {result}\n")

# #             # Write to file
# #             with open(self.filename, 'a') as f:
# #                 f.write(log_entry)

# #             # Also print log entry to console
# #             print(log_entry, end="")

# #             return result
# #         return wrapper

# # # Apply the logger to another class
# # class Calculator:
# #     logger = Logger()

# #     @logger.log
# #     def add(self, a, b):
# #         return a + b

# #     @logger.log
# #     def multiply(self, a, b):
# #         return a * b

# # # Using the Calculator
# # calc = Calculator()
# # print("Add Result:", calc.add(5, 3))
# # print("Multiply Result:", calc.multiply(4, 2))



# # class Singleton:
# #     _instance = None  # Class-level attribute to store the single instance

# #     def __new__(cls, *args, **kwargs):
# #         if cls._instance is None:
# #             print("Creating new instance...")
# #             cls._instance = super(Singleton, cls).__new__(cls)
# #         else:
# #             print("Using existing instance...")
# #         return cls._instance

# #     def __init__(self, value):
# #         self.value = value


# # obj1 = Singleton("First")
# # print(f"obj1.value = {obj1.value}")

# # obj2 = Singleton("Second")
# # print(f"obj2.value = {obj2.value}")

# # print(f"obj1 is obj2: {obj1 is obj2}")  # Should be True



# # class Person:
# #     def whoami(self):
# #         print("I am a person")

# # class Engineer(Person):
# #     def whoami(self):
# #         print("I am an engineer")

# # class Doctor(Person):
# #     def whoami(self):
# #         print("I am a doctor")

# # class SuperHuman(Engineer, Doctor):
# #     pass

# # s = SuperHuman()
# # s.whoami()
# # help(SuperHuman)



# # def funargs(normal, *args, **kwargs):
# #     print(normal)
# #     for item in args:
# #         print(item)
    
# #     print("\nNow I would like to introduce some of our heroes")
# #     for key, value in kwargs.items():
# #         print(f"{key} is a {value}")

# # har = ["Harry", "Rohan", "SkillF", "Hammad"]
# # normal = "I am a normal Argument and the students are:"
# # kw = {"Rohan": "Monitor", "Harry": "Fitness Instructor"}
# # funargs(normal, *har, **kw)




# class yashwanth:
#     def __init__(self,age,status,gender):
#         self.age = age
#         self.status = status
#         self.gender = gender

#     def details(self):
#         print(f'Yashwanth details are age : {self.age}, status : {self.status} , gender : {self.gender}')
# y = yashwanth(22,'Single','Male')  
# y.details()          


# import keyword

# def is_valid_identifier(s):
#     return s.isidentifier() and not keyword.iskeyword(s)

# print(is_valid_identifier("name"))      # True
# print(is_valid_identifier("2name"))     # False
# print(is_valid_identifier("for"))       # False (keyword)
# print(is_valid_identifier("_value"))    # True
name = 'yashwanth'
for i in name:
    if i == 'z':
        print('true')
else:
    print('false')
        