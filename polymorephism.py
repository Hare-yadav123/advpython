# polymorephism means many form 

'''ch can it can define a entity wchich can define for multi role ,its capability is called 
polymorephism'''

# TYPES OF POLYMOREWPHISM 
# 1) method overloading

class Poly:
    def calu(self , num1=5,num2=None,num3=None):
        if num1 !=None and num2 !=None and num3 !=None :
            print('method overloading',num1+num2+num3)
        elif num1 !=None and num2 !=None:
            print('method overloading',num1*num2)
        else:
            print('method overloading',num1)
ob=Poly()
ob.calu(20)


# METHOD OVERRIDING
class Add:
    def Result(self, a,b):
        return a+b
    
class Multi(Add):
    def Result(self,a,b ): # multi class method override the parent class method
        return a*b
m=Multi()
print('method overriding',m.Result(20, 10))


''' super method use in overriding call parents class method'''
class Add:
    def Result(self, x,y):
        print('addtion:',x+y)
class Multi(Add):
    def Result(self,a,b ):
        super().Result(30, 60)
        return a*b
m=Multi()
print(m.Result(20,20))

