#Accessor/getter method
# THIS METHOD USED TO ACCESS or READ OF DATA OF THE VARIABLE. THIS don't USE MODiFY OF DATA OF THE VARIABLE ,IT IS ALSO CALLED GETTER METHOD
'''class Mobile:
    age=30
    @classmethod
    def disp(cls):
        return cls.age
        
m=Mobile()
print(Mobile.age)
print(m.age)'''




# MUTATOR/SETTER METHOD

#Property decorator(getter,setter and deletter)

# THIS METHOD USED TO ACCESS , READ and modify OF DATA OF THE VARIABLE. THIS method CAN USE MODOFY OF DATA OF THE VARIABLE ,IT IS ALSO CALLED setter METHOD
'''class Mobile:
    def __init__(self):
        self.model="Realme c11"
        self.battery="tata"
    def set_model(self):
        self.model="Realme x12"
        self.battery="mahindra"
realme=Mobile()
#befor settor
print(realme.model)
#after setter
realme.set_model()
print(realme.model)'''

#getter method
'''class test:
    name="haree"
    def __init__(self):
        print(self.name)
        self.__show()
    def __show(self):
        print("welcome  you")
        
s=test()'''

#Exa
class Student:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        
    @property
    def email(self):
        return self.fname+"."+self.lname+"@gmail.com"
    @property
    def fullname(self):
        return self.fname+" "+self.lname
    
    @fullname.setter
    def full(self,name):
        self.fname,self.lname=name.split()
        
    @fullname.deleter
    def fullname(self):
        self.fname=None
        self.lname=None
        print("delete all")
    
    
s=Student("haree", "raj")
print(s.fullname)
print(s.email)
s.full="hansh raj"
print(s.full)
print(s.email)
del s.fullname
print(s.fname)
print(s.lname)

