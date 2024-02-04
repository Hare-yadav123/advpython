#single inheritance
class parent:
    def Per_fun(self):
    
        print("This is a parent class")
        
class Child(parent):
    def chi_fun(self):
        print("this is a child class")
ch=Child()
ch.chi_fun()
ch.Per_fun()

#MultiInheritance
class GrandFather:
    def __init__(self,a_name):
        self.aname=a_name
        
class Papa(GrandFather):
    def __init__(self, b_name,a_name):
        self.bname=b_name
        
        # invoke of constructor of class Grandfather
        GrandFather.__init__(self, a_name) # or super().__init__(a_name) here in super method no need self keyword
                                            # insted of class name "GrandFather" we can use
class Grand_son(Papa):
    def __init__(self, c_name,b_name,a_name):
        self.cname=c_name
        
        # invoke of constructor of class Papa
        Papa.__init__(self, b_name,a_name)
        
    def Display(self):
        print("name of dada:",self.aname)
        print("name of papa:",self.bname)
        print("name of beta:",self.cname)
        
obj=Grand_son("Aapa","Jappa","Dabba")
obj.Display()


# multiInheritance

class Papa:
    def papa_func(self):
        print("This is a papa class")
        
class Mom:
    def mom_func(self):
        print("This is a mom class")
        
class child_class(Papa,Mom):
    def chil_func(self):
        print("this is a child class")
        self.papa_func()
        self.mom_func()
        
obj=child_class()
obj.chil_func()


# Hierarchical Inheritance
class A:
    def a_func(self):
        print("I am the parant class")
class B(A):
    def b_func(self):
        print("I am the first child")
        
class C(A):
    def c_func(self):
        print("i am the second child")
        
obj1=B()
obj1.a_func()
obj1.b_func()
print("************")
obj2=C()
obj2.a_func()
obj2.c_func()

# How do you access Base or parent class member in the child class

'''we can use parent class name access the attribute'''

class Base:
    def __init__(self,Name):
        self.Name=Name
class cheldren(Base):
    def __init__(self,age,Name):
        self.age=age
        Base.Name=Name
        
    def chil_dis(self):
        print(self.age,Base.Name)
obj3=cheldren(20,'Raju')
obj3.chil_dis()

'''we can also use super() function access the attribute of the parent class in child class'''

class Base:
    def __init__(self,Name):
        self.Name=Name
class cheldren(Base):
    #constructor
    def __init__(self,age,Name):
        # Note Base.Name can't be used
        # here super() used in constructor
        super(cheldren,self).__init__(Name)
        self.age=age
    
    def chil_dis(self):
        print(self.age,self.Name)
obj3=cheldren(28,'Ram')
obj3.chil_dis()

# Are  access specifier used in pythion
#to demonstrate access specifiers 
class InterviewEmplioyee:
    # protected member
    _emp_name="haree"
    _age=None
    
    #private member
    __branch=None
    #constructor
    def __init__(self,emp_name,age,branch):
        self._emp_name=emp_name
        self._age=age
        self.__branch=branch
     # public member   
    def show_Details(self):
        print(self._emp_name,self._age,self.__branch)
ie=InterviewEmplioyee('haree' ,21,'Mechanical Engineering')
ie.show_Details()


# How will you cheak if a class is child class of another class
''' This is done by usin method  called issubclass() provided by python '''

class parent:
    pass
class child(parent):
    pass
print(issubclass(child,parent))
print(issubclass(parent,child))

# write python program whether veriable is integer or string
#we can cheak  if an object is an instance of class by making instance()
print('cheak  child and parent class*********s')
ob1=child()
ob2=parent()
print(isinstance(ob1,child))
print(isinstance(ob2, parent))

print('*********************************************')
print(isinstance(20, int)) or print(isinstance(25, str))
print(isinstance([25],int)) or print(isinstance([25], str))
print(isinstance('20', int)) or print(isinstance('20', str))