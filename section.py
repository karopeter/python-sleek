# Functions

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')
    
print("Start")
greet_user("John", "Smith")
print("Finish")

# Return Statement

def square(number):
   return number * number

print(square(3))

# Exceptions
try:
   age = int(input('Age: '))
   income = 20000
   risk = income / age
   print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')
    
    
# Classes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")
  
point = Point(10, 20)
point.x = 11
print(point.x)
#point1 = Point()
#point1.x = 10
#point1.y = 20
#print(point1.x)
#point1.draw()


class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")
        
john = Person("John Smith")
john.talk()
    
bob = Person("Bob Smith")
bob.talk()

# Inheritance
class Mammal:
    def walk(self):
        print("walk")
        
class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def be_annoying(self):
        print("annoying")

dog1 = Dog()
dog1.walk()

    
