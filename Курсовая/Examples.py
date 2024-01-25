# Пример класса с атрибутами и методами
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print(account.get_balance())
account.deposit(500)
print(account.get_balance())
account.withdraw(200)
print(account.get_balance())



# Применение инкапсуляции
class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if len(new_name) > 0:
            self._name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age

person = Person("Alice", 25)
print(person.get_name())
person.set_name("Bob")
print(person.get_name())
print(person.get_age())
person.set_age(30)
print(person.get_age())



# Работа с полиморфизмом
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

def make_sound(animal):
    return animal.sound()

dog = Dog()
cat = Cat()

print(make_sound(dog))
print(make_sound(cat))
Глава 2: Практическая часть



# Примеры создания классов
class SimpleClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

simple_instance = SimpleClass("Value1", "Value2")
print(simple_instance.attribute1)
print(simple_instance.attribute2)
2.2 Использование наследования



# Использование наследования
class ParentClass:
    def __init__(self, attribute1):
        self.attribute1 = attribute1

    def print_attribute(self):
        print(self.attribute1)

class ChildClass(ParentClass):
    def __init__(self, attribute1, attribute2):
        super().__init__(attribute1)
        self.attribute2 = attribute2

child_instance = ChildClass("Value1", "Value2")
child_instance.print_attribute()
print(child_instance.attribute2)



# Работа с полиморфизмом
class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

def calculate_area_of_shape(shape):
    return shape.calculate_area()

circle = Circle(5)
square = Square(4)

print(calculate_area_of_shape(circle))
print(calculate_area_of_shape(square))



# Пример приложения с использованием классов
class Student:
    def __init__(self, student_id, first_name, last_name, age):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.courses = {}

    def register_course(self, course):
        self.courses[course.code] = []

    def assign_grade(self, course_code, grade):
        if course_code in self.courses:
            self.courses[course_code].append(grade)

    def get_grades(self, course_code):
        return self.courses.get(course_code, [])

class Course:
    def __init__(self, code, name):
        self.code = code
        self.name = name