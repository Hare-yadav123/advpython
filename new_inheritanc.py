# class Raju:
#     def name(self):
#         print(' i am boss of raju')
# class Haree(Raju):
#     def yadav(self):
#         print('you are my boss')
# obs=Haree()
# obs.name()
# obs.yadav()

# #multiple inheritance

# class Father:
#     def fab(self):
#         print('this is a father class')    
# class Mother():
#     def mom(self):
#         print('this is a mother class ')    
# class Child(Mother,Father):
#     def son(self):
#         print('this is a son calss')    
# ob=Child()
# f=Father()
# f.fab()
# ob.fab()
# ob.mom()
# ob.son()

#MULTILEVEL INHERITANCE
# class Father:
#     def fab(self):
#         print('this is a father class')    
# class Child(Father):
#     def mom(self):
#         print('this is a Child class ')    
# class GrendChild(Child):
#     def son(self):
#         print('this is a grendchild calss')    
# ob=Child()
# ob.fab()
# ob.mom()
# ob.son()



# Hierarchical Inheritance
class Father:
    def fab(self):
        print('this is a father class')    
class Child(Father):
    def mom(self):
        print('this is a Child class ')    
class GrendChild(Father):
    def son(self):
        print('this is a grendchild calss')
class small_child(Father):
    def nam(self):
        print('this small_child')
        
obj=Father()  
gh=Child()
fj=GrendChild()
nb=small_child()  
obj.fab()
gh.mom()
fj.son()   
nb.nam()      
        


