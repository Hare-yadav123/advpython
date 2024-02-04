# class parant:
#     def __init__(self,r):
#         self.money=r
#         self.num=555
#         print("this is a parant class")
#     def uncle(self):
#         print("you are parant of this class")
    
# class child(parant):
#     def __init__(self,m):
#         self.money=m
#         self.daular=2000
#         self.city='patna'
#         print("child class is callable")
#     def asd(self):
#             print("this is a child class")
        
# c=child(10000)
# print(c.money)
# print(c.city) 
# print(c.daular) 
# c.asd()
# c.uncle()
# p=parant(100)



# lambda is anonuams function in python whic take number of argument but give only one expression
# it define use lambda keyword

#assinging a lambda func in variable
lb=lambda x,y:print((x*y))
lb(4,5)

# wrapping lambda function inside the another functipon
def Mywraper(n):
    r= lambda a:a*n
    print(r(2))
n=Mywraper(20)



class father:
    def __init__(self,r,num):
        self.r=r
        self.num=num
        print('This is a parent class')
        
class child(father):
    def __init__(self ,r):
        
        super().__init__(r)
        print('this is child class')
c=child('raju')
print(c.r)







