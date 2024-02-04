'''Opps:
opps is a object oriented programming language which totaly based on class & object 
in simple language opps is a method to repersent 'real world entity' in programming


feature of opps
# class & object 
inheritance
polymorphism
abstraction 
Encapsulation
'''

# class person:
#     age=10
#     name="pooja"
#     surname="mali"
# p=person()
# print(p.age)
# print(person.age)
# print(person.name)
# print(person.surname)

class sume:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sume(self):
        ax=self.a+self.b
        return ax
s=sume(40,50)
print(s.sume())

#
'''class Test:
    def findsum( self,b, a):
        s = a + b
        return s
a = 87
b = 8
t = Test()
s = t.findsum(a, b)
print("sum is", s)'''


# class :-
    # Class is a user-defined blueprint or prototype from which object is created.

    #  Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like a "blueprint" for creating objects.
## class are created by keyword "class"



'''class Person:
    age = 10
    name="pooja"
    surname="Mali"


print(Person.age)

print(Person.name)

print(Person.surname)'''


# 1) construcator is special type of method
# 2) it fix-->__init__(self)
# 3) construcator call automatically when object of class created
# 4)construcator  only execute one time

#construcator call automatically when object of class created
'''class Student:
    def __init__(self):
        print("Construcator Automatically called")

    def m1(self):
        print("instance method ")

s1=Student()
s1.m1()'''



# construcator atleast one varibale required

class Student:
    def __init__(self):
        pass

s3=Student()

#
# without construcator
'''class Student:
    def info(self):
        print('My name is :',self.name)
        print("My age is :",self.age)
        print("My City is :",self.city)
s1=Student()
s1.name='pooja'
s1.age=23
s1.city='pune'
s1.info()'''


#
# with construcator
'''class Student:
    def __init__(demo,name,age,city):
        demo.name=name
        demo.age=age
        demo.city=city

    def info(demo):
        print('My name is :',demo.name)
        print("My age is :",demo.age)
        print("My City is :",demo.city)

s1=Student('Raj',22,'Beed')
s1.info()
print()
s2=Student("pooja",25,"pune")
s2.info()'''

## Type of variable ##

  # 1) instance variables
  # 2) static variable
  # 3)local variables
  
  # 1) instance variables :-
# The data of variable changing object to object is called as instance variables.

'''class Student:
    def __init__(self,name,age,city):
        self.name=name    #instance variable
        self.age=age    #instance variable
        self.city=city    #instance variable

    def info(self):
        print('My name is :',self.name)
        print("My age is :",self.age)
        print("My City is :",self.city)

s1=Student('pooja',22,'Beed')
s1.info()
s2=Student('Raman',21,'Seed')

'''


#with inside instance method by using self

'''class Employee:
    def __init__(self,eid,ename,ecity):
        self.Eid=eid
        self.Ename=ename
        self.Ecity=ecity

    def einfo(self):
        print("ID of Employee :",self.Eid)
        print("Name of Employee :",self.Ename)
        print("Ecity of Employee :",self.Ecity)
        self.Esalary=10000

e=Employee('E12',"apurva",'pune')
print(e.__dict__)
e.einfo()
print()
print(e.__dict__)
e.Edepartment='Web Developement'
print(e.__dict__)'''

#
### instance method
'''class Grading:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print("Name of Student ",self.name)
        print("MArks of Student ",self.marks)

    def grade(self):
        if self.marks>90:
            print("A+")
        else:
            print("C")

n=int(input("Number of student "))
for i in range(n):
    name=input("Enter Student name ")
    marks=int(input("Enter Student Marks "))
    g=Grading(name,marks)
    g.display()
    g.grade()''' 
    
    
## Static Variables
# generally static variable declare inside class but outside not change object to object is called as static variable  

#1) directly inside class but outside any method
#2) construcator by using class name
#3)inside instance method by using class name
#4)inside class method by using class name or cls name
#5) static method by using class name

'''class Demo:
    a=10
    def __init__(self):
        Demo.b=20
    def instance_method(self):
        Demo.c=30

    @classmethod
    def class_method(cls):
        Demo.d=40
        cls.e=50
    @staticmethod
    def static_method():
        Demo.f=60

print(Demo.__dict__)
d=Demo()
print(Demo.__dict__)
d.instance_method()
print(Demo.__dict__)
Demo.class_method()
print(Demo.__dict__)
Demo.static_method()
print(Demo.__dict__) '''
    

## How to access instance variable
# inside method
'''class Emp:
    def __init__(self,eid,ename):
        self.eid=eid
        self.ename=ename

    def m1(self): #inside method access variable
        print("inside method:",self.ename)

e=Emp('E33','apurva')
e.m1()'''

# outside class

class Emp:
    def __init__(self,eid,ename):
        self.eid=eid
        self.ename=ename

    def m1(self):
        print("inside method:",self.ename)

e=Emp('E33','apurva')
e.m1()
print("outside class",e.eid) #outside class

#Local variable
class Localvar:
    def m1(self):
        x=10
        print(x)
    def m2(self):
        x=20
        print(x)

l=Localvar()
l.m1()
l.m2()

import django
print(django.get_version)