class add:
    def __init__(self,x):
        self.x=x
        
    def __add__(self,other):
        return self.x + other.y   
class B():
    def __init__(self,y):
        self.y=y
        
a=add(100)
v=B(10)
print(a+v)       #A.__add__(self,other)

# print(int.__add__(50, 50))
# print(str.__add__('haree', 'raju'))

class M:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
m=M(30, 30)
n=M(40, 40)
print(m+n)