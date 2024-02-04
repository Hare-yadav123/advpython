#   class /static variable
# class variables are  the those varible whose single copy is available to all the instance of class
# if we modufy the copy variable in instance ,it will effect all the copy in the other instance

# to access variable we need class method cls as first parameterthen ,we can access  class variable using cls.varible_name

class Mobile:
    r='god'  # class varible
    def __init__(self):
        self.model="realme11"
         
    def A(self):
        print(self.model)
        
    @classmethod
    def is_ram(cls): 
        cls.r
m=Mobile()
print(m.r) #cls.variable name(cls.r) and Mobile.variable name(Mobile.r)

#Q. example  @classmethod
# class Mobile:
#     name="Haree"
#     @classmethod
#     def show(cls,t):
#         cls.time=t
#         print("we can see time in the",cls.time)
#         print(cls.name)
#         print("you are bestr friend")
        
# m=Mobile()
# m.show("watch")


# Q. example @staticmethod
# class Mobile:
#     name="Haree"
#     @staticmethod
#     def show(t,p):
#         time=t
#         price=p
#         print("we can see time in the:*",time)
#         print("there prise is:",price)
#         #print(Mobile.name)
#         print("you are bestr friend")
        
# m=Mobile()
# print(m.name)
# m.show("watch",1000)

# class A:
#     name='Ranu'
#     def get(self):
#         self.name
#     @classmethod
#     def show(cls): 
#        return cls.name
    
# s=A()
# print(s.show())

