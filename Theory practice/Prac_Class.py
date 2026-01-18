'''class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        self.name = name          # Instance attribute
        self.age = age            # Instance attribute

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing class attribute
print(Dog.species)     # ✅ "Canis familiaris"
print(dog1.species)    # ✅ "Canis familiaris"

# Accessing instance attribute
print(dog1.name)       # ✅ "Buddy"
print(dog2.name)       # ✅ "Max"
print(Dog.name)        # ❌ Error
dog1.species = "Wolf"  # Creates a new instance attribute
print(dog1.species)    # "Wolf"
print(dog2.species)    # "Canis familiaris"
print(Dog.species)     # "Canis familiaris"'''
'''class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def deposit(self, rupees):
        self.amount += rupees
        print(f"{self.name} deposited {rupees}. New balance: {self.amount}")

    def withdraw(self, rupees):
        if rupees <= self.amount:
            self.amount -= rupees
            print(f"{self.name} withdrew {rupees}. New balance: {self.amount}")
        else:
            print("Insufficient funds!!")

    def display(self):
        print(f"Hi {self.name}, your current balance is ₹{self.amount}")
account1 = BankAccount("Alice", 1000)
account1.display()          # Hi Alice, your current balance is ₹1000       
account1.deposit(500)      # Alice deposited 500. New balance: 1500
account1.withdraw(200)     # Alice withdrew 200. New balance: 1300'''
'''
class student:

    def __init__(self,name,rollNo,DOB):
        self.name=name
        self.rollNo=rollNo
        self.DOB=DOB

    def jobs(self,position):
        self.postion=position

import datetime as dt

name=input("Enter your name:")
rollNo=input("Enter your roll number:")
DOBY=int(input("Enter your date of birth year(YYYY):"))
DOBM=int(input("Enter your date of birth month(MM):"))
DOBD=int(input("Enter your date of birth day(DD):"))

p_c=input('are you placed? (yes/no):').strip().lower()
if p_c=='yes':
    position=input('enter your position:')
else:
    position='not placed'

s1=student(name,rollNo)
s1.jobs(position)
print(f"Name:{s1.name}\nRoll Number:{s1.rollNo}\nDate of Birth:{s1.DOB}\nPosition:{s1.postion}")'''
'''class Book:
    def __init__(self,book, author):
        self.book=book
        self.author=author
book=input("Enter book name:")
author=input("Enter author name:")
b1=Book(book,author)
print(f"Book:{b1.book}\nAuthor:{b1.author}")'''

class Student:
    schoolName= 'School of computing'
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(self.name)
        print(self.marks)
name=input()
marks=int(input())
s1=Student(name,marks)
s1.display()
        
        

